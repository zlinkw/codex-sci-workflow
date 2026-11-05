"""Resolve explicitly selected Codex TeX review marks, without network or backups."""

import argparse
import codecs
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
import sys


MARK = re.compile(r"\\codex(replace|add|delete)\s*\{([1-9][0-9]*|[a-z]+)\}")
VERBATIM = re.compile(r"\\begin\{(verbatim\*?|Verbatim|lstlisting|minted|comment)\}")


@dataclass(frozen=True)
class Change:
    kind: str
    id: str
    start: int
    end: int
    new: str
    old: str
    line: int


def code_mask(text):
    """Preserve offsets while excluding TeX comments and literal environments."""
    result = list(text)
    i = 0
    while i < len(text):
        if text[i] == '%':
            end = text.find('\n', i)
            end = len(text) if end < 0 else end
            result[i:end] = ' ' * (end - i)
            i = end
        elif text[i] == '\\':
            literal = VERBATIM.match(text, i)
            if literal:
                closing = '\\end{' + literal.group(1) + '}'
                end = text.find(closing, literal.end())
                if end < 0:
                    raise ValueError('Unclosed literal environment at offset ' + str(i))
                end += len(closing)
                result[i:end] = ['\n' if c == '\n' else ' ' for c in text[i:end]]
                i = end
            elif re.match(r'\\verb\*?(?![A-Za-z])', text[i:]):
                prefix = re.match(r'\\verb\*?', text[i:]).group()
                start = i + len(prefix)
                if start >= len(text) or text[start].isspace():
                    raise ValueError('Invalid verb delimiter')
                end = text.find(text[start], start + 1)
                if end < 0 or '\n' in text[start:end]:
                    raise ValueError('Unclosed verb literal')
                end += 1
                result[i:end] = ' ' * (end - i)
                i = end
            else:
                if i + 1 < len(text) and text[i + 1] in '{}':
                    result[i + 1] = ' '
                i += 2
        else:
            i += 1
    return ''.join(result)


def group(text, mask, start):
    while start < len(mask) and mask[start].isspace():
        start += 1
    if start >= len(mask) or mask[start] != '{':
        raise ValueError('Expected braced argument at offset ' + str(start))
    depth = 1
    i = start + 1
    while i < len(mask):
        if mask[i] == '{':
            depth += 1
        elif mask[i] == '}':
            depth -= 1
            if depth == 0:
                return text[start + 1:i], i + 1
        i += 1
    raise ValueError('Unclosed braced argument at offset ' + str(start))


def changes(text):
    mask = code_mask(text)
    items = []
    seen = set()
    for match in MARK.finditer(mask):
        kind, change_id = match.groups()
        if change_id in seen:
            raise ValueError('Duplicate review ID: ' + change_id)
        first, end = group(text, mask, match.end())
        if kind == 'replace':
            old, end = group(text, mask, end)
            new = first
        elif kind == 'add':
            new, old = first, ''
        else:
            new, old = '', first
        if items and match.start() < items[-1].end:
            raise ValueError('Nested review marks require manual reconciliation')
        seen.add(change_id)
        items.append(Change(kind, change_id, match.start(), end, new, old,
                            text.count('\n', 0, match.start()) + 1))
    return items


def resolve(text, items, selected, action):
    known = {item.id for item in items}
    if not selected or not selected <= known:
        raise ValueError('Select existing IDs only; unknown=' + ','.join(sorted(selected - known)))
    result = text
    for item in reversed(items):
        if item.id in selected:
            retained = item.new if action == 'accept' else item.old
            result = result[:item.start] + retained + result[item.end:]
    return result


def project_file(project, relative):
    root = Path(project)
    child = Path(relative)
    if not root.is_absolute() or child.is_absolute() or '..' in child.parts:
        raise ValueError('Use an absolute project root and a relative file without traversal')
    if child.suffix.lower() != '.tex':
        raise ValueError('This tool resolves marks in existing .tex files only')
    path = root / child
    for item in (path, *path.parents):
        if item.is_symlink() or getattr(item, 'is_junction', lambda: False)():
            raise ValueError('Refusing linked or junction paths: ' + str(item))
        if item == root:
            break
    root = root.resolve(strict=True)
    resolved = path.resolve(strict=True)
    if not resolved.is_relative_to(root) or resolved == root or not resolved.is_file():
        raise ValueError('Target must be an existing file inside the project')
    return resolved


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['list', 'accept', 'reject'])
    parser.add_argument('--project', required=True)
    parser.add_argument('--file', required=True)
    parser.add_argument('--ids', help='Exact IDs, e.g. 1,3 for manuscript or a,c for response')
    parser.add_argument('--apply', action='store_true', help='Write an already authorized resolution')
    parser.add_argument('--expect-sha256', help='Required with --apply; hash from the reviewed input')
    args = parser.parse_args()
    path = project_file(args.project, args.file)
    original = path.read_bytes()
    input_hash = hashlib.sha256(original).hexdigest()
    text = original.decode('utf-8-sig')
    items = changes(text)
    summary = {
        'file': str(path), 'input_sha256': input_hash, 'action': args.action,
        'changes': [dict(id=item.id, kind=item.kind, line=item.line,
                         new=item.new[:180], old=item.old[:180]) for item in items],
        'applied': False,
    }
    if args.action == 'list':
        if args.apply or args.ids:
            raise ValueError('List is read-only and does not take a selection')
    else:
        if args.ids:
            selected = {item.strip() for item in args.ids.split(',')}
        else:
            raise ValueError('Accept/reject requires exact --ids, e.g. 1,3 or a,c')
        updated = resolve(text, items, selected, args.action)
        bom = codecs.BOM_UTF8 if original.startswith(codecs.BOM_UTF8) else b''
        output = bom + updated.encode('utf-8')
        summary['selected'] = sorted(selected)
        summary['output_sha256'] = hashlib.sha256(output).hexdigest()
        if args.apply:
            if args.expect_sha256 != input_hash:
                raise ValueError('Reviewed content hash does not match; re-read before applying')
            if path.read_bytes() != original:
                raise ValueError('File changed during preflight; nothing written')
            path.write_bytes(output)
            if path.read_bytes() != output:
                raise RuntimeError('Write verification failed')
            summary['applied'] = True
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, OSError, UnicodeError) as error:
        print('ERROR: ' + str(error), file=sys.stderr)
        sys.exit(1)
