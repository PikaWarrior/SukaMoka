# EPUB source extractor

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

The command refuses to replace existing output files unless `--overwrite` is provided. `--allow-partial` is for diagnosis only; inspect every warning before using partial output.

The script takes the reading order from `standard.opf` spine, uses `lxml` for XML parsing, preserves ruby readings in `base〔reading〕` form, emits unique image markers, checks text and ruby sequences, and writes a detailed omission/resource report. Image contents such as gaiji are not OCRed or visually classified automatically.

GitHub Actions runs the tests and smoke checks for source volumes 4 and 5. A successful XML extraction does not replace visual image review or EPUBCheck of the final built EPUB.
