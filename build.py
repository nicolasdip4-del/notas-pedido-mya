"""Arma notas-pedido-mya.html (un solo archivo) desde src/notas.html, embebiendo logo, fuentes Gotham y html2canvas (imagen PNG A4)."""
import base64
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(AQUI, 'src')


def b64(nombre):
    with open(os.path.join(SRC, nombre), 'rb') as f:
        return base64.b64encode(f.read()).decode('ascii')


with open(os.path.join(SRC, 'notas.html'), encoding='utf-8') as f:
    html = f.read()

html = (html.replace('{{LOGO}}', b64('logo-mya.svg'))
            .replace('{{FONT_REG}}', b64('GOTHAMPRO.TTF'))
            .replace('{{FONT_BOLD}}', b64('GOTHAMPRO-BOLD.OTF'))
            .replace('{{HTML2CANVAS}}', open(os.path.join(SRC, 'vendor', 'html2canvas.min.js'), encoding='utf-8').read()))

salida = os.path.join(AQUI, 'notas-pedido-mya.html')
with open(salida, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'{salida} ({len(html) // 1024} KB)')
