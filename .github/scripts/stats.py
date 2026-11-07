"""Gera dist/stats.svg com números do perfil, no mesmo visual do README.

Roda na GitHub Action usando o GITHUB_TOKEN; só lê dados públicos.
"""
import json
import os
import urllib.request
from html import escape

USER = os.environ.get("GH_USER", "HerbertyFreire")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
API = "https://api.github.com"

COLORS = {
    "Python": "#3572A5", "C": "#8b9cb3", "C++": "#f34b7d", "JavaScript": "#f1e05a",
    "TypeScript": "#3178c6", "HTML": "#e34c26", "CSS": "#663399", "Java": "#b07219",
    "Blade": "#f7523f", "PHP": "#4F5D95", "Shell": "#89e051", "TeX": "#3D6117",
}
FALLBACK = ["#5eead4", "#fbbf24", "#f472b6", "#a78bfa", "#60a5fa", "#fb923c"]


def get(path):
    req = urllib.request.Request(API + path, headers={
        "Accept": "application/vnd.github+json",
        **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def main():
    user = get(f"/users/{USER}")
    repos, page = [], 1
    while True:
        batch = get(f"/users/{USER}/repos?per_page=100&page={page}&type=owner")
        repos += batch
        if len(batch) < 100:
            break
        page += 1

    own = [r for r in repos if not r["fork"]]
    stars = sum(r["stargazers_count"] for r in own)
    langs = {}
    for r in repos:  # forks entram: são trabalhos de disciplina feitos por ele
        try:
            for lang, size in get(f"/repos/{USER}/{r['name']}/languages").items():
                langs[lang] = langs.get(lang, 0) + size
        except Exception:
            pass
    total = sum(langs.values()) or 1
    top = sorted(langs.items(), key=lambda kv: -kv[1])[:6]

    stats = [
        (str(user.get("public_repos", len(repos))), "repositórios"),
        (str(len(own)), "autorais"),
        (str(stars), "estrelas"),
        (str(user.get("followers", 0)), "seguidores"),
    ]

    W, H = 1200, 230
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Estatísticas de {escape(USER)} no GitHub">',
           '<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#07182a"/><stop offset="1" stop-color="#0b2738"/></linearGradient>',
           f'<clipPath id="f"><rect width="{W}" height="{H}" rx="22"/></clipPath>',
           '<style>.m{font-family:"JetBrains Mono",Consolas,"Courier New",monospace}.s{font-family:"Segoe UI",Inter,-apple-system,Helvetica,Arial,sans-serif}'
           '.g{transform-box:fill-box;transform-origin:left center;transform:scaleX(0);animation:g 1.3s cubic-bezier(.2,.8,.2,1) forwards}@keyframes g{to{transform:scaleX(1)}}'
           '.fd{opacity:0;animation:i .8s ease-out forwards}@keyframes i{to{opacity:1}}</style></defs>',
           '<g clip-path="url(#f)">', f'<rect width="{W}" height="{H}" fill="url(#bg)"/>',
           '<text class="m" x="56" y="54" font-size="14" fill="#5eead4" letter-spacing="2">GITHUB · EM NÚMEROS</text>']

    for i, (num, label) in enumerate(stats):
        x, y = 56 + (i % 2) * 186, 76 + (i // 2) * 72
        out.append(f'<g class="fd" style="animation-delay:{.1 + i * .12:.2f}s" transform="translate({x} {y})">'
                   f'<rect width="170" height="60" rx="12" fill="#fff" fill-opacity=".04" stroke="#5eead4" stroke-opacity=".18"/>'
                   f'<text class="s" x="16" y="38" font-size="26" font-weight="800" fill="#f8fafc">{escape(num)}</text>'
                   f'<text class="s" x="154" y="37" text-anchor="end" font-size="13" fill="#94a3b8">{escape(label)}</text></g>')

    # barra empilhada de linguagens
    bx, by, bw = 470, 80, 674
    out.append(f'<text class="m" x="{bx}" y="54" font-size="14" fill="#94a3b8">linguagens mais usadas</text>')
    out.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="14" rx="7" fill="#fff" fill-opacity=".05"/>')
    out.append(f'<g class="g"><clipPath id="bar"><rect x="{bx}" y="{by}" width="{bw}" height="14" rx="7"/></clipPath><g clip-path="url(#bar)">')
    cx, shown = bx, sum(v for _, v in top) or 1
    fb = iter(FALLBACK)
    colors = {}
    for lang, size in top:
        colors[lang] = COLORS.get(lang) or next(fb, "#5eead4")
        w = bw * size / shown
        out.append(f'<rect x="{cx:.1f}" y="{by}" width="{w + .5:.1f}" height="14" fill="{colors[lang]}"/>')
        cx += w
    out.append('</g></g>')
    for i, (lang, size) in enumerate(top):
        x, y = bx + (i % 3) * 226, by + 48 + (i // 3) * 40
        out.append(f'<g class="fd" style="animation-delay:{.6 + i * .1:.2f}s"><circle cx="{x + 6}" cy="{y - 5}" r="6" fill="{colors[lang]}"/>'
                   f'<text class="s" x="{x + 20}" y="{y}" font-size="15" fill="#e2e8f0">{escape(lang)} '
                   f'<tspan class="m" fill="#94a3b8" font-size="13">{100 * size / total:.1f}%</tspan></text></g>')

    out.append('</g>')
    out.append(f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="21" fill="none" stroke="#5eead4" stroke-opacity=".18" stroke-width="2"/></svg>')

    OUT = os.environ.get("OUT_DIR", "dist")
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "stats.svg"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("ok:", stats, top)


if __name__ == "__main__":
    main()
