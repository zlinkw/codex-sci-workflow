"""Package the dependency-free local editor extension; never clean old artifacts."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile
from xml.sax.saxutils import escape

parser = argparse.ArgumentParser()
parser.add_argument("--output", type=Path, required=True)
parser.add_argument("--source-archive", action="store_true")
args = parser.parse_args()
here = Path(__file__).resolve().parent
source = here if (here / 'package.json').is_file() else here.parent / "assets" / "vscode-local-latex"
backend = source if (source / 'source_review.py').is_file() else here
metadata = json.loads((source / "package.json").read_text(encoding="utf-8"))
runtime = ("package.json", "main.js", "extension.js", "core.js", "backup.js", "navigation.js", "menu_commands.js", "chktex_actions.js", "chktex_messages.js", "inline_review.js", "review_pdf.py", "tools.js", "setup.js", "questions.js", "writing-presets.json", "paper.code-snippets", "README.md", "LICENSE")
args.output.mkdir(parents=True, exist_ok=True)
package = args.output / f"{metadata['publisher']}.{metadata['name']}-{metadata['version']}.vsix"
manifest = f"""<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011">
 <Metadata>
  <Identity Language="en-US" Id="{metadata['name']}" Version="{metadata['version']}" Publisher="{metadata['publisher']}"/>
  <DisplayName>{escape(metadata['displayName'])}</DisplayName>
  <Description xml:space="preserve">{escape(metadata['description'])}</Description>
  <Tags>latex,formatting</Tags><Categories>Formatters</Categories>
  <Properties>
   <Property Id="Microsoft.VisualStudio.Code.Engine" Value="{metadata['engines']['vscode']}"/>
   <Property Id="Microsoft.VisualStudio.Code.ExtensionDependencies" Value="{escape(','.join(metadata.get('extensionDependencies', [])))}"/>
   <Property Id="Microsoft.VisualStudio.Code.ExtensionPack" Value=""/>
   <Property Id="Microsoft.VisualStudio.Code.ExtensionKind" Value="{escape(','.join(metadata.get('extensionKind', ['ui'])))}"/>
  </Properties>
 </Metadata>
 <Installation><InstallationTarget Id="Microsoft.VisualStudio.Code"/></Installation>
 <Dependencies/>
 <Assets><Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true"/></Assets>
</PackageManifest>
"""
content_types = """<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
 <Default Extension="json" ContentType="application/json"/>
 <Default Extension="js" ContentType="application/javascript"/>
 <Default Extension="py" ContentType="text/x-python"/>
 <Default Extension="md" ContentType="text/markdown"/>
 <Default Extension="code-snippets" ContentType="application/json"/>
 <Default Extension="vsixmanifest" ContentType="text/xml"/>
</Types>
"""
import io
buffer = io.BytesIO()
with zipfile.ZipFile(buffer, "w", zipfile.ZIP_DEFLATED) as archive:
    contents = {"extension.vsixmanifest": manifest.encode("utf-8"),
                "[Content_Types].xml": content_types.encode("utf-8")}
    contents.update({f"extension/{name}": (source / name).read_bytes() for name in runtime})
    contents["extension/source_review.py"] = (backend / "source_review.py").read_bytes()
    contents["extension/review_checkpoint.py"] = (backend / "review_checkpoint.py").read_bytes()
    for name, data in contents.items():
        entry = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
        entry.compress_type = zipfile.ZIP_DEFLATED
        archive.writestr(entry, data)
data = buffer.getvalue()
if package.exists():
    if package.read_bytes() != data:
        raise SystemExit("Existing package differs; preserve it and use a new version/output.")
else:
    package.write_bytes(data)
print(package)
print("SHA256", hashlib.sha256(data).hexdigest())
if args.source_archive:
    sources = {name: (source / name).read_bytes() for name in runtime}
    for name in ('source_review.py', 'review_checkpoint.py', 'native_review_test.py', 'source_review_test.py'):
        sources[name] = (backend / name).read_bytes()
    for name in ('inline_review.test.js', 'setup.test.js', 'questions.test.js', 'extension.test.js', 'core.test.js',
                 'backup.test.js', 'menu_commands.test.js', 'navigation.test.js', 'chktex_actions.test.js', 'review_pdf_test.py'):
        sources[name] = (source / name).read_bytes()
    sources['build.py'] = Path(__file__).read_bytes()
    archive_path = args.output / f"{metadata['name']}-{metadata['version']}-source.zip"
    source_buffer = io.BytesIO()
    with zipfile.ZipFile(source_buffer, 'w', zipfile.ZIP_DEFLATED) as archive:
        for name, raw in sources.items():
            entry = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0)); entry.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(entry, raw)
    raw = source_buffer.getvalue()
    if archive_path.exists() and archive_path.read_bytes() != raw:
        raise SystemExit('Existing source archive differs; preserve it and use another output/version.')
    if not archive_path.exists():
        archive_path.write_bytes(raw)
    print(archive_path)
    print('SOURCE_SHA256', hashlib.sha256(raw).hexdigest())
