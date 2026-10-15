#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador do site do Dr. Thales Pizziolo.

Edite o conteúdo aqui e rode:   python3 build.py
Saída em public/, que é a pasta que sobe para o servidor.

Cabeçalho, rodapé, barra fixa, aviso de cookies e ícones ficam num lugar só,
para as páginas nunca divergirem entre si.

As versões WebP das fotos, os ícones e as imagens de compartilhamento são
gerados à parte por gerar_imagens.py (precisa de Pillow). Este arquivo só
referencia o que já está em public/assets/.
"""
import hashlib
import json
import os
from urllib.parse import quote

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "public")
SITE = "https://www.drthalespizziolo.com.br"
WA = "5511912141608"
GTM = "GTM-WDB6CZFL"
ATUALIZADO = "2026-10-14"          # sitemap e política de privacidade
ATUALIZADO_EXTENSO = "14 de outubro de 2026"

FONTS = ("https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700"
         "&family=Spectral:ital,wght@1,500;1,600&display=swap")

# tamanhos exibidos, para o navegador escolher entre os arquivos -480 e -800
SIZES_HERO = "(max-width: 900px) calc(100vw - 2.5rem), 470px"
SIZES_SPLIT = "(max-width: 880px) min(390px, calc(100vw - 2.5rem)), 460px"


def wa(texto):
    """Link de WhatsApp com mensagem pré-preenchida. A mensagem identifica a
    origem para a secretária. É o rastreamento que sobrevive a bloqueador,
    iOS e recusa de cookies."""
    return "https://wa.me/%s?text=%s" % (WA, quote(texto, safe=""))


def css_versao():
    """Muda a URL do style.css sempre que o arquivo muda, para o cache longo
    da Vercel nunca servir CSS velho com HTML novo."""
    with open(os.path.join(OUT, "assets", "style.css"), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


def foto(p, nome, alt, sizes, prioridade=False):
    srcset = ", ".join("%sassets/%s-%d.webp %dw" % (p, nome, w, w) for w in (480, 800))
    carga = 'fetchpriority="high"' if prioridade else 'loading="lazy" decoding="async"'
    return ('<img src="%sassets/%s-800.webp" srcset="%s" sizes="%s" alt="%s" '
            'width="800" height="1200" %s>' % (p, nome, srcset, sizes, alt, carga))


# ---------------------------------------------------------------- ícones ----
SPRITE = """<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <symbol id="i-wa" viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.46 1.32 4.96L2 22l5.25-1.38c1.45.79 3.08 1.21 4.79 1.21 5.46 0 9.91-4.45 9.91-9.91S17.5 2 12.04 2m0 1.67c4.55 0 8.24 3.7 8.24 8.24s-3.69 8.25-8.24 8.25c-1.5 0-2.96-.4-4.24-1.16l-.3-.18-3.12.82.83-3.04-.19-.32a8.19 8.19 0 0 1-1.25-4.37c0-4.54 3.7-8.24 8.27-8.24m-3.7 4.1c-.18 0-.46.07-.7.33-.25.25-.94.92-.94 2.23 0 1.32.96 2.59 1.09 2.77.14.18 1.87 2.98 4.6 4.06 2.27.9 2.73.72 3.22.67.5-.04 1.6-.65 1.82-1.29.23-.63.23-1.18.16-1.29-.07-.11-.25-.18-.53-.32-.27-.14-1.6-.79-1.85-.88-.25-.09-.43-.14-.61.14-.18.27-.7.89-.86 1.07-.16.18-.32.2-.59.07-.27-.14-1.17-.43-2.23-1.38-.82-.73-1.38-1.63-1.54-1.9-.16-.28-.02-.43.11-.57.12-.13.32-.34.48-.52.16-.18.21-.3.32-.48.11-.18.05-.34-.02-.48-.07-.14-.6-1.47-.83-2-.18-.43-.37-.44-.53-.45h-.36Z"/></symbol>
  <symbol id="i-star" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2.3l2.9 5.9 6.5.95-4.7 4.6 1.1 6.5-5.8-3.05-5.8 3.05 1.1-6.5-4.7-4.6 6.5-.95L12 2.3Z"/></symbol>
  <symbol id="i-arrow" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" d="M5 12h14M13 6l6 6-6 6"/></symbol>
  <symbol id="i-pin" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></g></symbol>
  <symbol id="i-check" viewBox="0 0 24 24"><g fill="none" stroke="currentColor" stroke-width="2.1" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9.2"/><path d="m8.2 12.3 2.6 2.6 5-5.4"/></g></symbol>
</svg>"""


WA_AGENDAR = "Olá! Vim pelo Google e gostaria de agendar uma consulta com o Dr. Thales."


def ic(nome):
    return '<svg aria-hidden="true" focusable="false"><use href="#i-%s"/></svg>' % nome


# ------------------------------------------------------------- conteúdo -----
# Regra do CFM (Res. 2.336/2023): o RQE é de Ortopedia e Traumatologia.
# "Ortopedista de ombro" pode; "especialista em ombro" não.
JOINTS = [
    {
        "slug": "ombro", "nome": "Ombro", "og": "og-ombro.jpg",
        "resumo": "Bursite, tendinite, lesões do manguito rotador, luxações, instabilidade e traumas ligados ao esporte.",
        "title": "Tratamento de Bursite e Tendinite no Ombro na Vila Mariana | Dr. Thales Pizziolo",
        "desc": "Ortopedista de ombro na Vila Mariana, São Paulo. Avaliação de bursite, tendinite, manguito rotador e instabilidade. Tratamento conservador avaliado primeiro. CRM-SP 213316 / RQE 125841.",
        "h1": "Bursite, tendinite ou dor no ombro?",
        "h1seo": "Ortopedista de ombro em Vila Mariana, São Paulo",
        "lede": "O ombro é a articulação de maior amplitude do corpo, e por isso uma das que mais sofrem com esporte, sobrecarga e movimentos repetidos. A avaliação começa entendendo a origem da sua dor, antes de qualquer decisão de tratamento.",
        "wa": "Olá! Vim pelo Google e gostaria de saber mais sobre o tratamento de ombro.",
        "conds_h2": "O que é avaliado no ombro",
        "conds_lede": "Bursite, tendinite e lesão do manguito rotador causam dores parecidas, mas pedem tratamentos diferentes. A consulta serve para separar uma da outra.",
        "conds": [
            ("Bursite no ombro", "Inflamação da bolsa que reduz o atrito entre tendão e osso. Dor ao elevar o braço é comum."),
            ("Tendinite do manguito rotador", "Inflamação dos tendões que estabilizam o ombro, frequente em quem treina com carga."),
            ("Lesão do manguito rotador", "Desgaste ou ruptura parcial ou completa desses tendões, por trauma ou sobrecarga."),
            ("Tendinite calcária", "Depósito de cálcio dentro do tendão, que pode causar dor intensa e súbita."),
            ("Luxação e instabilidade", "Sensação de que o ombro sai do lugar, geralmente após trauma esportivo."),
            ("Dor por sobrecarga", "Dores ligadas a gestos repetidos no esporte ou no trabalho."),
        ],
        "etapas": [
            ("Como é a avaliação", "A consulta começa pela sua história: quando a dor começou, que movimento piora, se houve queda ou luxação e que esporte você pratica. No exame físico, testes específicos ajudam a separar dor da bursa, do tendão e da instabilidade. Raio-X, ultrassom ou ressonância são pedidos quando o resultado muda a conduta. Se você já tem exames, leve-os."),
            ("Tratamento sem cirurgia", "Bursite e tendinite do manguito costumam responder bem a controle da dor, fisioterapia com fortalecimento do manguito e da musculatura da escápula, e ajuste de carga no treino. Em casos selecionados, uma infiltração ajuda a reduzir a dor para que a reabilitação avance."),
            ("Quando a cirurgia entra", "A cirurgia é discutida quando há ruptura do manguito com perda de força, luxações que se repetem ou dor que não melhora depois de um tratamento conservador bem conduzido. Na maioria desses casos, ela é feita por artroscopia."),
        ],
        "sinais": [
            "Dor ao levantar o braço ou ao deitar sobre o ombro",
            "Perda de força para erguer ou segurar objetos",
            "Sensação de que o ombro sai do lugar",
            "Dor que continua depois de algumas semanas de repouso",
            "Queda ou trauma seguido de dor ou limitação",
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
        "slug": "cotovelo", "nome": "Cotovelo", "og": "og-cotovelo.jpg",
        "resumo": "Bursite, epicondilite, cotovelo de tenista, dores por sobrecarga e lesões que limitam a função.",
        "title": "Tratamento de Bursite e Epicondilite no Cotovelo na Vila Mariana | Dr. Thales Pizziolo",
        "desc": "Ortopedista de cotovelo na Vila Mariana, São Paulo. Avaliação de bursite, epicondilite, cotovelo de tenista e dor por sobrecarga. CRM-SP 213316 / RQE 125841.",
        "h1": "Bursite, epicondilite ou dor no cotovelo?",
        "h1seo": "Ortopedista de cotovelo em Vila Mariana, São Paulo",
        "lede": "Dor no cotovelo costuma aparecer aos poucos, no treino, na raquete ou no teclado, até atrapalhar gestos simples como segurar um copo. A avaliação identifica a origem da sobrecarga para tratar a causa, não só o sintoma.",
        "wa": "Olá! Vim pelo Google e gostaria de saber mais sobre o tratamento de cotovelo.",
        "conds_h2": "O que é avaliado no cotovelo",
        "conds_lede": "Boa parte das dores do cotovelo vem de sobrecarga nos tendões do antebraço. A consulta identifica qual estrutura está envolvida e o que está causando a sobrecarga.",
        "conds": [
            ("Bursite do olécrano", "Inflamação da bolsa na ponta do cotovelo. Inchaço visível é o sinal mais comum."),
            ("Epicondilite lateral", "Conhecida como cotovelo de tenista: dor na parte externa, ao segurar ou girar objetos."),
            ("Tendinite no cotovelo", "Inflamação dos tendões por gesto repetido, no esporte ou no trabalho."),
            ("Dor por sobrecarga", "Dores que surgem com o volume de treino ou de atividade repetitiva."),
            ("Lesões traumáticas", "Lesões decorrentes de queda ou impacto, que limitam o movimento."),
            ("Perda de função", "Dificuldade para estender, dobrar ou fazer força com o braço."),
        ],
        "etapas": [
            ("Como é a avaliação", "Dor na parte externa do cotovelo ao segurar uma xícara ou apertar a mão é o quadro típico da epicondilite lateral, mas não é a única causa possível. A consulta avalia o gesto que provoca a dor, no esporte ou no trabalho, e examina os tendões, a bursa e a estabilidade da articulação. Ultrassom ou ressonância entram quando o diagnóstico não está claro ou quando a dor não melhora."),
            ("Tratamento sem cirurgia", "A epicondilite costuma melhorar com ajuste do gesto e da carga, fisioterapia com exercícios para os tendões do antebraço e, em alguns casos, uso de órtese. A melhora é gradual e pode levar alguns meses. A bursite do olécrano sem infecção geralmente é tratada protegendo o cotovelo do apoio e controlando o inchaço."),
            ("Quando a cirurgia entra", "A cirurgia fica para a epicondilite que não melhora depois de meses de tratamento bem conduzido, para lesões traumáticas com instabilidade e para alguns casos de bursite que voltam ou infeccionam."),
        ],
        "sinais": [
            "Dor na parte externa ou interna do cotovelo ao segurar objetos",
            "Inchaço na ponta do cotovelo",
            "Dificuldade para esticar ou dobrar o braço",
            "Dor que volta sempre que você retoma o treino ou o trabalho",
            "Queda ou trauma seguido de dor ou limitação",
        ],
        "faq": [
            ("Cotovelo de tenista só acontece em quem joga tênis?", "Não. O nome vem do esporte, mas a epicondilite lateral aparece com frequência em quem faz movimentos repetidos de punho e antebraço, inclusive fora do esporte."),
            ("Bursite no cotovelo precisa ser drenada?", "Nem sempre. A conduta depende da causa, do tamanho e de haver ou não sinais de infecção, o que só a avaliação define."),
            ("Epicondilite tem tratamento sem cirurgia?", "Na grande maioria dos casos o tratamento é conservador. A cirurgia fica reservada a situações específicas, após avaliação individual."),
            ("Preciso parar de treinar?", "Nem sempre. Muitas vezes é possível adaptar a carga e o gesto durante a recuperação, com orientação."),
            ("O atendimento é por convênio?", "O atendimento é particular, sem convênio, com emissão de nota fiscal para você solicitar reembolso ao seu plano de saúde."),
        ],
    },
    {
        "slug": "joelho", "nome": "Joelho", "og": "og-joelho.jpg",
        "resumo": "Tendinite patelar, bursite, lesões ligamentares e de menisco, desgaste articular e lesões esportivas.",
        "title": "Tratamento de Tendinite e Dor no Joelho na Vila Mariana | Dr. Thales Pizziolo",
        "desc": "Ortopedista de joelho na Vila Mariana, São Paulo. Avaliação de tendinite patelar, bursite, lesões ligamentares e de menisco. Tratamento conservador avaliado primeiro. CRM-SP 213316 / RQE 125841.",
        "h1": "Tendinite, lesão ou dor no joelho?",
        "h1seo": "Ortopedista de joelho em Vila Mariana, São Paulo",
        "lede": "O joelho sustenta o corpo em cada passada, salto e mudança de direção. Por isso as lesões aparecem tanto em quem corre quanto em quem joga, treina ou simplesmente quer subir escada sem dor. A avaliação considera sua modalidade e seus objetivos.",
        "wa": "Olá! Vim pelo Google e gostaria de saber mais sobre o tratamento de joelho.",
        "conds_h2": "O que é avaliado no joelho",
        "conds_lede": "A mesma dor no joelho pode vir do tendão, do menisco, de um ligamento ou da cartilagem. A consulta separa essas causas antes de definir o tratamento.",
        "conds": [
            ("Tendinite patelar", "Conhecida como joelho de saltador: dor abaixo da patela, comum em corrida e esportes de salto."),
            ("Bursite no joelho", "Inflamação das bolsas ao redor da articulação, com dor e inchaço localizados."),
            ("Lesões ligamentares", "Entorses e lesões de ligamentos como o cruzado anterior, geralmente em mudança brusca de direção."),
            ("Lesão de menisco", "Lesão da cartilagem que amortece o joelho. Travamento e dor ao agachar são sinais frequentes."),
            ("Desgaste articular", "Alterações da cartilagem que causam dor e rigidez, com impacto na rotina."),
            ("Lesões esportivas", "Traumas e sobrecargas ligados à corrida, ao futebol, à musculação e a outras modalidades."),
        ],
        "etapas": [
            ("Como é a avaliação", "A consulta quer saber como a dor começou: numa torção, num salto ou aos poucos, com o aumento do volume de corrida. O exame testa ligamentos, meniscos e o tendão patelar, comparando com o outro joelho. A ressonância é pedida quando há suspeita de lesão de menisco ou de ligamento; nem toda dor no joelho precisa dela."),
            ("Tratamento sem cirurgia", "Tendinite patelar, bursite e boa parte das lesões de menisco e do desgaste articular são tratadas com fortalecimento muscular, ajuste de treino, controle da dor e, em casos selecionados, infiltração. Sempre que for seguro, o plano mantém você ativo durante a recuperação."),
            ("Quando a cirurgia entra", "A cirurgia é considerada quando o joelho trava, quando há instabilidade por lesão do ligamento cruzado anterior em quem quer voltar a esportes com giro, ou quando o tratamento conservador não resolve. Lesões de menisco e de ligamento costumam ser operadas por artroscopia."),
        ],
        "sinais": [
            "Inchaço depois de uma torção",
            "Joelho que trava ou falha",
            "Dor para subir escada, agachar ou correr",
            "Dor que volta sempre que você aumenta o treino",
            "Queda ou trauma seguido de dor ou limitação",
        ],
        "faq": [
            ("Toda lesão de ligamento no joelho precisa de cirurgia?", "Não. A decisão considera o tipo de lesão, o grau, a estabilidade do joelho e a demanda esportiva de cada paciente."),
            ("Lesão de menisco sempre é cirúrgica?", "Não. Muitas lesões de menisco são tratadas de forma conservadora. A indicação depende do padrão da lesão e dos sintomas."),
            ("Posso continuar correndo com dor no joelho?", "Depende da causa. Em muitos casos é possível adaptar o volume e a intensidade durante a recuperação, com orientação."),
            ("Quando a artroscopia de joelho é indicada?", "Quando há indicação adequada após avaliação. É uma técnica minimamente invasiva, mas continua sendo uma cirurgia, e só é considerada quando necessária."),
            ("O atendimento é por convênio?", "O atendimento é particular, sem convênio, com emissão de nota fiscal para você solicitar reembolso ao seu plano de saúde."),
        ],
    },
]

TRATAMENTOS = [
    ("Tratamento conservador", "Medicação, fisioterapia e ajuste de treino. É por onde a maioria dos casos começa."),
    ("Infiltrações", "Medicamento aplicado na articulação ou perto do tendão, só em situações específicas."),
    ("Procedimentos guiados", "Feitos com auxílio de imagem, para o medicamento chegar ao ponto certo."),
    ("Artroscopia", "Cirurgia com câmera, por pequenas incisões, quando o tratamento sem cirurgia não resolve."),
    ("Cirurgia ortopédica", "Quando indicada, o plano é explicado da preparação à reabilitação."),
    ("Retorno ao esporte", "Volta gradual ao treino, guiada por força e função, não só pelo calendário."),
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

ENDERECO = "R. Domingos de Morais, 2781, 12º andar"
MAPS_LINK = "https://www.google.com/maps/search/?api=1&query=" + quote("Rua Domingos de Morais 2781 Vila Mariana São Paulo")


# ------------------------------------------------------------- partes -------
def head(p, title, desc, canon, og_img, robots="index,follow,max-image-preview:large"):
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta name="robots" content="{robots}">
<meta name="geo.region" content="BR-SP">
<meta name="geo.placename" content="Vila Mariana, São Paulo">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="Dr. Thales Pizziolo">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE}/assets/{og_img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0B1826">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="{p}assets/icon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="{FONTS}" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="{FONTS}"></noscript>
<link rel="stylesheet" href="{p}assets/style.css?v={css_versao()}">
<script>
// Consentimento (Google Consent Mode v2), antes do GTM carregar.
// Medição do Google fica ligada até a pessoa recusar no aviso.
// Anúncio personalizado fica sempre desligado: é site de saúde.
// O Microsoft Clarity só carrega com "Aceitar" (evento consent_accept no GTM).
window.dataLayer=window.dataLayer||[];
function gtag(){{dataLayer.push(arguments);}}
(function(){{
  var c=null;try{{c=localStorage.getItem('tp_consent')}}catch(e){{}}
  var g=c==='recusado'?'denied':'granted';
  gtag('consent','default',{{ad_storage:g,analytics_storage:g,ad_user_data:g,ad_personalization:'denied'}});
  gtag('set','ads_data_redaction',true);
  if(c==='aceito')dataLayer.push({{event:'consent_accept'}});
}})();
</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});
var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;
j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})
(window,document,'script','dataLayer','{GTM}');</script>
"""


def schema_physician():
    return '<script type="application/ld+json">%s</script>' % json.dumps({
        "@context": "https://schema.org", "@type": "Physician",
        "name": "Dr. Thales Pizziolo",
        "alternateName": "Thales Ramos Pizziolo",
        "medicalSpecialty": "https://schema.org/Musculoskeletal",
        "description": "Ortopedista e traumatologista (RQE 125841) com atuação em trauma esportivo e artroscopia. Atende ombro, cotovelo e joelho, a partir de 14 anos, em consultas particulares.",
        "url": SITE + "/",
        "image": SITE + "/assets/hero.jpg",
        "logo": SITE + "/assets/icon-192.png",
        "telephone": "+5511912141608",
        "email": "thpizziolo@gmail.com",
        "isAcceptingNewPatients": True,
        "address": {"@type": "PostalAddress",
                    "streetAddress": "Rua Domingos de Morais, 2781, 12º andar, Edifício Artwork",
                    "addressLocality": "São Paulo", "addressRegion": "SP",
                    "postalCode": "04035-001", "addressCountry": "BR"},
        "geo": {"@type": "GeoCoordinates", "latitude": -23.6009, "longitude": -46.6362},
        "hasMap": MAPS_LINK,
        "openingHoursSpecification": [
            {"@type": "OpeningHoursSpecification",
             "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
             "opens": "08:00", "closes": "20:00"},
            {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday",
             "opens": "09:00", "closes": "12:00"},
        ],
        "areaServed": {"@type": "City", "name": "São Paulo"},
        "sameAs": ["https://www.doctoralia.com.br/thales-pizziolo/ortopedista-traumatologista/sao-paulo",
                   "https://www.instagram.com/drthalespizziolo"],
    }, ensure_ascii=False)


def schema_faq(itens):
    return '<script type="application/ld+json">%s</script>' % json.dumps({
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in itens]
    }, ensure_ascii=False)


def schema_breadcrumb(nome, slug):
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
      <img src="{p}assets/logo-96.webp" alt="" width="38" height="38">
      <span class="visually-hidden">Dr. Thales Pizziolo, página inicial</span>
      <span class="brand-text" aria-hidden="true"><b class="brand-name">Dr. Thales Pizziolo</b><span class="brand-sub">Ortopedista · CRM-SP 213316</span></span>
    </a>
    <nav class="nav" aria-label="Principal">
      {nav("ombro","Ombro")}
      {nav("cotovelo","Cotovelo")}
      {nav("joelho","Joelho")}
      <a href="{home}#sobre">Sobre</a>
      <a href="{home}#consultorio">Consultório</a>
    </nav>
    <a class="btn btn-1 header-cta" href="{wa(next((j["wa"] for j in JOINTS if j["slug"] == atual), WA_AGENDAR))}">{ic("wa")}Agendar</a>
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
    li = "\n".join('      <li class="treat-card"><h3>%s</h3><p>%s</p><a class="treat-btn" href="%s">Saber mais<span class="treat-btn-ic">%s</span></a></li>' % (t, d, wa("Olá! Vim pelo Google e gostaria de saber mais sobre %s." % t.lower()), ic("arrow")) for t, d in TRATAMENTOS)
    return f"""<section id="tratamentos">
  <div class="wrap">
    <h2>{titulo}</h2>
    <ul class="treat">
{li}
    </ul>
    <p class="note" style="color:var(--muted); text-align: center; margin-inline: auto;">A indicação de qualquer tratamento depende de consulta médica e avaliação individual.</p>
  </div>
</section>"""


def about(p, compacto=False):
    li = "\n".join('        <li><b>%s</b><span>%s</span></li>' % c for c in CREDS)
    extra = "" if compacto else """
        <p style="margin-top:1.1rem;color:var(--text-dark);">Construo uma estratégia individualizada, priorizando tratamentos não cirúrgicos e minimamente invasivos quando indicados, sem perder de vista a atividade que faz parte da sua vida. Corredor de rua e praticante de musculação, conheço de perto o valor que o esporte tem na rotina de cada pessoa.</p>"""
    return f"""<section id="sobre" style="background:#fff">
  <div class="wrap split">
    <figure class="split-figure" style="margin:0">
      {foto(p, "sobre", "Dr. Thales Pizziolo de jaleco branco", SIZES_SPLIT)}
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


def faq(itens, titulo, lede=None, fundo="#fff"):
    d = "\n".join("""      <details>
        <summary>%s</summary>
        <p class="answer">%s</p>
      </details>""" % qa for qa in itens)
    lede_html = f'\n    <p class="lede" style="margin-top:1rem">{lede}</p>' if lede else ""
    return f"""<section id="faq" style="background:{fundo}">
  <div class="wrap">
    <h2>{titulo}</h2>{lede_html}
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


COOKIE_JS = """(function(){
  // Aviso de cookies. A escolha fica no localStorage (tp_consent) e o
  // <head> a lê antes do GTM em toda página.
  var box=document.getElementById('cookie');
  if(!box) return;
  var c=null;try{c=localStorage.getItem('tp_consent')}catch(e){}
  function abrir(){box.hidden=false;document.body.classList.add('cookie-open')}
  function fechar(){box.hidden=true;document.body.classList.remove('cookie-open')}
  function apagar(){
    // ao recusar, remove os cookies de medição que já existiam
    var dom=['', '; domain=.drthalespizziolo.com.br', '; domain=www.drthalespizziolo.com.br'];
    document.cookie.split(';').forEach(function(k){
      var n=k.split('=')[0].trim();
      if(/^(_ga|_gid|_gcl_|_clck|_clsk)/.test(n)) dom.forEach(function(d){
        document.cookie=n+'=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/'+d;
      });
    });
  }
  if(!c) abrir();
  box.addEventListener('click',function(e){
    var b=e.target.closest('[data-consent]');
    if(!b) return;
    var v=b.getAttribute('data-consent');
    try{localStorage.setItem('tp_consent',v)}catch(err){}
    var g=v==='aceito'?'granted':'denied';
    gtag('consent','update',{ad_storage:g,analytics_storage:g,ad_user_data:g,ad_personalization:'denied'});
    if(v==='aceito'&&c!=='aceito') dataLayer.push({event:'consent_accept'});
    if(v==='recusado'){
      try{if(window.clarity) window.clarity('consent',false)}catch(err){}
      apagar();
    }
    c=v;fechar();
  });
  document.querySelectorAll('[data-cookie-prefs]').forEach(function(a){
    a.addEventListener('click',function(e){e.preventDefault();abrir();box.querySelector('button').focus();});
  });
})();"""


def footer(p, wa_dock):
    home = p or "./"
    return f"""</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="{p}assets/logo-96.webp" alt="" width="46" height="46" loading="lazy">
        <p>Ortopedia e traumatologia com atuação em trauma esportivo e artroscopia. Ombro, cotovelo e joelho.</p>
      </div>
      <nav aria-label="Articulações">
        <h2 class="foot-h">Articulações</h2>
        <ul>
          <li><a href="{p}ombro/">Ombro</a></li>
          <li><a href="{p}cotovelo/">Cotovelo</a></li>
          <li><a href="{p}joelho/">Joelho</a></li>
          <li><a href="{home}">Página inicial</a></li>
        </ul>
      </nav>
      <div>
        <h2 class="foot-h">Contato</h2>
        <ul>
          <li><a href="{wa(wa_dock)}">WhatsApp (11) 91214-1608</a></li>
          <li><a href="mailto:thpizziolo@gmail.com">thpizziolo@gmail.com</a></li>
          <li><a href="https://www.instagram.com/drthalespizziolo" target="_blank" rel="noopener">@drthalespizziolo</a></li>
          <li><a href="https://www.doctoralia.com.br/thales-pizziolo/ortopedista-traumatologista/sao-paulo" target="_blank" rel="noopener">Doctoralia</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-legal">
      <p>Dr. Thales Pizziolo · CRM-SP 213316 · RQE 125841<br>{ENDERECO} · Vila Mariana · São Paulo/SP</p>
      <p>As informações deste site têm caráter educativo e não substituem a consulta médica. O resultado de qualquer tratamento depende de avaliação individual.</p>
      <p class="foot-links"><a href="{p}privacidade/">Política de privacidade</a><button type="button" class="link-btn" data-cookie-prefs>Preferências de cookies</button></p>
    </div>
  </div>
</footer>

<div class="dock is-hidden">
  <a class="btn btn-1" href="{wa(wa_dock)}">{ic("wa")}Agendar pelo WhatsApp</a>
</div>

<div class="cookie" id="cookie" role="region" aria-label="Aviso de cookies" hidden>
  <p>Usamos cookies do Google para medir visitas e o resultado dos anúncios. Se você aceitar, também usamos o Microsoft Clarity para ver como o site é usado. <a href="{p}privacidade/">Política de privacidade</a></p>
  <div class="cookie-btns">
    <button type="button" class="btn btn-1" data-consent="aceito">Aceitar</button>
    <button type="button" class="btn btn-2" data-consent="recusado">Recusar</button>
  </div>
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
{COOKIE_JS}
</script>
</body>
</html>
"""


# ---------------------------------------------------------------- páginas ---
def page_home():
    p = ""
    cards = "\n".join(f"""      <a class="joint reveal" href="{j['slug']}/">
        <div class="joint-body">
          <h3>{j['nome']}</h3>
          <p>{j['resumo']}</p>
          <span class="joint-go">Ver {j['nome'].lower()}{ic("arrow")}</span>
        </div>
      </a>""" for j in JOINTS)

    steps = [("Entender", "Escutar sua história, seu esporte e o que você quer voltar a fazer."),
             ("Explicar", "Mostrar com clareza o diagnóstico e as possibilidades reais de tratamento."),
             ("Tratar", "Priorizar opções conservadoras e menos invasivas quando indicadas."),
             ("Retornar", "Planejar uma volta segura e progressiva à atividade física.")]
    st = "\n".join('      <li class="step"><h3><span class="step-n">%d</span>%s</h3><p>%s</p></li>' % (i+1, t, d) for i, (t, d) in enumerate(steps))

    html = head(p,
        "Ortopedista de Ombro, Cotovelo e Joelho na Vila Mariana | Dr. Thales Pizziolo",
        "Ortopedista na Vila Mariana (SP) com atuação em trauma esportivo e artroscopia. Atende ombro, cotovelo e joelho, com tratamento conservador avaliado primeiro. CRM-SP 213316 / RQE 125841.",
        SITE + "/", "og-home.jpg")
    html += schema_physician() + "\n" + schema_faq(FAQ_HOME) + "\n"
    html += header(p)
    html += f"""
<section class="hero on-dark">
  <div class="wrap">
    <div>
      <h1 class="rise">
        Dor no ombro, cotovelo ou joelho?
        <span class="seo">Ortopedista em Vila Mariana, São Paulo</span>
      </h1>
      <p class="lede rise rise-2">Atuação em trauma esportivo e artroscopia. A avaliação começa entendendo sua lesão, e o tratamento conservador é considerado antes de qualquer cirurgia.</p>
      <div class="hero-actions rise rise-3">
        <a class="btn btn-1 btn-lg" href="{wa(WA_AGENDAR)}">{ic("wa")}Agendar pelo WhatsApp</a>
        <a class="btn btn-2 btn-lg" href="#articulacoes">Ver áreas de atuação</a>
      </div>
      <div class="rise rise-4">{trust()}</div>
    </div>
    <figure class="hero-figure rise rise-2" style="margin:0">
      {foto(p, "hero", "Dr. Thales Pizziolo, médico ortopedista", SIZES_HERO, prioridade=True)}
    </figure>
  </div>
</section>

<section id="articulacoes">
  <span id="atuacao" aria-hidden="true"></span>
  <div class="wrap">
    <h2>Ombro, cotovelo e joelho</h2>
    <p class="lede" style="margin-top:1rem">O atendimento é dedicado a essas três articulações, para pacientes a partir de 14 anos. Escolha uma para ver o que é avaliado e como costuma ser o tratamento.</p>
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
    <ol class="steps">
{st}
    </ol>
  </div>
</section>

{about(p)}

{treatments("Do tratamento conservador à cirurgia, quando ela é necessária")}

{consultorio(p)}

{faq(FAQ_HOME, "Perguntas frequentes", "Respostas curtas para as dúvidas mais comuns. O seu caso é discutido em detalhe na consulta.")}

{closing("Agende sua avaliação", "O agendamento é feito pelo WhatsApp. Atendimento particular, com nota fiscal para pedir reembolso ao plano de saúde.", WA_AGENDAR)}
"""
    html += footer(p, WA_AGENDAR)
    return html


def consultorio(p, msg=WA_AGENDAR):
    maps_iframe = '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3656.368524317135!2d-46.63806452377519!3d-23.59114787878036!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94ce5a2b0e77d949%3A0xc3c57053e144a2b9!2sR.%20Domingos%20de%20Morais%2C%202781%20-%20Vila%20Mariana%2C%20S%C3%A3o%20Paulo%20-%20SP%2C%2004035-001!5e0!3m2!1spt-BR!2sbr!4v1714152345678!5m2!1spt-BR!2sbr" width="100%" height="100%" style="border:0; border-radius: var(--r); min-height: 400px; flex-grow: 1;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mapa do consultório no Google Maps"></iframe>'
    return f"""<section id="consultorio" class="on-dark">
  <div class="wrap split flip">
    <div>
      <h2>Vila Mariana, no coração de São Paulo</h2>
      <address class="addr">
        <span class="street">{ENDERECO}</span>
        <span class="more">Vila Mariana, São Paulo, SP · 04035-001</span>
      </address>

      <div style="margin-top: 1.8rem;">
        <p style="margin-bottom: 0.6rem; display: flex; align-items: center; gap: 0.6rem; font-size: 1.05rem;">
          <strong style="color: #fff;">WhatsApp:</strong>
          <a href="{wa(msg)}" style="color: var(--orange); text-decoration: none; font-weight: 500;">(11) 91214-1608</a>
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
          <li style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--navy-700); padding-bottom: 0.5rem; margin-bottom: 0.5rem;"><span>Segunda a Sexta</span> <span style="font-weight: 500; color: #fff;">8h às 20h</span></li>
          <li style="display: flex; justify-content: space-between;"><span>Sábado</span> <span style="font-weight: 500; color: #fff;">9h às 12h</span></li>
        </ul>
      </div>

      <div class="hero-actions" style="margin-top:2rem;margin-bottom:0">
        <a class="btn btn-2" href="{MAPS_LINK}" target="_blank" rel="noopener">{ic("pin")}Ver rota no Maps</a>
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
    sinais = "\n".join(f"""        <li>{ic("check")}<div><strong>{s}</strong></div></li>""" for s in j["sinais"])
    etapas = "\n".join(f"""      <article class="etapa">
        <h3>{t}</h3>
        <p>{d}</p>
      </article>""" for t, d in j["etapas"])

    html = head(p, j["title"], j["desc"], "%s/%s/" % (SITE, j["slug"]), j["og"])
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
    <figure class="hero-figure rise rise-2" style="margin:0">
      {foto(p, "consultorio", "Dr. Thales Pizziolo em consultório", SIZES_HERO, prioridade=True)}
    </figure>
  </div>
</section>

<section id="condicoes">
  <div class="wrap">
    <h2>{j['conds_h2']}</h2>
    <p class="lede" style="margin-top:1rem">{j['conds_lede']}</p>
    <ul class="conds">
{conds}
    </ul>
  </div>
</section>

<section id="tratamento" style="background:#fff">
  <div class="wrap">
    <h2>Da avaliação ao tratamento</h2>
    <div class="etapas">
{etapas}
    </div>
    <p class="note" style="color:var(--muted)">Cada caso é diferente. A indicação de qualquer tratamento depende de consulta médica e avaliação individual.</p>
  </div>
</section>

<section class="on-dark">
  <div class="wrap split flip">
    <div>
      <h2>Quando vale procurar avaliação</h2>
      <p class="lede" style="margin-top:1rem">Se algum destes sinais aparece, vale marcar uma consulta.</p>
      <ul class="conds conds-1">
{sinais}
      </ul>
      <div class="hero-actions" style="margin-top:2.2rem;margin-bottom:0">
        <a class="btn btn-1 btn-lg" href="{wa(j['wa'])}">{ic("wa")}Agendar pelo WhatsApp</a>
      </div>
    </div>
    <figure class="split-figure" style="margin:0">
      {foto(p, "retrato-casual", "Dr. Thales Pizziolo", SIZES_SPLIT)}
    </figure>
  </div>
</section>

{faq(j["faq"], "Dúvidas sobre o " + j["nome"].lower(), fundo="var(--bone)")}

{stance()}

{consultorio(p, j["wa"])}

"""
    html += footer(p, j["wa"])
    return html


# ------------------------------------------------------- privacidade ------
PRIVACIDADE = f"""
<h1>Política de privacidade</h1>
<p class="doc-meta">Última atualização: {ATUALIZADO_EXTENSO}</p>

<p>Esta política explica quais dados o site drthalespizziolo.com.br coleta, para que eles servem e como você pode recusar ou pedir a exclusão. Ela segue a Lei Geral de Proteção de Dados (Lei 13.709/2018, a LGPD).</p>

<h2>Quem é o responsável</h2>
<p>Dr. Thales Pizziolo, médico ortopedista, CRM-SP 213316, com consultório na Rua Domingos de Morais, 2781, 12º andar, Vila Mariana, São Paulo/SP, CEP 04035-001.</p>
<p>Para qualquer assunto sobre seus dados pessoais, escreva para <a href="mailto:thpizziolo@gmail.com">thpizziolo@gmail.com</a>.</p>

<h2>O que o site coleta</h2>
<p><strong>O site não tem formulário nem cadastro.</strong> Ele não pede nome, e-mail, telefone ou CPF.</p>
<p><strong>Dados de navegação.</strong> Quando você visita o site, ferramentas do Google registram as páginas vistas, quanto tempo você ficou, de onde veio (por exemplo, uma busca ou um anúncio), o tipo de aparelho e navegador, a cidade aproximada e os cliques nos botões de WhatsApp. Usamos o Google Tag Manager, o Google Analytics 4 e a medição de conversões do Google Ads.</p>
<p><strong>Microsoft Clarity, só se você aceitar.</strong> O Clarity registra cliques, rolagem e movimentos na página, em forma de mapas de calor e gravações da sessão. Textos digitados ficam mascarados. Ele só é carregado depois que você clica em “Aceitar” no aviso de cookies.</p>
<p><strong>Contato pelo WhatsApp.</strong> Os botões de agendamento abrem o WhatsApp com uma mensagem já escrita, que indica de qual página você veio (por exemplo, “tratamento de joelho”). Nada é enviado se você não mandar a mensagem. Se mandar, o que você escrever é usado pelo consultório para responder e agendar a consulta, e também passa pelo WhatsApp, que segue a política de privacidade da Meta.</p>
<p><strong>Conteúdo de terceiros.</strong> O mapa do consultório vem do Google Maps e as fontes de texto vêm do Google Fonts. Para carregar esse conteúdo, o Google recebe o endereço IP e dados técnicos do seu navegador. A hospedagem do site (Vercel) também registra o IP em seus registros de acesso.</p>

<h2>Para que usamos</h2>
<ul>
  <li>Saber quantas pessoas visitam o site e quais páginas são úteis.</li>
  <li>Saber se os anúncios no Google trazem pessoas que entram em contato, para decidir onde investir.</li>
  <li>Melhorar o site, com base em como ele é usado.</li>
  <li>Responder e agendar consultas pelo WhatsApp.</li>
</ul>
<p>Não usamos os dados de navegação para anúncios personalizados: essa função fica desligada no site, porque as páginas tratam de condições de saúde. Não vendemos dados.</p>

<h2>Bases legais</h2>
<ul>
  <li><strong>Medição de visitas e de anúncios (Google):</strong> legítimo interesse (art. 7º, IX), com a opção de recusar a qualquer momento.</li>
  <li><strong>Microsoft Clarity:</strong> consentimento (art. 7º, I), dado ao clicar em “Aceitar”.</li>
  <li><strong>Atendimento pelo WhatsApp:</strong> procedimentos preliminares a uma consulta, a seu pedido (art. 7º, V). Informações de saúde que você decidir contar na mensagem são tratadas para a tutela da sua saúde, por profissional de saúde (art. 11, II, f).</li>
</ul>

<h2>Cookies</h2>
<div class="doc-table">
<table>
  <thead><tr><th>Nome</th><th>De quem</th><th>Para que</th><th>Duração</th></tr></thead>
  <tbody>
    <tr><td>_ga, _ga_*</td><td>Google Analytics</td><td>Distinguir visitantes e sessões</td><td>até 2 anos</td></tr>
    <tr><td>_gcl_au, _gcl_aw</td><td>Google Ads</td><td>Ligar um contato ao anúncio que o trouxe</td><td>90 dias</td></tr>
    <tr><td>_clck, _clsk</td><td>Microsoft Clarity (só com aceite)</td><td>Agrupar as páginas de uma mesma visita</td><td>1 ano e 1 dia</td></tr>
    <tr><td>tp_consent</td><td>Este site (armazenamento local)</td><td>Lembrar sua escolha no aviso de cookies</td><td>até você limpar o navegador</td></tr>
  </tbody>
</table>
</div>
<p>Você pode mudar sua escolha quando quiser em <button type="button" class="link-btn" data-cookie-prefs>Preferências de cookies</button>, que também está no rodapé de todas as páginas. Ao recusar, os cookies de medição são apagados e o Google passa a receber apenas sinais sem identificador. Também é possível bloquear cookies nas configurações do navegador.</p>

<h2>Com quem os dados são compartilhados</h2>
<p>Com os fornecedores das ferramentas citadas: Google (Analytics, Ads, Tag Manager, Maps e Fonts), Microsoft (Clarity), Meta (WhatsApp) e Vercel (hospedagem). Esses serviços guardam dados em servidores fora do Brasil, com as garantias contratuais previstas no art. 33 da LGPD.</p>

<h2>Por quanto tempo</h2>
<ul>
  <li>Google Analytics: os relatórios detalhados ficam disponíveis por até 14 meses.</li>
  <li>Microsoft Clarity: gravações por até 30 dias e mapas de calor por até 13 meses.</li>
  <li>Conversas no WhatsApp: pelo tempo necessário ao atendimento. Os dados da consulta, quando ela acontece, seguem as regras do prontuário médico.</li>
</ul>

<h2>Seus direitos</h2>
<p>Pela LGPD (art. 18), você pode pedir a confirmação de que tratamos seus dados, acesso, correção, anonimização ou eliminação, portabilidade, informação sobre com quem compartilhamos e a revogação do consentimento. Basta escrever para <a href="mailto:thpizziolo@gmail.com">thpizziolo@gmail.com</a>; respondemos em até 15 dias. Você também pode reclamar à Autoridade Nacional de Proteção de Dados (ANPD).</p>

<h2>Menores de idade</h2>
<p>O site é informativo e não coleta dados de cadastro. O atendimento começa aos 14 anos; consultas de menores de 18 anos são agendadas com um responsável.</p>

<h2>Mudanças nesta política</h2>
<p>Se a forma de coletar dados mudar, esta página será atualizada e a data no topo mudará.</p>
"""


def page_privacidade():
    p = "../"
    html = head(p, "Política de privacidade | Dr. Thales Pizziolo",
                "Quais dados o site do Dr. Thales Pizziolo coleta, para que servem e como recusar ou pedir a exclusão, conforme a LGPD.",
                SITE + "/privacidade/", "og-home.jpg")
    html += header(p)
    html += f"""
<section class="doc-page">
  <div class="wrap">
    <nav class="crumbs crumbs-light" aria-label="Você está em"><a href="../">Início</a><span aria-hidden="true">/</span><span aria-current="page">Política de privacidade</span></nav>
    <article class="doc">
{PRIVACIDADE}
    </article>
  </div>
</section>
"""
    html += footer(p, WA_AGENDAR)
    return html


def page_404():
    # servida em qualquer URL inexistente: caminhos absolutos
    p = "/"
    html = head(p, "Página não encontrada | Dr. Thales Pizziolo",
                "A página procurada não existe no site do Dr. Thales Pizziolo.",
                SITE + "/", "og-home.jpg", robots="noindex,follow")
    html += header(p)
    html += f"""
<section class="doc-page">
  <div class="wrap">
    <article class="doc">
      <h1>Página não encontrada</h1>
      <p>O endereço pode ter mudado ou estar digitado errado. Estas são as páginas do site:</p>
      <ul>
        <li><a href="/">Página inicial</a></li>
        <li><a href="/ombro/">Ombro</a></li>
        <li><a href="/cotovelo/">Cotovelo</a></li>
        <li><a href="/joelho/">Joelho</a></li>
      </ul>
      <p>Para agendar uma consulta, fale pelo WhatsApp.</p>
      <p style="margin-top:1.5rem"><a class="btn btn-1" href="{wa(WA_AGENDAR)}">{ic("wa")}Agendar pelo WhatsApp</a></p>
    </article>
  </div>
</section>
"""
    html += footer(p, WA_AGENDAR)
    return html


def llms_txt():
    linhas = [
        "# Dr. Thales Pizziolo: ortopedista na Vila Mariana, São Paulo",
        "",
        "> Médico ortopedista e traumatologista (CRM-SP 213316, RQE 125841) com atuação em trauma esportivo e artroscopia. Atende ombro, cotovelo e joelho, a partir de 14 anos. Consulta particular, sem convênio, com nota fiscal para reembolso do plano de saúde.",
        "",
        "## Atendimento",
        "",
        "- Endereço: Rua Domingos de Morais, 2781, 12º andar (Edifício Artwork), Vila Mariana, São Paulo/SP, CEP 04035-001",
        "- Agendamento: WhatsApp (11) 91214-1608, https://wa.me/%s" % WA,
        "- Horário: segunda a sexta, das 8h às 20h; sábado, das 9h às 12h",
        "- Forma de atendimento: particular, sem convênio; emite nota fiscal para o paciente pedir reembolso ao plano",
        "- Idade: a partir de 14 anos",
        "- Abordagem: o tratamento conservador é considerado antes de qualquer cirurgia",
        "",
        "## Páginas",
        "",
        "- [Início](%s/): visão geral, formação, tratamentos e perguntas frequentes" % SITE,
    ]
    for j in JOINTS:
        linhas.append("- [%s](%s/%s/): %s" % (j["nome"], SITE, j["slug"], j["resumo"]))
    linhas += [
        "- [Política de privacidade](%s/privacidade/)" % SITE,
        "",
        "## Formação",
        "",
    ]
    linhas += ["- %s: %s" % (b, s) for b, s in CREDS[:4]]
    linhas += [
        "",
        "## Perfis",
        "",
        "- Doctoralia: https://www.doctoralia.com.br/thales-pizziolo/ortopedista-traumatologista/sao-paulo",
        "- Instagram: https://www.instagram.com/drthalespizziolo",
        "",
    ]
    return "\n".join(linhas)


def escrever(caminho, conteudo):
    full = os.path.join(OUT, caminho)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(conteudo)
    print("  public/" + caminho)


def main():
    escrever("index.html", page_home())
    for j in JOINTS:
        escrever(j["slug"] + "/index.html", page_joint(j))
    escrever("privacidade/index.html", page_privacidade())
    escrever("404.html", page_404())
    escrever("llms.txt", llms_txt())

    urls = [("", "1.0"), ("ombro/", "0.9"), ("cotovelo/", "0.9"), ("joelho/", "0.9"), ("privacidade/", "0.2")]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    sm += ["  <url><loc>%s/%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>" % (SITE, u, ATUALIZADO, pr)
           for u, pr in urls]
    sm.append("</urlset>\n")
    escrever("sitemap.xml", "\n".join(sm))
    escrever("robots.txt", "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE)


if __name__ == "__main__":
    main()
