# EPUB source extractor

**Requires Python 3.10 or newer.** The workflow runs under Python 3.12. Run commands from the repository root.

This repository includes a reproducible `lxml`-based extractor for the unpacked Japanese EPUB sources.

## Install

```powershell
python -m pip install -r tools/requirements.txt
```

## Check without writing output

```powershell
python tools/extract_epub.py --volume 5 --dry-run
```

## Generate into a separate test directory

```powershell
python tools/extract_epub.py --volume 5 --output-dir .\tmp\volume5-check
```

## Generate to repository root

```powershell
python tools/extract_epub.py --volume 5
```

The command checks for existing output files before processing and refuses to replace them unless `--overwrite` is provided. `--allow-partial` is for diagnosis only; inspect every warning before using partial output. Report links can be configured with `--github-repo OWNER/REPO` and `--github-ref BRANCH_OR_TAG`.

The script takes the reading order from `standard.opf` spine, uses `lxml` for XML parsing, preserves ruby readings in `base〔reading〕` form, emits unique image markers, checks text and ruby sequences, and writes a detailed omission/resource report. Image contents such as gaiji are not OCRed or visually classified automatically.

GitHub Actions runs the regression tests and smoke checks for source volumes 4 and 5; a separate workflow generates volume 6. Before publishing another volume, add or update a matching workflow so the exact target volume is covered. A successful extraction is not a substitute for EPUBCheck of the final built EPUB.
