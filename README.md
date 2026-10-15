# Dr. Thales Pizziolo — Site

Site do Dr. Thales Pizziolo, ortopedista com atuação em trauma esportivo e
artroscopia, dedicado a ombro, cotovelo e joelho, na Vila Mariana, São Paulo.

CRM-SP 213316 · RQE 125841

## Páginas

| URL | Conteúdo |
|---|---|
| `/` | Home |
| `/ombro/` | Avaliação de ombro |
| `/cotovelo/` | Avaliação de cotovelo |
| `/joelho/` | Avaliação de joelho |
| `/privacidade/` | Política de privacidade (LGPD) e cookies |
| `404.html` | Página de erro |
| `llms.txt` | Resumo do consultório para assistentes de I.A. |

## Estrutura

```
public/          o site publicado — HTML estático, sem build
  assets/        imagens WebP, fontes woff2 (assets/fonts) e style.css
build.py         gera as páginas, sitemap, robots, llms.txt e 404
gerar_imagens.py gera WebP, ícones e imagens de compartilhamento (Pillow)
DESIGN.md        paleta, tipografia e regras de contraste
vercel.json      configuração de deploy
```

## Editar

As quatro páginas compartilham cabeçalho, rodapé e componentes, e são geradas
por `build.py`. Edite o conteúdo lá — não nos HTML — e rode:

```bash
python3 build.py
```

Requer só Python 3, sem dependências.

Trocou uma foto ou o logo? Rode antes `python3 gerar_imagens.py` (precisa de
Pillow). Ele gera as versões WebP de 480 e 800 px, o favicon e as imagens de
compartilhamento 1200x630.

## Cookies e consentimento

O `<head>` de cada página define o Consent Mode do Google antes do GTM:
medição ligada até a pessoa recusar, anúncio personalizado sempre desligado
(site de saúde). O Microsoft Clarity só dispara no GTM com o evento
`consent_accept`, enviado quando a pessoa clica em "Aceitar". A escolha fica
em `localStorage` (`tp_consent`).

## Deploy

Pronto para a Vercel: importe o repositório e publique. O `vercel.json` já
define `public/` como diretório de saída e dispensa etapa de build.

Funciona igualmente em qualquer hospedagem estática (Netlify, Cloudflare Pages,
cPanel) servindo o conteúdo de `public/`.

## Direitos

© Dr. Thales Pizziolo. Todos os direitos reservados.
Textos, fotografias, ilustrações e marca não são licenciados para reutilização.
