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

## Estrutura

```
public/          o site publicado — HTML estático, sem build
  assets/        imagens otimizadas e style.css
build.py         gera as páginas de public/
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

## Deploy

Pronto para a Vercel: importe o repositório e publique. O `vercel.json` já
define `public/` como diretório de saída e dispensa etapa de build.

Funciona igualmente em qualquer hospedagem estática (Netlify, Cloudflare Pages,
cPanel) servindo o conteúdo de `public/`.

## Direitos

© Dr. Thales Pizziolo. Todos os direitos reservados.
Textos, fotografias, ilustrações e marca não são licenciados para reutilização.
