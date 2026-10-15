#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera as imagens otimizadas do site a partir das fotos em public/assets/*.jpg
e das ilustrações e do logo em _originais/.

Rode só quando trocar uma foto ou o logo:   python3 gerar_imagens.py
Requer Pillow com suporte a WebP (pip install pillow). O build.py continua
sem dependências: ele só referencia os arquivos que este script gera.

Saída:
  public/assets/<foto>-480.webp e -800.webp   versões para srcset
  public/assets/logo-96.webp                  logo do cabeçalho e do rodapé
  public/assets/og-<página>.jpg               imagem de compartilhamento 1200x630
  public/favicon.ico, public/apple-touch-icon.png, public/assets/icon-192.png
"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(ROOT, "public", "assets")
PUBLIC = os.path.join(ROOT, "public")
ORIG = os.path.join(ROOT, "_originais")

FOTOS = ["hero", "sobre", "retrato-casual"]
ILUSTRACOES = ["joint-shoulder", "joint-elbow", "joint-knee"]   # fonte: _originais/<nome>.png
LARGURAS_ILUSTRACAO = [320, 640]
LARGURAS = [480, 800]

NAVY_900 = (11, 24, 38)
NAVY_800 = (16, 35, 49)
ORANGE = (241, 140, 69)
ON_NAVY = (220, 229, 236)
ON_NAVY_MUTED = (159, 178, 194)

AVENIR = "/System/Library/Fonts/Avenir Next.ttc"
BOLD, DEMI, MEDIUM, REGULAR = 0, 2, 5, 7

# texto da segunda linha da imagem de compartilhamento, por página
OG = {
    "home": "Ombro, cotovelo e joelho",
    "ombro": "Avaliação de ombro",
    "cotovelo": "Avaliação de cotovelo",
    "joelho": "Avaliação de joelho",
}


def fotos():
    for nome in FOTOS:
        im = Image.open(os.path.join(ASSETS, nome + ".jpg")).convert("RGB")
        for w in LARGURAS:
            h = round(im.height * w / im.width)
            out = os.path.join(ASSETS, "%s-%d.webp" % (nome, w))
            im.resize((w, h), Image.LANCZOS).save(out, "WEBP", quality=82, method=6)
            print("  %s (%d KB)" % (os.path.relpath(out, ROOT), os.path.getsize(out) // 1024))


def ilustracoes():
    for nome in ILUSTRACOES:
        im = Image.open(os.path.join(ORIG, nome + ".png")).convert("RGB")
        for w in LARGURAS_ILUSTRACAO:
            out = os.path.join(ASSETS, "%s-%d.webp" % (nome, w))
            im.resize((w, w), Image.LANCZOS).save(out, "WEBP", quality=80, method=6)
            print("  %s (%d KB)" % (os.path.relpath(out, ROOT), os.path.getsize(out) // 1024))


def monograma(lado):
    """Só o monograma TP do logo, centralizado num quadrado navy."""
    logo = Image.open(os.path.join(ORIG, "logo.jpg")).convert("RGB")
    m = logo.crop((575, 465, 905, 850))
    s = int(m.height * 1.28)
    c = Image.new("RGB", (s, s), NAVY_800)
    c.paste(m, ((s - m.width) // 2, (s - m.height) // 2))
    return c.resize((lado, lado), Image.LANCZOS)


def icones():
    monograma(256).save(os.path.join(PUBLIC, "favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])
    monograma(180).save(os.path.join(PUBLIC, "apple-touch-icon.png"), optimize=True)
    monograma(192).save(os.path.join(ASSETS, "icon-192.png"), optimize=True)
    marca = Image.open(os.path.join(ASSETS, "logo-marca.png")).convert("RGBA")
    marca.resize((96, round(96 * marca.height / marca.width)), Image.LANCZOS).save(
        os.path.join(ASSETS, "logo-96.webp"), "WEBP", quality=90, method=6)
    print("  public/favicon.ico, apple-touch-icon.png, assets/icon-192.png, assets/logo-96.webp")


def og():
    foto = Image.open(os.path.join(ASSETS, "hero.jpg")).convert("RGB")
    # recorte do rosto e ombros, 470 x 630
    fw, fh = 470, 630
    escala = fw / (foto.width * 0.86)
    f = foto.resize((round(foto.width * escala), round(foto.height * escala)), Image.LANCZOS)
    x0 = (f.width - fw) // 2
    y0 = round(f.height * 0.06)
    f = f.crop((x0, y0, x0 + fw, y0 + fh))

    for pagina, linha2 in OG.items():
        c = Image.new("RGB", (1200, 630), NAVY_900)
        c.paste(f, (1200 - fw, 0))
        # degradê curto para a foto não terminar num corte seco
        grad = Image.new("L", (90, 630))
        for x in range(90):
            ImageDraw.Draw(grad).line([(x, 0), (x, 630)], fill=round(255 * (1 - x / 89)))
        c.paste(Image.new("RGB", (90, 630), NAVY_900), (1200 - fw, 0), grad)

        d = ImageDraw.Draw(c)
        x = 76
        d.rectangle([x, 190, x + 6, 400], fill=ORANGE)
        tx = x + 34
        d.text((tx, 182), "Dr. Thales Pizziolo", font=ImageFont.truetype(AVENIR, 66, index=BOLD), fill=(255, 255, 255))
        d.text((tx, 272), "Ortopedista", font=ImageFont.truetype(AVENIR, 38, index=DEMI), fill=ORANGE)
        d.text((tx, 322), linha2, font=ImageFont.truetype(AVENIR, 38, index=MEDIUM), fill=ON_NAVY)
        d.text((tx, 372), "Vila Mariana · São Paulo", font=ImageFont.truetype(AVENIR, 28, index=REGULAR), fill=ON_NAVY_MUTED)
        d.text((tx, 520), "CRM-SP 213316  ·  RQE 125841", font=ImageFont.truetype(AVENIR, 24, index=MEDIUM), fill=ON_NAVY_MUTED)
        out = os.path.join(ASSETS, "og-%s.jpg" % pagina)
        c.save(out, "JPEG", quality=84, optimize=True, progressive=True)
        print("  %s (%d KB)" % (os.path.relpath(out, ROOT), os.path.getsize(out) // 1024))


if __name__ == "__main__":
    fotos()
    ilustracoes()
    icones()
    og()
