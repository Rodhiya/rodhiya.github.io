#!/usr/bin/env python3
"""Compress photos for a Creative Space post.

Usage:
    python3 bin/compress_photos.py <input_folder> <post-name> [--max 2000] [--quality 82]

Example:
    python3 bin/compress_photos.py ~/Pictures/trek trek-2026

Resizes every JPEG, PNG, WebP or TIFF image in <input_folder> so its long side is at most
--max pixels, saves it as JPEG in assets/img/creative/<post-name>/, and strips all
metadata (including GPS location). Prints a `photos:` block to paste into the post.
Originals are never modified. Requires Pillow: pip install Pillow
"""
import argparse
import re
import sys
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("Pillow is not installed. Run: pip install Pillow")

EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff"}
REPO_ROOT = Path(__file__).resolve().parent.parent


def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "photo"


def main():
    parser = argparse.ArgumentParser(description="Compress photos for a Creative Space post.")
    parser.add_argument("input_folder", type=Path)
    parser.add_argument("post_name", help="folder name under assets/img/creative/, e.g. trek-2026")
    parser.add_argument("--max", type=int, default=2000, help="longest side in pixels (default 2000)")
    parser.add_argument("--quality", type=int, default=82, help="JPEG quality 1-95 (default 82)")
    args = parser.parse_args()

    photos = sorted(p for p in args.input_folder.iterdir() if p.suffix.lower() in EXTENSIONS)
    if not photos:
        sys.exit(f"No images found in {args.input_folder}")

    post_name = slugify(args.post_name)
    out_dir = REPO_ROOT / "assets" / "img" / "creative" / post_name
    out_dir.mkdir(parents=True, exist_ok=True)

    written = []
    for src in photos:
        with Image.open(src) as im:
            im = ImageOps.exif_transpose(im)  # apply camera rotation before metadata is dropped
            im.thumbnail((args.max, args.max), Image.LANCZOS)
            if im.mode != "RGB":
                background = Image.new("RGB", im.size, (255, 255, 255))
                background.paste(im, mask=im.getchannel("A") if "A" in im.getbands() else None)
                im = background
            dest = out_dir / f"{slugify(src.stem)}.jpg"
            # Saving without exif=... drops all metadata, including GPS location.
            im.save(dest, "JPEG", quality=args.quality, optimize=True, progressive=True)
        before, after = src.stat().st_size / 1e6, dest.stat().st_size / 1e6
        print(f"{src.name}: {before:.1f} MB -> {after:.2f} MB")
        written.append(dest)

    print(f"\nSaved {len(written)} photo(s) to {out_dir.relative_to(REPO_ROOT)}/")
    print("\nPaste this into the post's front matter:\n")
    print("photos:")
    for dest in written:
        print(f"  - src: {post_name}/{dest.name}")
        print("    caption:")


if __name__ == "__main__":
    main()
