"""Authoring only: compile LaTeX and rasterize its equations with Poppler.

Requires a TeX distribution, pdftoppm, pdfplumber and pypdf.
The Python learning examples do not need these authoring dependencies.
"""
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import pdfplumber
from pypdf import PdfReader, PdfWriter


def main():
    root = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build-dir', type=Path, default=root.parents[1]/'runs'/'s02-tex')
    parser.add_argument('--skip-compile', action='store_true')
    args = parser.parse_args()
    build = args.build_dir.resolve()
    build.mkdir(parents=True, exist_ok=True)
    if not args.skip_compile:
        subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                        f'-output-directory={build}', str(root/'formulas.tex')], check=True)
    mapping = json.loads((root/'equation-map.json').read_text(encoding='utf-8'))
    reader = PdfReader(build/'formulas.pdf')
    writer = PdfWriter()
    with pdfplumber.open(build/'formulas.pdf') as pdf:
        assert len(pdf.pages) == len(mapping), 'Unexpected formula page count'
        for i, page in enumerate(pdf.pages):
            assert page.chars, f'Empty formula page {i+1}'
            top = max(0, min(c['top'] for c in page.chars)-12)
            bottom = min(page.height, max(c['bottom'] for c in page.chars)+12)
            # Crop only the vertical whitespace, preserving a consistent type scale.
            reader.pages[i].cropbox.lower_left = (0, page.height-bottom)
            reader.pages[i].cropbox.upper_right = (page.width, page.height-top)
            writer.add_page(reader.pages[i])
    with (build/'cropped.pdf').open('wb') as handle:
        writer.write(handle)
    subprocess.run(['pdftoppm', '-cropbox', '-r', '180', '-png',
                    str(build/'cropped.pdf'), str(build/'equation')], check=True)
    for row in mapping:
        candidates = [build/f"equation-{row['page']:02d}.png",
                      build/f"equation-{row['page']}.png"]
        source = next(path for path in candidates if path.exists())
        shutil.copyfile(source, root/'assets'/f"formula-{row.get('asset', row['slide']):02d}.png")
    print(f'Rendered {len(mapping)} LaTeX equations.')


if __name__ == '__main__':
    main()
