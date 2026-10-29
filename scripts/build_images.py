"""Generate the web-ready images in src/assets from the full-size originals in art/.

Run with:  npm run images   (requires Python 3 and Pillow: pip install Pillow)

Outputs are committed, so this only needs to run again when the art changes.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
ART = ROOT / "art"
OUT = ROOT / "src" / "assets"

CREAM = (251, 250, 246, 255)
INK = (16, 36, 59, 255)
INK_SOFT = (61, 88, 104, 255)
TEAL = (37, 99, 111, 255)
MINT = (220, 243, 242, 255)

# Noto Sans is openly licensed (SIL OFL), so it is safe to bake into a published image.
FONT_DIRS = [Path("C:/Windows/Fonts"), Path("/usr/share/fonts/truetype/noto"), Path("/Library/Fonts")]


def font(name, size):
    for folder in FONT_DIRS:
        path = folder / name
        if path.exists():
            return ImageFont.truetype(str(path), size)
    raise SystemExit(f"Font {name} not found. Install Noto Sans and try again.")


def square(image, padding=0.0, background=(0, 0, 0, 0)):
    """Centre the image on a square canvas, optionally with padding around it."""
    side = round(max(image.size) * (1 + padding * 2))
    canvas = Image.new("RGBA", (side, side), background)
    canvas.alpha_composite(image, ((side - image.width) // 2, (side - image.height) // 2))
    return canvas


def resized(image, size):
    return image.resize((size, size), Image.LANCZOS)


def save_png(image, name):
    """Save as an optimized PNG; a 256-colour palette is visually identical for this flat art."""
    path = OUT / name
    image = image.quantize(256, method=Image.FASTOCTREE, dither=Image.FLOYDSTEINBERG)
    image.save(path, optimize=True)
    print(f"{name:28} {path.stat().st_size / 1024:7.1f} KB")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    icon = square(Image.open(ART / "icon.png").convert("RGBA"))
    mascot = Image.open(ART / "mascot.png").convert("RGBA")

    # Header logo: shown at 37px, so 80px covers 2x screens.
    save_png(resized(icon, 80), "logo.png")

    # Browser tab icons.
    favicon = resized(icon, 48)
    favicon.save(OUT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    print(f"{'favicon.ico':28} {(OUT / 'favicon.ico').stat().st_size / 1024:7.1f} KB")
    save_png(resized(icon, 32), "favicon-32.png")

    # iOS fills transparency with black, so the touch icon gets a solid background.
    save_png(resized(square(icon, 0.12, CREAM), 180), "apple-touch-icon.png")

    # Web app manifest icons.
    save_png(resized(square(icon, 0.12, CREAM), 192), "icon-192.png")
    save_png(resized(square(icon, 0.12, CREAM), 512), "icon-512.png")

    # Hero mascot: a palette PNG comes out smaller than WebP for this flat illustration.
    save_png(mascot, "mascot.png")

    # Social preview card (1200x630) for link previews on messaging and social apps.
    card = Image.new("RGBA", (1200, 630), CREAM)
    draw = ImageDraw.Draw(card)
    draw.ellipse((700, 45, 1240, 585), fill=MINT)
    art = mascot.resize((470, 470), Image.LANCZOS)
    card.alpha_composite(art, (705, 80))
    draw.text((80, 150), "COMING SOON TO ANDROID", font=font("NotoSans-Bold.ttf", 26), fill=TEAL)
    draw.text((76, 196), "Receipts,", font=font("NotoSans-Bold.ttf", 96), fill=INK)
    draw.text((76, 300), "Please.", font=font("NotoSans-Bold.ttf", 96), fill=INK)
    draw.text((80, 440), "A smarter home for your receipts.", font=font("NotoSans-Regular.ttf", 36), fill=INK_SOFT)
    save_png(card, "og-image.png")


if __name__ == "__main__":
    main()
