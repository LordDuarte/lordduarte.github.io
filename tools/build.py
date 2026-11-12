#!/usr/bin/env python3
"""Gera as páginas estáticas PT (raiz) e EN (/en/). Rodar: python3 tools/build.py
O resultado é commitado, porque o GitHub Pages serve os arquivos como estão."""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://lordlimastudio.com"
DEV = "https://play.google.com/store/apps/dev?id=8411854920311777114"
RICO_PLAY = "https://play.google.com/store/apps/details?id=com.lordlima.ricochetrescue"
PRIV = {
    "oops": "https://lordduarte.github.io/oops_potion-privacidade/",
    "rico": "https://lordduarte.github.io/ricochet_rescue-privacidade/",
    "loteco": "https://lordduarte.github.io/Loteco-privacidade/",
}
EMAIL = "lordlimastudio@gmail.com"
PAGES = ["/", "/games/", "/games/ricochet-rescue/", "/games/oops-potion/", "/about/", "/contact/", "/privacy/"]

S = {
 "pt": {
  "html": "pt-BR", "other": "EN", "otherlabel": "English",
  "nav_games": "Jogos", "nav_about": "Estúdio", "nav_contact": "Contato", "nav_priv": "Privacidade",
  "skip": "Ir para o conteúdo",
  "tagline": "Jogos pequenos, feitos com capricho",
  "home_title": "Lord Lima Studio | Jogos mobile em pixel art",
  "home_desc": "Estúdio indie de jogos para Android feitos em Unity, com pixel art e mecânicas fáceis de entender. Ricochet Rescue e Oops Potion.",
  "h_eyebrow": "Estúdio indie de jogos mobile",
  "h_title": "Jogos pequenos, <em>feitos com capricho</em>.",
  "h_lead": "Desenvolvo jogos para Android em Unity, com pixel art, mecânicas fáceis de entender e muita personalidade.",
  "h_cta1": "VER JOGOS", "h_cta2": "GOOGLE PLAY",
  "mascot_alt": "Mascote do Lord Lima Studio: uma ervilha com coroa dourada, óculos escuros e cetro",
  "g_eyebrow": "Catálogo", "g_title": "Jogos",
  "g_lead": "Cada jogo tem página própria com descrição, imagens e link para a loja.",
  "oops_alt": "Oops Potion: Misture, acerte, descubra!",
  "rico_alt": "Ricochet Rescue: Mire. Ricocheteie. Resgate.",
  "chip_dev": "EM DESENVOLVIMENTO", "chip_play": "GOOGLE PLAY",
  "oops_short": "Escolha os ingredientes, acerte as doses e mexa o caldeirão. Cada poção tem um efeito que você só descobre bebendo: chifres, asas, chamas no chapéu. Complete o livro com 40 receitas.",
  "rico_short": "Mire. Ricocheteie. Resgate. Um cowboy, uma arma e balas que ricocheteiam: corte a corda, salve os reféns e derrube os bandidos no Velho Oeste. 66 fases, munições especiais e fases bônus de caça ao pato.",
  "f_rec": "receitas", "f_eff": "efeitos", "f_ing": "ingredientes por mistura",
  "f_lvl": "fases", "f_stars": "por fase", "f_world": "mundos",
  "see_page": "VER PÁGINA", "priv_btn": "POLÍTICA DE PRIVACIDADE", "get": "BAIXAR",
  "a_eyebrow": "Sobre", "a_title": "O estúdio",
  "a_h1": "Quem faz",
  "a_p1": "Lord Lima é o estúdio de Gabriel, desenvolvedor de jogos. Cada projeto é desenhado, programado e publicado por uma pessoa só, do primeiro sprite à versão da loja.",
  "a_h2": "Como trabalha",
  "a_l": ["Unity 6, foco em Android", "Pixel art e interface legível", "Jogos em português, inglês e espanhol", "Política de privacidade clara em cada app"],
  "more_about": "CONHECER O ESTÚDIO",
  "c_eyebrow": "Contato", "c_title": "Vamos conversar", "c_p": "Suporte, parcerias e imprensa.",
  "c_play": "Todos os jogos na Google Play",
  "home_nav": "Início",
  "rights": "© 2026 Lord Lima Studio",
  "games_title": "Jogos | Lord Lima Studio",
  "games_desc": "Jogos mobile do Lord Lima Studio: Ricochet Rescue e Oops Potion.",
  "about_title": "O estúdio | Lord Lima Studio",
  "about_desc": "Lord Lima é um estúdio indie de jogos mobile. Conheça quem faz e como os jogos são feitos.",
  "about_lead": "Um estúdio de uma pessoa só, com foco em jogos de celular curtos e bem acabados.",
  "about_h3": "Ferramentas", "about_p3": "Os jogos são feitos em Unity 6 para Android, com arte em pixel art criada no Aseprite. Os anúncios usam Unity LevelPlay e o progresso online usa Firebase e Google Play Games.",
  "contact_title": "Contato | Lord Lima Studio",
  "contact_desc": "Fale com o Lord Lima Studio: suporte, parcerias e imprensa.",
  "contact_lead": "Para suporte aos jogos, parcerias ou imprensa, escreva para o e-mail abaixo.",
  "priv_title": "Políticas de privacidade | Lord Lima Studio",
  "priv_desc": "Políticas de privacidade dos apps do Lord Lima Studio.",
  "priv_h": "Políticas de privacidade",
  "priv_lead": "Cada app tem a sua política. Escolha o app abaixo.",
  "open": "ABRIR",
  "r_title": "Ricochet Rescue | Lord Lima Studio",
  "r_desc": "Ricochet Rescue: salve os reféns no Velho Oeste com balas que ricocheteiam. 66 fases para Android.",
  "r_lead": "Salve os reféns no Velho Oeste.",
  "r_h1": "Como se joga",
  "r_p1": "Segure, arraste e solte para mirar. A bala atravessa corda, amigo e inimigo e só é parada por superfícies, então vale usar as paredes e ricochetear. Solte todos os amigos e derrube todos os inimigos para passar de fase. Se o cowboy ou um amigo morrer, o tempo acabar ou as balas acabarem, a fase é perdida.",
  "r_h2": "O que tem no jogo",
  "r_l": ["66 fases em dois mundos: Faroeste I e Faroeste II (Ferrovia, Pântano e Gelo)", "Três estrelas por fase, de acordo com as balas usadas", "Munições especiais, baús e loja", "Fases bônus de tiro às garrafas e de caça ao pato", "Inimigos que atiram, plataformas móveis, barris de pólvora, escudos e chefes", "Textos em português, inglês e espanhol"],
  "side_h": "Ficha do jogo", "side_plat": "Plataforma", "side_eng": "Motor", "side_price": "Preço", "side_free": "Grátis, com anúncios e opção sem anúncios",
  "video_alt": "Vídeo do Ricochet Rescue: cowboy dançando",
  "o_title": "Oops Potion | Lord Lima Studio",
  "o_desc": "Oops Potion: misture ingredientes, acerte as doses e descubra os efeitos de 40 receitas de poção.",
  "o_lead": "Misture, acerte, descubra!",
  "o_h1": "Como se joga",
  "o_p1": "Escolha até 4 ingredientes diferentes, despeje os líquidos e jogue os sólidos no caldeirão, depois mexa por 5 segundos. Se a combinação estiver certa, a poção é descoberta e a qualidade, de 0 a 100%, depende de quão perto você chegou das doses. Se estiver errada, o jogo dá uma dica sobre o que faltou. Cuidado com os ingredientes explosivos: mexer demais faz o caldeirão explodir.",
  "o_h2": "O que tem no jogo",
  "o_l": ["40 receitas, de Comum a Épica, para registrar no seu livro", "17 efeitos que você só descobre bebendo: chifres, asas, chamas no chapéu, cabelo arco-íris", "Receitas em que a ordem dos ingredientes importa", "Qualidade em quatro faixas, de Poção Rala a Poção Perfeita", "Moedas pela qualidade da poção e loja de ingredientes"],
  "o_status": "Em desenvolvimento",
  "side_status": "Situação",
  "nf_title": "Página não encontrada | Lord Lima Studio",
  "nf_h": "Página não encontrada", "nf_p": "O endereço não existe ou foi movido.", "nf_btn": "VOLTAR AO INÍCIO",
 },
 "en": {
  "html": "en", "other": "PT", "otherlabel": "Português",
  "nav_games": "Games", "nav_about": "Studio", "nav_contact": "Contact", "nav_priv": "Privacy",
  "skip": "Skip to content",
  "tagline": "Small games, made with care",
  "home_title": "Lord Lima Studio | Pixel art mobile games",
  "home_desc": "Indie studio making Android games in Unity, with pixel art and easy-to-grasp mechanics. Ricochet Rescue and Oops Potion.",
  "h_eyebrow": "Indie mobile game studio",
  "h_title": "Small games, <em>made with care</em>.",
  "h_lead": "I build Android games in Unity, with pixel art, easy-to-grasp mechanics and a lot of personality.",
  "h_cta1": "SEE GAMES", "h_cta2": "GOOGLE PLAY",
  "mascot_alt": "Lord Lima Studio mascot: a green pea with a golden crown, sunglasses and a scepter",
  "g_eyebrow": "Catalog", "g_title": "Games",
  "g_lead": "Each game has its own page with description, images and a store link.",
  "oops_alt": "Oops Potion: Mix, nail it, discover!",
  "rico_alt": "Ricochet Rescue: Aim. Ricochet. Rescue.",
  "chip_dev": "IN DEVELOPMENT", "chip_play": "GOOGLE PLAY",
  "oops_short": "Pick the ingredients, nail the doses and stir the cauldron. Every potion has an effect you only discover by drinking it: horns, wings, a burning hat. Fill the book with 40 recipes.",
  "rico_short": "Aim. Ricochet. Rescue. One cowboy, one gun and bullets that bounce: cut the rope, save the hostages and take down the outlaws in the Wild West. 66 levels, special ammo and duck-hunt bonus levels.",
  "f_rec": "recipes", "f_eff": "effects", "f_ing": "ingredients per mix",
  "f_lvl": "levels", "f_stars": "per level", "f_world": "worlds",
  "see_page": "VIEW PAGE", "priv_btn": "PRIVACY POLICY", "get": "GET IT",
  "a_eyebrow": "About", "a_title": "The studio",
  "a_h1": "Who makes it",
  "a_p1": "Lord Lima is Gabriel's game development studio. Each project is designed, programmed and published by one person, from the first sprite to the store release.",
  "a_h2": "How it works",
  "a_l": ["Unity 6, Android first", "Pixel art and readable UI", "Games in Portuguese, English and Spanish", "A clear privacy policy for every app"],
  "more_about": "ABOUT THE STUDIO",
  "c_eyebrow": "Contact", "c_title": "Let's talk", "c_p": "Support, partnerships and press.",
  "c_play": "All games on Google Play",
  "home_nav": "Home",
  "rights": "© 2026 Lord Lima Studio",
  "games_title": "Games | Lord Lima Studio",
  "games_desc": "Mobile games by Lord Lima Studio: Ricochet Rescue and Oops Potion.",
  "about_title": "The studio | Lord Lima Studio",
  "about_desc": "Lord Lima is an indie mobile game studio. Meet who makes the games and how they are built.",
  "about_lead": "A one-person studio focused on short, polished mobile games.",
  "about_h3": "Tools", "about_p3": "Games are made in Unity 6 for Android, with pixel art created in Aseprite. Ads use Unity LevelPlay and online progress uses Firebase and Google Play Games.",
  "contact_title": "Contact | Lord Lima Studio",
  "contact_desc": "Get in touch with Lord Lima Studio: support, partnerships and press.",
  "contact_lead": "For game support, partnerships or press, write to the e-mail below.",
  "priv_title": "Privacy policies | Lord Lima Studio",
  "priv_desc": "Privacy policies for Lord Lima Studio apps.",
  "priv_h": "Privacy policies",
  "priv_lead": "Each app has its own policy. Pick the app below.",
  "open": "OPEN",
  "r_title": "Ricochet Rescue | Lord Lima Studio",
  "r_desc": "Ricochet Rescue: save the hostages in the Wild West with bouncing bullets. 66 levels for Android.",
  "r_lead": "Save the hostages in the Wild West.",
  "r_h1": "How to play",
  "r_p1": "Hold, drag and release to aim. The bullet passes through ropes, friends and enemies and is only stopped by surfaces, so use the walls and bounce your shots. Free every friend and take down every enemy to clear a level. If the cowboy or a friend dies, or time or bullets run out, the level is lost.",
  "r_h2": "What is in the game",
  "r_l": ["66 levels in two worlds: Wild West I and Wild West II (Railroad, Swamp and Ice)", "Three stars per level, based on bullets used", "Special ammo, chests and a shop", "Bonus levels with bottle shooting and duck hunting", "Shooting enemies, moving platforms, powder barrels, shields and bosses", "Text in Portuguese, English and Spanish"],
  "side_h": "Game facts", "side_plat": "Platform", "side_eng": "Engine", "side_price": "Price", "side_free": "Free, with ads and an ad-free option",
  "video_alt": "Ricochet Rescue video: dancing cowboy",
  "o_title": "Oops Potion | Lord Lima Studio",
  "o_desc": "Oops Potion: mix ingredients, nail the doses and discover the effects of 40 potion recipes.",
  "o_lead": "Mix, nail it, discover!",
  "o_h1": "How to play",
  "o_p1": "Pick up to 4 different ingredients, pour the liquids and throw the solids into the cauldron, then stir for 5 seconds. If the combination is right the potion is discovered, and its quality, from 0 to 100%, depends on how close you got to the doses. If it is wrong, the game gives a hint about what is missing. Watch out for explosive ingredients: stir too long and the cauldron blows up.",
  "o_h2": "What is in the game",
  "o_l": ["40 recipes, from Common to Epic, to record in your book", "17 effects you only find out by drinking: horns, wings, a burning hat, rainbow hair", "Recipes where ingredient order matters", "Quality in four tiers, from Weak Potion to Perfect Potion", "Coins for potion quality and an ingredient shop"],
  "o_status": "In development",
  "side_status": "Status",
  "nf_title": "Page not found | Lord Lima Studio",
  "nf_h": "Page not found", "nf_p": "This address does not exist or was moved.", "nf_btn": "BACK TO HOME",
 },
}

def url(lang, p):
    return p if lang == "pt" else "/en" + p

def out_path(lang, p):
    base = ROOT if lang == "pt" else os.path.join(ROOT, "en")
    return os.path.join(base, p.strip("/"), "index.html") if p != "/" else os.path.join(base, "index.html")

def e(s):
    return html.escape(s, quote=True)

def head(lang, p, title, desc, og="/assets/img/og.jpg"):
    t = S[lang]
    alt = "en" if lang == "pt" else "pt"
    return f"""<!doctype html>
<html lang="{t['html']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#150c2b">
<link rel="canonical" href="{DOMAIN}{url(lang, p)}">
<link rel="alternate" hreflang="pt-BR" href="{DOMAIN}{url('pt', p)}">
<link rel="alternate" hreflang="en" href="{DOMAIN}{url('en', p)}">
<link rel="alternate" hreflang="x-default" href="{DOMAIN}{url('pt', p)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Lord Lima Studio">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{DOMAIN}{url(lang, p)}">
<meta property="og:image" content="{DOMAIN}{og}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/assets/img/favicon.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Pixelify+Sans:wght@500;700&family=Press+Start+2P&display=swap">
<link rel="stylesheet" href="/assets/css/site.css">
</head>
<body>
<a class="skip" href="#main">{e(t['skip'])}</a>
<canvas id="sky" aria-hidden="true"></canvas>
<div class="wrap">
"""

def nav(lang, p):
    t = S[lang]
    alt = "en" if lang == "pt" else "pt"
    def a(href, label, match):
        cur = ' aria-current="page"' if p.startswith(match) and (match != "/" or p == "/") else ""
        return f'<li><a href="{url(lang, href)}"{cur}>{e(label)}</a></li>'
    return f"""<nav class="site" aria-label="Principal">
  <a class="brand" href="{url(lang, '/')}"><img src="/assets/img/logo.png" alt="" width="44" height="44">Lord Lima Studio</a>
  <ul>
    {a('/games/', t['nav_games'], '/games/')}
    {a('/about/', t['nav_about'], '/about/')}
    {a('/contact/', t['nav_contact'], '/contact/')}
    {a('/privacy/', t['nav_priv'], '/privacy/')}
    <li><a class="lang" href="{url(alt, p)}" hreflang="{ 'en' if alt == 'en' else 'pt-BR'}" lang="{ 'en' if alt == 'en' else 'pt-BR'}" aria-label="{e(t['otherlabel'])}">{t['other']}</a></li>
  </ul>
</nav>
<main id="main">
"""

def foot(lang):
    t = S[lang]
    return f"""</main>
<footer>
  <span>{t['rights']} · lordlimastudio.com · <a href="{DEV}" target="_blank" rel="noopener">Google Play</a></span>
  <span>{e(t['nav_priv'])}: <a href="{PRIV['rico']}" target="_blank" rel="noopener">Ricochet Rescue</a> · <a href="{PRIV['oops']}" target="_blank" rel="noopener">Oops Potion</a> · <a href="{PRIV['loteco']}" target="_blank" rel="noopener">Loteco</a></span>
</footer>
</div>
<script src="/assets/js/site.js" defer></script>
</body>
</html>
"""

def facts(items):
    return '<ul class="facts">' + "".join(f"<li><b>{b}</b><span>{e(s)}</span></li>" for b, s in items) + "</ul>"

def card_oops(lang, rev=False):
    t = S[lang]
    return f"""<article class="game px">
    <a class="shot" href="{url(lang, '/games/oops-potion/')}"><img src="/assets/img/games/oops-{lang}.png" alt="{e(t['oops_alt'])}" width="1024" height="500" loading="lazy"></a>
    <div>
      <span class="chip soon">{t['chip_dev']}</span>
      <h3>Oops Potion</h3>
      <p>{e(t['oops_short'])}</p>
      {facts([('40', t['f_rec']), ('17', t['f_eff']), ('4', t['f_ing'])])}
      <div class="btns"><a class="btn" href="{url(lang, '/games/oops-potion/')}">{t['see_page']}</a><a class="btn alt" href="{PRIV['oops']}" target="_blank" rel="noopener">{t['priv_btn']}</a></div>
    </div>
  </article>"""

def card_rico(lang):
    t = S[lang]
    return f"""<article class="game px rev">
    <div>
      <span class="chip">{t['chip_play']}</span>
      <h3>Ricochet Rescue</h3>
      <p>{e(t['rico_short'])}</p>
      {facts([('66', t['f_lvl']), ('★★★', t['f_stars']), ('2', t['f_world'])])}
      <div class="btns"><a class="btn" href="{url(lang, '/games/ricochet-rescue/')}">{t['see_page']}</a><a class="btn alt" href="{RICO_PLAY}" target="_blank" rel="noopener">{t['get']}</a><a class="btn alt" href="{PRIV['rico']}" target="_blank" rel="noopener">{t['priv_btn']}</a></div>
    </div>
    <a class="shot" href="{url(lang, '/games/ricochet-rescue/')}"><img src="/assets/img/games/rico-{lang}.png" alt="{e(t['rico_alt'])}" width="1024" height="500" loading="lazy"></a>
  </article>"""

def about_block(lang):
    t = S[lang]
    lis = "".join(f"<li>{e(x)}</li>" for x in t['a_l'])
    return f"""<div class="about">
    <div class="card px"><h3>{t['a_h1']}</h3><p>{e(t['a_p1'])}</p></div>
    <div class="card px"><h3>{t['a_h2']}</h3><ul>{lis}</ul></div>
  </div>"""

def contact_block(lang):
    t = S[lang]
    return f"""<div class="contact px">
    <span class="eyebrow">{t['c_eyebrow']}</span>
    <h2 style="margin-top:10px">{t['c_title']}</h2>
    <a class="mail" href="mailto:{EMAIL}">{EMAIL}</a>
    <p>{e(t['c_p'])}</p>
    <p><a href="{DEV}" target="_blank" rel="noopener">{e(t['c_play'])}</a></p>
  </div>"""

def page_home(lang):
    t = S[lang]
    return head(lang, "/", t['home_title'], t['home_desc']) + nav(lang, "/") + f"""<header class="hero">
  <div>
    <span class="eyebrow">{t['h_eyebrow']}</span>
    <h1>{t['h_title']}</h1>
    <p class="lead">{e(t['h_lead'])}</p>
    <div class="btns">
      <a class="btn" href="#games">{t['h_cta1']}</a>
      <a class="btn alt" href="{DEV}" target="_blank" rel="noopener">{t['h_cta2']}</a>
    </div>
  </div>
  <div class="mascot"><img src="/assets/img/logo.png" alt="{e(t['mascot_alt'])}" width="512" height="512"></div>
</header>
<canvas class="grass" id="grass" aria-hidden="true"></canvas>

<section id="games">
  <div class="sec-h">
    <span class="eyebrow">{t['g_eyebrow']}</span>
    <h2>{t['g_title']}</h2>
    <p>{e(t['g_lead'])}</p>
  </div>
  {card_oops(lang)}
  {card_rico(lang)}
</section>

<section id="about">
  <div class="sec-h"><span class="eyebrow">{t['a_eyebrow']}</span><h2>{t['a_title']}</h2></div>
  {about_block(lang)}
  <p style="margin-top:32px"><a class="btn alt" href="{url(lang, '/about/')}">{t['more_about']}</a></p>
</section>

<section id="contact">
  {contact_block(lang)}
</section>
""" + foot(lang)

def page_games(lang):
    t = S[lang]
    return head(lang, "/games/", t['games_title'], t['games_desc']) + nav(lang, "/games/") + f"""<div class="page-h"><span class="eyebrow">{t['g_eyebrow']}</span><h1>{t['g_title']}</h1><p>{e(t['g_lead'])}</p></div>
<section style="padding-top:24px">
  {card_oops(lang)}
  {card_rico(lang)}
</section>
""" + foot(lang)

def crumbs(lang, name):
    t = S[lang]
    return f'<div class="crumbs"><a href="{url(lang, "/")}">{t["home_nav"]}</a> / <a href="{url(lang, "/games/")}">{t["nav_games"]}</a> / {name}</div>'

def lis(items):
    return "<ul>" + "".join(f"<li>{e(x)}</li>" for x in items) + "</ul>"

def page_rico(lang):
    t = S[lang]
    video = ""
    if lang == "pt":
        video = f"""<div class="side px" style="margin-top:32px"><div class="video shot"><video src="/assets/video/ricochet-promo.mp4" poster="/assets/video/ricochet-poster.jpg" controls muted loop playsinline preload="none" aria-label="{e(t['video_alt'])}"></video></div></div>"""
    return head(lang, "/games/ricochet-rescue/", t['r_title'], t['r_desc'], "/assets/img/og.jpg") + nav(lang, "/games/ricochet-rescue/") + f"""<div class="page-h">{crumbs(lang, 'Ricochet Rescue')}<span class="eyebrow">{t['chip_play']}</span><h1>Ricochet Rescue</h1><p>{e(t['r_lead'])}</p></div>
<div class="gp-hero"><div class="shot"><img src="/assets/img/games/rico-{lang}.png" alt="{e(t['rico_alt'])}" width="1024" height="500"></div></div>
<div class="btns" style="margin-top:24px"><a class="btn" href="{RICO_PLAY}" target="_blank" rel="noopener">{t['get']}</a><a class="btn alt" href="{PRIV['rico']}" target="_blank" rel="noopener">{t['priv_btn']}</a></div>
<div class="gp-grid">
  <div>
    <h2>{t['r_h1']}</h2><p>{e(t['r_p1'])}</p>
    <h2>{t['r_h2']}</h2>{lis(t['r_l'])}
  </div>
  <aside>
    <div class="side px"><h3>{t['side_h']}</h3>
      {facts([('66', t['f_lvl']), ('★★★', t['f_stars']), ('2', t['f_world'])])}
      <p><b>{t['side_plat']}:</b> Android<br><b>{t['side_eng']}:</b> Unity 6<br><b>{t['side_price']}:</b> {e(t['side_free'])}</p>
    </div>
    {video}
  </aside>
</div>
""" + foot(lang)

def page_oops(lang):
    t = S[lang]
    return head(lang, "/games/oops-potion/", t['o_title'], t['o_desc'], "/assets/img/og.jpg") + nav(lang, "/games/oops-potion/") + f"""<div class="page-h">{crumbs(lang, 'Oops Potion')}<span class="chip soon" style="align-self:flex-start">{t['chip_dev']}</span><h1>Oops Potion</h1><p>{e(t['o_lead'])}</p></div>
<div class="gp-hero"><div class="shot"><img src="/assets/img/games/oops-{lang}.png" alt="{e(t['oops_alt'])}" width="1024" height="500"></div></div>
<div class="btns" style="margin-top:24px"><a class="btn alt" href="{PRIV['oops']}" target="_blank" rel="noopener">{t['priv_btn']}</a></div>
<div class="gp-grid">
  <div>
    <h2>{t['o_h1']}</h2><p>{e(t['o_p1'])}</p>
    <h2>{t['o_h2']}</h2>{lis(t['o_l'])}
  </div>
  <aside>
    <div class="side px"><h3>{t['side_h']}</h3>
      {facts([('40', t['f_rec']), ('17', t['f_eff']), ('4', t['f_ing'])])}
      <p><b>{t['side_plat']}:</b> Android<br><b>{t['side_eng']}:</b> Unity 6<br><b>{t['side_status']}:</b> {t['o_status']}</p>
    </div>
  </aside>
</div>
""" + foot(lang)

def page_about(lang):
    t = S[lang]
    return head(lang, "/about/", t['about_title'], t['about_desc']) + nav(lang, "/about/") + f"""<div class="page-h"><span class="eyebrow">{t['a_eyebrow']}</span><h1>{t['a_title']}</h1><p>{e(t['about_lead'])}</p></div>
<section style="padding-top:24px">
  {about_block(lang)}
  <div class="about" style="margin-top:32px;grid-template-columns:1fr"><div class="card px"><h3>{t['about_h3']}</h3><p>{e(t['about_p3'])}</p></div></div>
</section>
""" + foot(lang)

def page_contact(lang):
    t = S[lang]
    return head(lang, "/contact/", t['contact_title'], t['contact_desc']) + nav(lang, "/contact/") + f"""<div class="page-h"><span class="eyebrow">{t['c_eyebrow']}</span><h1>{t['c_title']}</h1><p>{e(t['contact_lead'])}</p></div>
<section style="padding-top:24px">
  {contact_block(lang)}
</section>
""" + foot(lang)

def page_privacy(lang):
    t = S[lang]
    items = [("Ricochet Rescue", PRIV['rico']), ("Oops Potion", PRIV['oops']), ("Loteco", PRIV['loteco'])]
    lis_ = "".join(f'<li class="px"><div><strong>{n}</strong></div><a class="btn" href="{u}" target="_blank" rel="noopener">{t["open"]}</a></li>' for n, u in items)
    return head(lang, "/privacy/", t['priv_title'], t['priv_desc']) + nav(lang, "/privacy/") + f"""<div class="page-h"><span class="eyebrow">{t['nav_priv']}</span><h1>{t['priv_h']}</h1><p>{e(t['priv_lead'])}</p></div>
<section style="padding-top:24px"><ul class="plist">{lis_}</ul></section>
""" + foot(lang)

def page_404():
    t = S['pt']
    h = head('pt', '/', t['nf_title'], t['nf_p']).replace('<link rel="canonical"', '<meta name="robots" content="noindex">\n<link rel="canonical"')
    return h + nav('pt', '/404') + f"""<section style="text-align:center"><span class="eyebrow">404</span><h1 style="margin:14px 0">{t['nf_h']}</h1><p style="color:var(--muted)">{t['nf_p']} / This page does not exist.</p><p><a class="btn" href="/">{t['nf_btn']}</a></p></section>
""" + foot('pt')

BUILD = {"/": page_home, "/games/": page_games, "/games/ricochet-rescue/": page_rico,
         "/games/oops-potion/": page_oops, "/about/": page_about, "/contact/": page_contact, "/privacy/": page_privacy}

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

for lang in ("pt", "en"):
    for p in PAGES:
        write(out_path(lang, p), BUILD[p](lang))
write(os.path.join(ROOT, "404.html"), page_404())

# sitemap e robots
urls = []
for p in PAGES:
    for lang in ("pt", "en"):
        urls.append(f"""  <url><loc>{DOMAIN}{url(lang, p)}</loc>
    <xhtml:link rel="alternate" hreflang="pt-BR" href="{DOMAIN}{url('pt', p)}"/>
    <xhtml:link rel="alternate" hreflang="en" href="{DOMAIN}{url('en', p)}"/>
  </url>""")
write(os.path.join(ROOT, "sitemap.xml"), '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")
write(os.path.join(ROOT, "robots.txt"), f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n")
print("ok", len(PAGES) * 2 + 1, "páginas")
