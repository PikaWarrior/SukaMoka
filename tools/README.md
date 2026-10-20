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

GitHub Actions runs the regression tests and smoke checks for source volumes 4 through 10; separate candidate-generation workflows cover volumes 5 through 10. Before publishing another volume, add or update a matching workflow so the exact target volume is covered. A successful extraction is not a substitute for EPUBCheck of the final built EPUB.


## Split extracted volumes into translation chunks

The completed Markdown sources and their extraction reports are stored in `completed_volumes/`. The chunk splitter is `tools/split_volume.py` and uses only the Python standard library.

The published chunks for volumes 4 through 10 are stored in `Cut_Volumes/Volume4/` through `Cut_Volumes/Volume10/`. Each volume folder contains `variant_A/` and `variant_B/`; each variant contains numbered `chunk_*.md` files and an `_index.md`.

Regenerate both variants locally from the repository root:

```powershell
python tools/split_volume.py completed_volumes/volume4.md --mode both --out-dir Cut_Volumes/Volume4
python tools/split_volume.py completed_volumes/volume5.md --mode both --out-dir Cut_Volumes/Volume5
python tools/split_volume.py completed_volumes/volume6.md --mode both --out-dir Cut_Volumes/Volume6
python tools/split_volume.py completed_volumes/volume7.md --mode both --out-dir Cut_Volumes/Volume7
python tools/split_volume.py completed_volumes/volume8.md --mode both --out-dir Cut_Volumes/Volume8
python tools/split_volume.py completed_volumes/volume9.md --mode both --out-dir Cut_Volumes/Volume9
python tools/split_volume.py completed_volumes/volume10.md --mode both --out-dir Cut_Volumes/Volume10
```

The splitter checks that joining the chunks reconstructs the selected source body exactly. By default it removes `## 奥付` only when it is a standalone heading and no later Markdown heading follows; this leaves the epilogue intact and avoids cutting prose that merely mentions the colophon. Use `--keep-colophon` to retain publisher output data. A legacy standalone illustrator-credit line is also recognized when no colophon heading exists.

Each `_index.md` reports both raw Markdown characters and an estimated count after removing ruby annotations (`〔...〕`), editorial annotations (`⟦...⟧`), `EPUB_IMAGE` markers, the literal `[пауза]` marker, and simple `em` tags. This second count is a practical text-size estimate, not a language detector or a count of Japanese characters only.

The v1.2 packing settings (including the +12% soft cap used when merging small chunks) are intentional. The repository workflow `.github/workflows/cut-volumes.yml` regenerates and commits these folders whenever the splitter or any completed source Markdown file for volumes 4–10 changes, and checks that the terminal colophon heading was not published. Treat each `_index.md` as navigation metadata, not as source text.
