# Private active-review backup and recovery

Load for requested review backup/restore. Git is optional source-history backup only; ordinary push/clone does not carry uncommitted work or private review objects.

Normal batch checkpoints retain accepted source in Git and compact finished candidate history after successful push. Do not create a full private archive automatically before every compaction. An explicitly requested archive captures the then-current active review state and available objects; it cannot recover candidate generations already retired and physically cleaned. Git alone restores successful source, never abandoned candidate text/annotations. Submission may request a current active-state archive for safety; that is not a promise of indefinite historical retention.

Use scripts/review_archive.py with verified Python and actual owner. New schema-2 backups include current local paper sources/assets, canonical owner, immutable .codex-review/objects and explicitly requested extra files, without calling Git. Exclude Git history/config, build outputs, temporary request attachments, caches and unselected non-paper files. Specify any required nonstandard asset with --extra. Keep the ZIP private locally; upload needs exact destination authorization.

```text
python -X utf8 <skill>/scripts/review_archive.py backup --repo <real-root> --state <relative-owner.tex> --output <absent-path-outside-project.zip> --extra <needed-extra-file>
python -X utf8 <skill>/scripts/review_archive.py restore --archive <archive.zip> --destination <absent-isolated-directory>
```

Backup validates every candidate generation, current source identity and file integrity. Restore validates confined names and checksums before writes and reconciles state/objects afterward. The destination must be absent; never restore over a live paper. Neither action changes author decisions or connects/uploads to a remote. Retain incomplete artifacts on failure. Verify IDs/counters/notes and needed objects in the restored copy before using it.

Legacy schema-1 archives also contain tracked working files, absent paths, staging content and a Git bundle of local refs/history. Their backup/restore still needs verified Git and excludes credentials/remotes/hooks. Convert actual legacy review state before adopting the Git-independent workflow; preserve the old archive/history. Do not claim a normal Git backup alone is a complete review-chain backup.
