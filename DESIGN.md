# DESIGN.md — Sistema visual

## Origem da identidade

A identidade parte dos ativos da marca: o logo (navy profundo + monograma
laranja) e as três ilustrações 3D das articulações. Paleta e tom foram derivados
diretamente deles.

## Cor

Extraída dos assets reais por amostragem de pixel.

| Token | Hex | Uso |
|---|---|---|
| `--navy-900` | `#0B1826` | fundo das seções escuras, texto em cima do laranja |
| `--navy-800` | `#102331` | navy da marca (fundo do logo) |
| `--navy-700` | `#1B3145` | superfícies elevadas no escuro |
| `--navy-600` | `#2A4459` | bordas no escuro |
| `--orange` | `#F18C45` | laranja da marca: botão, destaque grande sobre navy |
| `--orange-600` | `#DE7A33` | hover do botão |
| `--orange-ink` | `#B3520D` | **laranja para texto em fundo claro** |
| `--bone` | `#F7F5F2` | fundo claro, morno (acompanha o laranja) |
| `--bone-200` | `#EAE5DE` | divisores no claro |
| `--ink` | `#14212E` | corpo no claro |
| `--muted` | `#5A6B7C` | secundário no claro |
| `--on-navy` | `#DCE5EC` | corpo no escuro |
| `--on-navy-muted` | `#9FB2C2` | secundário no escuro |

### Duas regras que vieram da medição, não do gosto

1. **Texto branco em cima do laranja reprova** (2,45:1). O botão primário é
   laranja com texto `--navy-900` → **7,31:1, AAA**.
2. **O laranja da marca não serve como cor de texto em fundo claro** (2,45:1 no
   branco). Para texto existe `--orange-ink` `#B3520D`, mesmo matiz (24,8°),
   4,67:1 no bone e 5,09:1 no branco.

Secundário no claro é `#5A6B7C` (5,04:1 no bone), nunca cinza neutro — é navy
dessaturado, puxado do próprio matiz da marca.

## Tipografia

- **Archivo** (400/500/600/700) — display e interface. Larga, confiante,
  editorial-atlética.
- **Spectral** (itálico 500) — exclusivamente na frase de posicionamento. Dá
  à citação uma voz editorial própria, com itálico desenhado de verdade.

Medida de corpo 65–75ch. Tracking de display em -0,025em, nunca abaixo de -0,04em.

## Composição

Hero dividido, e as três articulações como **painéis conduzidos pela ilustração
real** — não cartões de ícone + título + texto. As ilustrações 3D são o ativo
visual mais forte que ele tem e viram a porta de entrada para cada página.

A frase de posicionamento ganha uma seção navy inteira, em serifa grande — é a
ideia central da abordagem dele e merece o maior destaque tipográfico da página.

## Acessibilidade dos botões

- Altura mínima **52px** (56px no mobile), alvo de toque ≥ 48px
- Texto navy sobre laranja, 7,31:1
- Anel de foco visível de 3px com deslocamento, em laranja sobre escuro e navy
  sobre claro — nunca `outline: none`
- **Barra fixa de CTA no mobile**, sempre alcançável com o polegar
- Um CTA primário por viewport; nada de botão secundário competindo
- Links de ícone com `aria-label`; `details/summary` nativo no FAQ (teclado)

## Movimento

Um momento autorado: entrada escalonada do hero, a partir de um estado já
visível, com ease-out exponencial. Painéis revelam uma vez na rolagem.
`prefers-reduced-motion` desliga tudo.

## Superfícies do navegador

Seleção, caret, barra de rolagem, anel de foco e `text-underline-offset` são
tematizados a partir da paleta.
