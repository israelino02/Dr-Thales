#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador do site do Dr. Thales Pizziolo.

Edite o conteúdo aqui e rode:   python3 build.py
Saída em public/ - é essa pasta que sobe para o servidor.

Cabeçalho, rodapé, barra fixa e ícones ficam num lugar só, para as quatro
páginas nunca divergirem entre si.
"""
import os
from urllib.parse import quote

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "public")
SITE = "https://www.drthalespizziolo.com.br"
WA = "5511912141608"
GTM = "GTM-WDB6CZFL"


def wa(texto):
    """Link de WhatsApp com mensagem pré-preenchida. A mensagem identifica a
    origem para a secretária - é o rastreamento que sobrevive a bloqueador,
    iOS e consentimento de cookie."""
    return "https://wa.me/%s?text=%s" % (WA, quote(texto, safe=""))


# ---------------------------------------------------------------- ícones ----
SPRITE = """<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <symbol id="i-wa" viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.46 1.32 4.96L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21 5.46 0 9.91-4.45 9.91-9.91S17.5 2 12.04 2m0 1.67c4.55 0 8.24 3.7 8.24 8.24s-3.69 8.25-8.24 8.25c-1.5 0-2.96-.4-4.24-1.16l-.3-.18-3.12.82.83-3.04-.19-.32a8.19 8.19 0 0 1-1.25-4.37c0-4.54 3.7-8.24 8.27-8.24m-3.7 4.1c-.18 0-.46.07-.7.33-.25.25-.94.92-.94 2.23 0 1.32.96 2.59 1.09 2.77.14.18 1.87 2.98 4.6 4.06 2.27.9 2.73.72 3.22.67.5-.04 1.6-.65 1.82-1.29.23-.63.23-1.18.16-1.29-.07-.11-.25-.18-.53-.32-.27-.14-1.6-.79-1.85-.88-.25-.09-.43-.14-.61.14-.18.27-.7.89-.86 1.07-.16.18-.32.2-.59.07-.27-.14-1.17-.43-2.23-1.38-.82-.73-1.38-1.63-1.54-1.9-.16-.28-.02-.43.11-.57.12-.13.32-.34.48-.52.16-.18.21-.3.32-.48.11-.18.05-.34-.02-.48-.07-.14-.6-1.47-.83-2-.18-.43-.37-.44-.53-.45h-.36Z"/></symbol>
  <symbol id="i-star" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2.3l2.9 5.9 6.5.95-4.7 4.6 1.1 6.5-5.8-3.05-5.8 3.05 1.1-6.5-4.7-4.6 6.5-.95L12 2.3Z"/></symbol>
  <symbol id="i-arrow" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" d="M5 12h14M13 6l6 6-6 6"/></symbol>
  <symbol id="i-pin" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></g></symbol>
  <symbol id="i-check" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9.2"/><path d="m8.2 12.3 2.6 2.6 5-5.4"/></g></symbol>
</svg>"""


def ic(nome):
    return '<svg aria-hidden="true" focusable="false"><use href="#i-%s"/></svg>' % nome


# ------------------------------------------------------------- conteúdo -----
JOINTS = [
    {
        "slug": "ombro", "nome": "Ombro", "img": "joint-shoulder.jpg",
        "resumo": "Bursite, tendinite, lesões do manguito rotador, luxações, instabilidade e traumas ligados ao esporte.",
        "title": "Tratamento de Bursite e Tendinite no Ombro na Vila Mariana | Dr. Thales Pizziolo",
        "desc": "Ortopedista de ombro na Vila Mariana, São Paulo. Avaliação de bursite, tendinite, manguito rotador e instabilidade. Tratamento conservador avaliado primeiro. CRM-SP 213316 / RQE 125841.",
        "h1": "Bursite, tendinite ou dor no ombro?",
        "h1seo": "Ortopedista de ombro em Vila Mariana, São Paulo",
        "lede": "O ombro é a articulação de maior amplitude do corpo - e por isso uma das que mais sofrem com esporte, sobrecarga e movimentos repetidos. A avaliação começa entendendo a origem da sua dor antes de qualquer decisão de tratamento.",
        "wa": "Olá! Vim pela página de ombro do site e gostaria de agendar uma avaliação.",
        "conds_h2": "O que é avaliado no ombro",
        "conds": [
            ("Bursite no ombro", "Inflamação da bolsa que reduz o atrito entre tendão e osso. Dor ao elevar o braço é comum."),
            ("Tendinite do manguito rotador", "Inflamação dos tendões que estabilizam o ombro, frequente em quem treina com carga."),
            ("Lesão do manguito rotador", "Desgaste ou ruptura parcial ou completa desses tendões, por trauma ou sobrecarga."),
            ("Tendinite calcária", "Depósito de cálcio dentro do tendão, que pode causar dor intensa e súbita."),
            ("Luxação e instabilidade", "Sensação de que o ombro sai do lugar, geralmente após trauma esportivo."),
            ("Dor por sobrecarga", "Dores ligadas a gestos repetidos no esporte ou no trabalho."),
        ],
        "faq": [
            ("Bursite no ombro precisa de cirurgia?", "Na maioria dos casos, não. A bursite costuma ser tratada de forma conservadora. A indicação de qualquer procedimento depende do diagnóstico e da avaliação individual."),
            ("Tendinite no ombro e bursite são a mesma coisa?", "Não. A tendinite afeta o tendão; a bursite afeta a bolsa que protege a articulação. Elas podem aparecer juntas, e a consulta serve justamente para diferenciar."),
            ("Posso continuar treinando com dor no ombro?", "Depende da lesão. Em muitos casos é possível adaptar o treino durante a recuperação, com orientação individualizada."),
            ("Quando a infiltração no ombro é indicada?", "Apenas em condições específicas e após avaliação. Infiltração não é indicada para qualquer dor."),
            ("O atendimento é por convênio?", "O atendimento é particular, sem convênio, com emissão de nota fiscal para você solicitar reembolso ao seu plano de saúde."),
        ],
    },
    {
        "slug": "cotovelo", "nome": "Cotovelo", "img": "joint-elbow.jpg",
        "resumo": "Bursite, epicondilite, cotovelo de tenista, dores por sobrecarga e lesões que limitam a função.",
        "title": "Tratamento de Bursite e Epicondilite no Cotovelo na Vila Mariana | Dr. Thales Pizziolo",
        "desc": "Ortopedista de cotovelo na Vila Mariana, São Paulo. Avaliação de bursite, epicondilite, cotovelo de tenista e dor por sobrecarga. CRM-SP 213316 / RQE 125841.",
        "h1": "Bursite, epicondilite ou dor no cotovelo?",
        "h1seo": "Ortopedista de cotovelo em Vila Mariana, São Paulo",
        "lede": "Dor no cotovelo costuma aparecer aos poucos - no treino, na raquete, no teclado - até atrapalhar gestos simples como segurar um copo. A avaliação identifica a origem da sobrecarga para tratar a causa, não só o sintoma.",
        "wa": "Olá! Vim pela página de cotovelo do site e gostaria de agendar uma avaliação.",
        "conds_h2": "O que é avaliado no cotovelo",
        "conds": [
            ("Bursite do olécrano", "Inflamação da bolsa na ponta do cotovelo. Inchaço visível é o sinal mais comum."),
            ("Epicondilite lateral", "Conhecida como cotovelo de tenista: dor na parte externa, ao segurar ou girar objetos."),
            ("Tendinite no cotovelo", "Inflamação dos tendões por gesto repetido, no esporte ou no trabalho."),
            ("Dor por sobrecarga", "Dores que surgem com o volume de treino ou de atividade repetitiva."),
            ("Lesões traumáticas", "Lesões decorrentes de queda ou impacto, que limitam o movimento."),
            ("Perda de função", "Dificuldade para estender, dobrar ou fazer força com o braço."),
        ],
        "faq": [
            ("Cotovelo de tenista só acontece em quem joga tênis?", "Não. O nome vem do esporte, mas a epicondilite lateral aparece com frequência em quem faz movimentos repetidos de punho e antebraço, inclusive fora do esporte."),
            ("Bursite no cotovelo precisa ser drenada?", "Nem sempre. A conduta depende da causa, do tamanho e de haver ou não sinais de infecção - o que só a avaliação define."),
            ("Epicondilite tem tratamento sem cirurgia?", "Na grande maioria dos casos o tratamento é conservador. A cirurgia fica reservada a situações específicas, após avaliação individual."),
            ("Preciso parar de treinar?", "Nem sempre. Muitas vezes é possível adaptar a carga e o gesto durante a recuperação, com orientação."),
            ("O atendimento é por convênio?", "O atendimento é particular, sem convênio, com emissão de nota fiscal para você solicitar reembolso ao seu plano de saúde."),
        ],
    },
    {
        "slug": "joelho", "nome": "Joelho", "img": "joint-knee.jpg",
        "resumo": "Tendinite patelar, bursite, lesões ligamentares e de menisco, desgaste articular e lesões esportivas.",
        "title": "Tratamento de Tendinite e Dor no Joelho na Vila Mariana | Dr. Thales Pizziolo",
        "desc": "Ortopedista de joelho na Vila Mariana, São Paulo. Avaliação de tendinite patelar, bursite, lesões ligamentares e de menisco. Tratamento conservador avaliado primeiro. CRM-SP 213316 / RQE 125841.",
        "h1": "Tendinite, lesão ou dor no joelho?",
        "h1seo": "Ortopedista de joelho em Vila Mariana, São Paulo",
        "lede": "O joelho sustenta o corpo em cada passada, salto e mudança de direção. Por isso as lesões aparecem tanto em quem corre quanto em quem joga, treina ou simplesmente quer subir escada sem dor. A avaliação considera sua modalidade e seus objetivos.",
        "wa": "Olá! Vim pela página de joelho do site e gostaria de agendar uma avaliação.",
        "conds_h2": "O que é avaliado no joelho",
        "conds": [
            ("Tendinite patelar", "Conhecida como joelho de saltador: dor abaixo da patela, comum em corrida e esportes de salto."),
            ("Bursite no joelho", "Inflamação das bolsas ao redor da articulação, com dor e inchaço localizados."),
            ("Lesões ligamentares", "Entorses e lesões de ligamentos como o cruzado anterior, geralmente em mudança brusca de direção."),
            ("Lesão de menisco", "Lesão da cartilagem que amortece o joelho. Travamento e dor ao agachar são sinais frequentes."),
            ("Desgaste articular", "Alterações da cartilagem que causam dor e rigidez, com impacto na rotina."),
            ("Lesões esportivas", "Traumas e sobrecargas ligados à corrida, ao futebol, à musculação e a outras modalidades."),
        ],
        "faq": [
            ("Toda lesão de ligamento no joelho precisa de cirurgia?", "Não. A decisão considera o tipo de lesão, o grau, a estabilidade do joelho e a demanda esportiva de cada paciente."),
            ("Lesão de menisco sempre é cirúrgica?", "Não. Muitas lesões de menisco são tratadas de forma conservadora. A indicação depende do padrão da lesão e dos sintomas."),
            ("Posso continuar correndo com dor no joelho?", "Depende da causa. Em muitos casos é possível adaptar o volume e a intensidade durante a recuperação, com orientação."),
            ("Quando a artroscopia de joelho é indicada?", "Quando há indicação adequada após avaliação. É uma técnica minimamente invasiva, mas continua sendo uma cirurgia - e só é considerada quando necessária."),
            ("O atendimento é por convênio?", "O atendimento é particular, sem convênio, com emissão de nota fiscal para você solicitar reembolso ao seu plano de saúde."),
        ],
    },
]

SINAIS = [
    "Dor persistente que não melhora com repouso",
    "Lesão durante atividade física ou trauma",
    "Dificuldade ou perda de movimento",
    "Estalos, travamentos ou instabilidade",
    "Limitação para o dia a dia ou para o esporte",
]

TRATAMENTOS = [
    ("Tratamento conservador", "Medicação, reabilitação e adaptação das atividades conforme cada diagnóstico."),
    ("Infiltrações", "Procedimentos selecionados para condições específicas, sempre após avaliação individual."),
    ("Procedimentos guiados", "Precisão com auxílio de imagem para intervenções minimamente invasivas."),
    ("Artroscopia", "Técnica cirúrgica minimamente invasiva quando há indicação adequada."),
    ("Cirurgia ortopédica", "Planejamento cuidadoso, alinhado ao diagnóstico e aos objetivos do paciente."),
    ("Retorno ao esporte", "Estratégia progressiva considerando força, função, segurança e modalidade."),
]

CREDS = [
    ("UFMA", "Graduação em Medicina"),
    ("INTO · Rio de Janeiro", "Residência em Ortopedia e Traumatologia"),
    ("Instituto VITA · SP", "Artroscopia e Trauma Esportivo"),
    ("SBOT", "Membro titular da Sociedade Brasileira de Ortopedia e Traumatologia"),
    ("CRM-SP 213316", "RQE 125841"),
]

FAQ_HOME = [
    ("Toda lesão esportiva precisa de cirurgia?", "Não. Muitas lesões podem ser tratadas de forma conservadora. A decisão considera o diagnóstico, a gravidade, as características e os objetivos de cada paciente."),
    ("Vou precisar parar completamente de treinar?", "Nem sempre. Dependendo da lesão, pode ser possível adaptar o treinamento durante a recuperação, com orientação individualizada."),
    ("Quando devo procurar um ortopedista?", "Dor persistente, perda de movimento, inchaço, instabilidade, redução de desempenho ou trauma merecem avaliação."),
    ("Como funciona o retorno ao esporte?", "O retorno é progressivo e considera a recuperação da lesão, a função, a força, a segurança e as demandas da sua modalidade."),
    ("Infiltração é indicada para qualquer dor?", "Não. Há diferentes procedimentos, e a indicação depende do diagnóstico e da avaliação individual."),
    ("O atendimento é por convênio?", "O atendimento é particular, sem convênio. É possível emitir nota fiscal para que você solicite reembolso ao seu plano de saúde, conforme as regras do seu contrato."),
    ("Atende a partir de qual idade?", "A partir de 14 anos, para atletas e para qualquer pessoa que queira se manter ativa."),
]


# ------------------------------------------------------------- partes -------
def head(p, title, desc, canon, og_img):
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="geo.region" content="BR-SP">
<meta name="geo.placename" content="Vila Mariana, São Paulo">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Dr. Thales Pizziolo">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{p}assets/logo-marca.png">
<link rel="apple-touch-icon" href="{p}assets/logo-marca.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Spectral:ital,wght@1,400;1,500;1,600&display=swap">
<link rel="stylesheet" href="{p}assets/style.css">
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});
var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;
j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})
(window,document,'script','dataLayer','{GTM}');</script>
"""


def schema_physician():
    return """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Physician","name":"Dr. Thales Pizziolo",
"medicalSpecialty":["Orthopedic","SportsMedicine"],
"description":"Ortopedista e traumatologista com atuação em trauma esportivo e artroscopia. Atendimento dedicado a ombro, cotovelo e joelho.",
"url":"%s/","image":"%s/assets/hero.jpg","telephone":"+5511912141608","email":"thpizziolo@gmail.com",
"isAcceptingNewPatients":true,
"address":{"@type":"PostalAddress","streetAddress":"Rua Domingos de Morais, 2781, 12º andar, Edifício Artwork","addressLocality":"São Paulo","addressRegion":"SP","addressCountry":"BR"},
"areaServed":{"@type":"City","name":"São Paulo"},
"sameAs":["https://www.doctoralia.com.br/thales-pizziolo/ortopedista-traumatologista/sao-paulo","https://www.instagram.com/drthalespizziolo"]}
</script>""" % (SITE, SITE)


def schema_faq(itens):
    import json
    return '<script type="application/ld+json">%s</script>' % json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in itens]
    }, ensure_ascii=False)


def schema_breadcrumb(nome, slug):
    import json
    return '<script type="application/ld+json">%s</script>' % json.dumps({
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Início", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": nome, "item": "%s/%s/" % (SITE, slug)},
        ]}, ensure_ascii=False)


def header(p, atual=None):
    def nav(slug, nome):
        cur = ' aria-current="page"' if atual == slug else ""
        return '<a href="%s%s/"%s>%s</a>' % (p, slug, cur, nome)
    home = p or "./"
    return f"""</head>
<body>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
{SPRITE}
<a class="skip" href="#main">Ir para o conteúdo</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{home}">
      <img src="{p}assets/logo-marca.png" alt="" width="38" height="38">
      <span class="visually-hidden">Dr. Thales Pizziolo - página inicial</span>
      <span class="brand-text" aria-hidden="true"><b class="brand-name">Dr. Thales Pizziolo</b><span class="brand-sub">Ortopedista · CRM-SP 213316</span></span>
    </a>
    <nav class="nav" aria-label="Principal">
      {nav("ombro","Ombro")}
      {nav("cotovelo","Cotovelo")}
      {nav("joelho","Joelho")}
      <a href="{home}#sobre">Sobre</a>
      <a href="{home}#consultorio">Consultório</a>
    </nav>
    <a class="btn btn-1 header-cta" href="{wa("Olá! Vim pelo site (topo) e gostaria de agendar uma consulta.")}">{ic("wa")}Agendar</a>
  </div>
</header>
<main id="main">
"""


def trust():
    return f"""<div class="trust">
        <a class="trust-item" href="https://www.google.com/search?q=Dr.+Thales+Pizziolo+ortopedista" target="_blank" rel="noopener">{ic("star")}<span><b>4,8</b> no Google · 12 avaliações</span></a>
        <a class="trust-item" href="https://www.doctoralia.com.br/thales-pizziolo/ortopedista-traumatologista/sao-paulo" target="_blank" rel="noopener">{ic("star")}<span><b>5,0</b> no Doctoralia · 13 avaliações</span></a>
        <span class="trust-cred">CRM-SP 213316 · RQE 125841</span>
      </div>"""


def stance():
    return """<section class="stance on-dark">
  <div class="wrap">
    <figure style="margin:0; padding: 3rem 1rem;">
      <blockquote style="margin:0; font-family: 'Spectral', serif; font-size: clamp(2rem, 4vw, 3rem); font-style: italic; line-height: 1.25; text-align: center; font-weight: 500; color: var(--orange);"><q>A melhor qualidade do cirurgião é saber <em style="font-weight: 600; color: #fff;">não</em> indicar uma cirurgia.</q></blockquote>
      <figcaption style="text-align: center; margin-top: 1.5rem; font-size: 1rem; color: var(--on-navy-muted); letter-spacing: 0.05em;">Dr. Thales Pizziolo · CRM-SP 213316 · RQE 125841</figcaption>
    </figure>
  </div>
</section>"""


def treatments(titulo):
    li = "\n".join('      <li class="treat-card" style="background: var(--bone-100); padding: 2rem 1.5rem; border: 1px solid var(--bone-200); border-radius: var(--r); transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;"><h3 style="font-size: 1.2rem; margin-bottom: 0.8rem; color: var(--navy-800);">%s</h3><p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6;">%s</p></li>' % t for t in TRATAMENTOS)
    return f"""<section id="tratamentos">
  <div class="wrap">
    <h2>{titulo}</h2>
    <ul class="treat" style="gap: 1.5rem; background: transparent; padding: 0; margin-top: 3rem;">
{li}
    </ul>
    <p class="note" style="color:var(--muted); text-align: center; margin-inline: auto;">A indicação de qualquer tratamento depende de consulta médica e avaliação individual.</p>
  </div>
</section>"""


def about(p, compacto=False):
    li = "\n".join('        <li><b>%s</b><span>%s</span></li>' % c for c in CREDS)
    extra = "" if compacto else """
        <p style="margin-top:1.1rem;color:var(--text-dark);">Construo uma estratégia individualizada, priorizando tratamentos não cirúrgicos e minimamente invasivos quando indicados - sem perder de vista a atividade que faz parte da sua vida. Corredor de rua e praticante de musculação, conheço de perto o valor que o esporte tem na rotina de cada pessoa.</p>"""
    return f"""<section id="sobre" style="background:#fff">
  <div class="wrap split">
    <figure class="split-figure" style="margin:0">
      <img src="{p}assets/sobre.jpg" alt="Dr. Thales Pizziolo de jaleco branco" width="800" height="1000" loading="lazy">
    </figure>
    <div>
      <h2 style="font-size: clamp(2rem, 3.5vw, 2.5rem); margin-bottom: 1.5rem; color: var(--navy-900);">{"Quem vai avaliar você" if compacto else "Ortopedia para quem quer continuar em movimento"}</h2>
      <div class="prose" style="margin-top:1.2rem; font-size: 1.12rem; line-height: 1.65; color: var(--ink);">
        <p class="lede" style="font-size: 1.25rem; font-weight: 500; color: var(--navy-800); border-left: 4px solid var(--orange); padding-left: 1.2rem;">Sou médico ortopedista com atuação em trauma esportivo e artroscopia. Minha abordagem começa por um princípio simples: você precisa entender sua lesão e o motivo de cada etapa do tratamento.</p>{extra}
      </div>
      <ul class="creds" style="margin-top: 2.5rem;">
{li}
      </ul>
    </div>
  </div>
</section>"""


def faq(itens, titulo, lede):
    d = "\n".join("""      <details>
        <summary>%s</summary>
        <p class="answer">%s</p>
      </details>""" % qa for qa in itens)
    return f"""<section id="faq" style="background:#fff">
  <div class="wrap">
    <h2>{titulo}</h2>
    <p class="lede" style="margin-top:1rem">{lede}</p>
    <div class="faq">
{d}
    </div>
  </div>
</section>"""


def closing(titulo, texto, wa_txt):
    return f"""<section class="close on-dark">
  <div class="wrap">
    <h2>{titulo}</h2>
    <p>{texto}</p>
    <a class="btn btn-1 btn-lg" href="{wa(wa_txt)}">{ic("wa")}Agendar pelo WhatsApp</a>
  </div>
</section>"""


def footer(p, wa_dock):
    home = p or "./"
    return f"""</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="{p}assets/logo-marca.png" alt="" width="46" height="46">
        <p>Ortopedia e traumatologia com atuação em trauma esportivo e artroscopia. Ombro, cotovelo e joelho.</p>
      </div>
      <nav aria-label="Articulações">
        <h4>Articulações</h4>
        <ul>
          <li><a href="{p}ombro/">Ombro</a></li>
          <li><a href="{p}cotovelo/">Cotovelo</a></li>
          <li><a href="{p}joelho/">Joelho</a></li>
          <li><a href="{home}">Página inicial</a></li>
        </ul>
      </nav>
      <div>
        <h4>Contato</h4>
        <ul>
          <li><a href="{wa("Olá! Vim pelo site (rodapé) e gostaria de agendar.")}">WhatsApp (11) 91214-1608</a></li>
          <li><a href="mailto:thpizziolo@gmail.com">thpizziolo@gmail.com</a></li>
          <li><a href="https://www.instagram.com/drthalespizziolo" target="_blank" rel="noopener">@drthalespizziolo</a></li>
          <li><a href="https://www.doctoralia.com.br/thales-pizziolo/ortopedista-traumatologista/sao-paulo" target="_blank" rel="noopener">Doctoralia</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-legal">
      <p>Dr. Thales Pizziolo · CRM-SP 213316 · RQE 125841<br>R. Domingos de Morais, 2781 - 12 andar · Vila Mariana · São Paulo/SP</p>
      <p>As informações deste site têm caráter educativo e não substituem a consulta médica. O resultado de qualquer tratamento depende de avaliação individual.</p>
    </div>
  </div>
</footer>

<div class="dock is-hidden">
  <a class="btn btn-1" href="{wa(wa_dock)}">{ic("wa")}Agendar pelo WhatsApp</a>
</div>

<script>
(function(){{
  var els=document.querySelectorAll('.reveal');
  if(!('IntersectionObserver' in window)||window.matchMedia('(prefers-reduced-motion: reduce)').matches){{
    els.forEach(function(el){{el.classList.add('seen')}});return;
  }}
  var io=new IntersectionObserver(function(es){{es.forEach(function(e){{
    if(e.isIntersecting){{e.target.classList.add('seen');io.unobserve(e.target)}}
  }})}},{{threshold:.14,rootMargin:'0px 0px -6% 0px'}});
  els.forEach(function(el,i){{el.style.transitionDelay=(i%3*80)+'ms';io.observe(el)}});
}})();
(function(){{
  // Barra fixa do mobile: aparece só quando nenhum botão laranja do conteúdo
  // está na tela. Nunca dois "Agendar" idênticos visíveis ao mesmo tempo.
  var dock=document.querySelector('.dock');
  if(!dock) return;
  var ctas=document.querySelectorAll('main .btn-1');
  if(!ctas.length||!('IntersectionObserver' in window)){{dock.classList.remove('is-hidden');return;}}
  var vis=new Set();
  var obs=new IntersectionObserver(function(es){{
    es.forEach(function(e){{ e.isIntersecting ? vis.add(e.target) : vis.delete(e.target); }});
    dock.classList.toggle('is-hidden', vis.size>0);
  }},{{threshold:0}});
  ctas.forEach(function(c){{ obs.observe(c); }});
}})();
</script>
</body>
</html>
"""


# ---------------------------------------------------------------- páginas ---
def page_home():
    p = ""
    cards = "\n".join(f"""      <a class="joint reveal" href="{j['slug']}/">
        <div class="joint-img"><img src="assets/{j['img']}" alt="Ilustração anatômica da articulação do {j['nome'].lower()}" width="640" height="640" loading="lazy"></div>
        <div class="joint-body">
          <h3>{j['nome']}</h3>
          <p>{j['resumo']}</p>
          <span class="joint-go">Ver avaliação de {j['nome'].lower()}{ic("arrow")}</span>
        </div>
      </a>""" for j in JOINTS)

    steps = [("Entender", "Escutar sua história, seu esporte e o que você quer voltar a fazer."),
             ("Explicar", "Mostrar com clareza o diagnóstico e as possibilidades reais de tratamento."),
             ("Tratar", "Priorizar opções conservadoras e menos invasivas quando indicadas."),
             ("Retornar", "Planejar uma volta segura e progressiva à atividade física.")]
    st = "\n".join('      <li class="step" style="background: var(--bone-100); padding: 2rem; border-radius: var(--r); box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); transition: transform 0.3s ease, box-shadow 0.3s ease;"><h3 style="font-size: 1.25rem; color: var(--navy-800); margin-bottom: 0.8rem; display: flex; align-items: center; gap: 0.5rem;"><span style="display: flex; align-items: center; justify-content: center; width: 32px; height: 32px; border-radius: 50%%; background: var(--orange); color: #fff; font-size: 1rem;">%d</span> %s</h3><p style="color: var(--muted); font-size: 1rem; line-height: 1.6;">%s</p></li>' % (i+1, t, d) for i, (t, d) in enumerate(steps))

    html = head(p,
        "Ortopedista de Ombro, Cotovelo e Joelho na Vila Mariana | Dr. Thales Pizziolo",
        "Ortopedista especialista em ombro, cotovelo e joelho na Vila Mariana, São Paulo. Trauma esportivo e artroscopia. Tratamento conservador avaliado primeiro - cirurgia apenas quando há indicação. CRM-SP 213316 / RQE 125841.",
        SITE + "/", "hero.jpg")
    html += schema_physician() + "\n" + schema_faq(FAQ_HOME) + "\n"
    html += header(p)
    html += f"""
<section class="hero on-dark">
  <div class="wrap">
    <div>
      <h1 class="rise">
        Dor no ombro, cotovelo ou joelho?
        <span class="seo">Ortopedista especialista em Vila Mariana, São Paulo</span>
      </h1>
      <p class="lede rise rise-2">Atuação em trauma esportivo e artroscopia. A avaliação começa entendendo sua lesão - e o tratamento conservador é considerado antes de qualquer cirurgia.</p>
      <div class="hero-actions rise rise-3">
        <a class="btn btn-1 btn-lg" href="{wa("Olá! Vim pelo site e gostaria de agendar uma consulta.")}">{ic("wa")}Agendar pelo WhatsApp</a>
        <a class="btn btn-2 btn-lg" href="#articulacoes">Ver áreas de atuação</a>
      </div>
      <div class="rise rise-4">{trust()}</div>
    </div>
    <figure class="hero-figure rise rise-2" style="margin:0">
      <img src="assets/hero.jpg" alt="Dr. Thales Pizziolo, médico ortopedista" width="800" height="1000" fetchpriority="high">
    </figure>
  </div>
</section>

<section id="articulacoes">
  <span id="atuacao" aria-hidden="true"></span>
  <div class="wrap">
    <h2>Três articulações. Nada além delas.</h2>
    <p class="lede" style="margin-top:1rem">Atender só ombro, cotovelo e joelho é uma escolha. Concentrar o estudo e a prática em três articulações permite um olhar mais aprofundado sobre cada uma. Atendimento a partir de 14 anos.</p>
    <div class="joints">
{cards}
    </div>
  </div>
</section>

{stance()}

<section id="atendimento">
  <div class="wrap">
    <h2>Como funciona o atendimento</h2>
    <p class="lede" style="margin-top:1rem">O objetivo não é mandar você parar. Sempre que for clinicamente seguro, adaptamos sua atividade durante a recuperação.</p>
    <ol class="steps" style="gap: 1.5rem; margin-top: 3rem; list-style: none; padding: 0;">
{st}
    </ol>
  </div>
</section>

{about(p)}

{treatments("Do cuidado conservador à cirurgia - apenas quando necessária")}

{consultorio(p)}

{faq(FAQ_HOME, "Informação clara também faz parte do tratamento", "A consulta é o momento de entender seu caso em profundidade. Aqui estão respostas iniciais para as dúvidas mais comuns.")}

{closing("Entenda sua lesão. Trate com propósito.", "Agende uma avaliação e descubra as possibilidades de tratamento para o seu caso.", "Olá! Vim pelo site (final da página) e gostaria de agendar uma avaliação.")}
"""
    html += footer(p, "Olá! Vim pelo site (botão fixo) e gostaria de agendar.")
    return html


def consultorio(p):
    maps_link = "https://www.google.com/maps/search/?api=1&query=" + quote("Rua Domingos de Morais 2781 Vila Mariana São Paulo")
    maps_iframe = '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3656.368524317135!2d-46.63806452377519!3d-23.59114787878036!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce5a2b0e77d949%3A0xc3c57053e144a2b9!2sR.%20Domingos%20de%20Morais%2C%202781%20-%20Vila%20Mariana%2C%20S%C3%A3o%20Paulo%20-%20SP%2C%2004035-001!5e0!3m2!1spt-BR!2sbr!4v1714152345678!5m2!1spt-BR!2sbr" width="100%" height="100%" style="border:0; border-radius: var(--r); min-height: 400px; flex-grow: 1;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Google Maps - Localização do Consultório"></iframe>'
    return f"""<section id="consultorio" class="on-dark">
  <div class="wrap split flip">
    <div>
      <h2>Vila Mariana, no coração de São Paulo</h2>
      <address class="addr">
        <span class="street">R. Domingos de Morais, 2781 - 12 andar</span>
        <span class="more">Vila Mariana, São Paulo - SP, 04035-001</span>
      </address>

      <div style="margin-top: 1.8rem;">
        <p style="margin-bottom: 0.6rem; display: flex; align-items: center; gap: 0.6rem; font-size: 1.05rem;">
          <strong style="color: #fff;">WhatsApp:</strong> 
          <a href="{wa('Olá! Gostaria de agendar uma consulta.')}" style="color: var(--orange); text-decoration: none; font-weight: 500;">(11) 91214-1608</a>
        </p>
        <p style="margin-bottom: 0.6rem; display: flex; align-items: center; gap: 0.6rem; font-size: 1.05rem;">
          <strong style="color: #fff;">Instagram:</strong> 
          <a href="https://www.instagram.com/drthalespizziolo/" target="_blank" rel="noopener" style="color: var(--orange); text-decoration: none; font-weight: 500;">@drthalespizziolo</a>
        </p>
      </div>

      <div style="margin-top: 2rem; background: var(--navy-800); padding: 1.5rem; border-radius: var(--r); border: 1px solid var(--navy-700);">
        <h3 style="font-size: 1.15rem; color: #fff; margin-bottom: 1.2rem; display: flex; align-items: center; gap: 0.5rem;">Horário de Funcionamento</h3>
        <ul style="list-style: none; padding: 0; margin: 0; color: var(--on-navy-muted); font-size: 1rem; line-height: 1.8;">
          <li style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--navy-700); padding-bottom: 0.5rem; margin-bottom: 0.5rem;"><span>Domingo</span> <span style="font-weight: 500;">Fechado</span></li>
          <li style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--navy-700); padding-bottom: 0.5rem; margin-bottom: 0.5rem;"><span>Segunda a Sexta</span> <span style="font-weight: 500; color: #fff;">08:00 - 20:00</span></li>
          <li style="display: flex; justify-content: space-between;"><span>Sábado</span> <span style="font-weight: 500; color: #fff;">09:00 - 12:00</span></li>
        </ul>
      </div>

      <div class="hero-actions" style="margin-top:2rem;margin-bottom:0">
        <a class="btn btn-2" href="{maps_link}" target="_blank" rel="noopener">{ic("pin")}Ver rota no Maps</a>
      </div>
      
      <p class="note" style="margin-top: 2rem;">Atendimento particular, sem convênio, com possibilidade de emissão de nota fiscal para solicitação de reembolso ao seu plano de saúde.</p>
    </div>
    <figure class="split-figure" style="margin:0; display: flex; flex-direction: column; min-height: 500px;">
      {maps_iframe}
    </figure>
  </div>
</section>"""


def page_joint(j):
    p = "../"
    conds = "\n".join(f"""      <li>{ic("check")}<div><strong>{n}</strong><em>{d}</em></div></li>""" for n, d in j["conds"])
    sinais = "\n".join(f"""        <li>{ic("check")}<div><strong>{s}</strong></div></li>""" for s in SINAIS)

    html = head(p, j["title"], j["desc"], "%s/%s/" % (SITE, j["slug"]), j["img"])
    html += schema_physician() + "\n" + schema_faq(j["faq"]) + "\n" + schema_breadcrumb(j["nome"], j["slug"]) + "\n"
    html += header(p, j["slug"])
    html += f"""
<section class="hero hero-joint on-dark">
  <div class="wrap">
    <div>
      <nav class="crumbs rise" aria-label="Você está em"><a href="../">Início</a><span aria-hidden="true">/</span><span aria-current="page">{j['nome']}</span></nav>
      <h1 class="rise">
        {j['h1']}
        <span class="seo">{j['h1seo']}</span>
      </h1>
      <p class="lede rise rise-2">{j['lede']}</p>
      <div class="hero-actions rise rise-3">
        <a class="btn btn-1 btn-lg" href="{wa(j['wa'])}">{ic("wa")}Agendar avaliação de {j['nome'].lower()}</a>
      </div>
      <div class="rise rise-4">{trust()}</div>
    </div>
    <figure class="hero-figure hero-figure-joint rise rise-2" style="margin:0">
      <img src="../assets/{j['img']}" alt="Ilustração anatômica da articulação do {j['nome'].lower()}" width="900" height="900" fetchpriority="high">
    </figure>
  </div>
</section>

<section id="condicoes">
  <div class="wrap">
    <h2>{j['conds_h2']}</h2>
    <p class="lede" style="margin-top:1rem">A consulta serve para diferenciar condições que causam dores parecidas - e que pedem tratamentos diferentes.</p>
    <ul class="conds">
{conds}
    </ul>
  </div>
</section>

<section class="on-dark">
  <div class="wrap split flip">
    <div>
      <h2>Quando vale procurar avaliação</h2>
      <p class="lede" style="margin-top:1rem">Identificar os sinais cedo ajuda a evitar que uma lesão simples se torne mais grave.</p>
      <ul class="conds conds-1">
{sinais}
      </ul>
      <div class="hero-actions" style="margin-top:2.2rem;margin-bottom:0">
        <a class="btn btn-1 btn-lg" href="{wa(j['wa'])}">{ic("wa")}Agendar pelo WhatsApp</a>
      </div>
    </div>
    <figure class="split-figure" style="margin:0">
      <img src="../assets/retrato-casual.jpg" alt="Dr. Thales Pizziolo" width="800" height="1000" loading="lazy">
    </figure>
  </div>
</section>

{stance()}

{consultorio(p)}

"""
    html += footer(p, j["wa"])
    return html


def main():
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
        f.write(page_home())
    print("  public/index.html")
    for j in JOINTS:
        d = os.path.join(OUT, j["slug"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.html"), "w", encoding="utf-8") as f:
            f.write(page_joint(j))
        print("  public/%s/index.html" % j["slug"])

    urls = ["", "ombro/", "cotovelo/", "joelho/"]
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for u in urls:
            f.write("  <url><loc>%s/%s</loc><changefreq>monthly</changefreq><priority>%s</priority></url>\n"
                    % (SITE, u, "1.0" if u == "" else "0.9"))
        f.write("</urlset>\n")
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE)
    print("  public/sitemap.xml\n  public/robots.txt")


if __name__ == "__main__":
    main()
