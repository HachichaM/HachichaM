"""Renders every README card from one palette. Run: GH_TOKEN=... python scripts/render_cards.py"""
import json, os, urllib.request, datetime as dt
from collections import defaultdict
from xml.sax.saxutils import escape as e

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'cards')
USER = 'HachichaM'
# Design system: ink / paper / one blue ramp. Every card uses only these.
INK, PAPER, LINE, LINE_D, MUT = '#111111', '#f3f3f1', '#e2e2de', '#3a3a3c', '#6e6e73'
BLUE, RAMP = '#2f55ff', ['#e2e2de', '#c8d3ff', '#94a8ff', '#6280ff', '#2f55ff', '#1a3be0']
MONO = "'Geist Mono',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
SANS = "Geist,system-ui,-apple-system,'Segoe UI',sans-serif"
SERIF = "'Instrument Serif',Georgia,serif"
FADE = ('.f{opacity:0;animation:in .6s ease-out forwards}.d1{animation-delay:.1s}.d2{animation-delay:.3s}.d3{animation-delay:.5s}'
        '.d4{animation-delay:.7s}@keyframes in{to{opacity:1}}.c{animation:b 1.1s steps(1) infinite}@keyframes b{50%{opacity:0}}'
        '@media (prefers-reduced-motion:reduce){.f{opacity:1;animation:none}.c{animation:none}}')
W, TW = 880, 293.333


def svg(w, h, title, body, style=''):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{e(title)}">'
            f'<title>{e(title)}</title><style>{style}</style>{body}</svg>\n')


def card(w, h, bg=PAPER, stroke=LINE):
    return f'<rect x="5" y="5" width="{w-10:.3f}" height="{h-10}" rx="14" fill="{bg}" stroke="{stroke}"/>'


def t(x, y, s, size=13, fill=INK, font=MONO, weight=400, extra=''):
    return f'<text x="{x}" y="{y}" font-family="{e(font)}" font-size="{size}" fill="{fill}" font-weight="{weight}" {extra}>{e(str(s))}</text>'


def write(name, content):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(content)


def hero():
    b = card(W, 300, INK, LINE_D) + f'<path d="M5 48H{W-5}" stroke="{LINE_D}"/>'
    b += ''.join(f'<circle cx="{28+i*16}" cy="27" r="4.5" fill="{c}"/>' for i, c in enumerate(RAMP[2:5]))
    b += t(W-26, 31, 'RESEARCH / PLATFORM / PRODUCT', 11, MUT, extra='text-anchor="end"')
    b += f'<g class="f d1">{t(28, 116, "Mohamed Hachicha", 54, PAPER, SERIF)}</g>'
    b += f'<g class="f d2">{t(30, 148, "FULL STACK DEVELOPER · PLATFORM ENGINEER · APPLIED AI RESEARCHER", 12, RAMP[2])}</g>'
    b += (f'<g class="f d3">{t(30, 194, "I build products businesses run on, the platforms that keep them up,", 16, PAPER, SANS)}'
          f'{t(30, 218, "and research that has to earn its conclusions.", 16, PAPER, SANS)}</g>')
    b += (f'<g class="f d4">{t(30, 266, "$ status", 12, MUT)}{t(100, 266, "shipping trena.pro + rovelo.fr", 12, PAPER)}'
          f'<rect class="c" x="333" y="255" width="8" height="14" fill="{BLUE}"/></g>')
    write('hero.svg', svg(W, 300, 'Mohamed Hachicha. Full stack developer, platform engineer and applied AI researcher.', b, FADE))


def pillars():
    for name, n, label, l1, l2, big, cap in [
            ('pillar-research.svg', '01', 'Research', 'Hybrid retrieval, optimizers,', 'evidence-gated AI agents.', '7', 'search algorithms'),
            ('pillar-platform.svg', '02', 'Platform', 'From repo to running service,', 'restore-tested recovery.', 'CI', 'gated releases'),
            ('pillar-product.svg', '03', 'Product', 'Software businesses run on:', 'web, mobile and desktop.', '2', 'products live')]:
        b = card(TW, 210) + t(26, 42, n, 11, MUT) + t(26, 82, label, 34, BLUE, SERIF)
        b += t(26, 116, l1, 13, INK, SANS) + t(26, 134, l2, 13, INK, SANS)
        b += f'<path d="M26 152H{TW-26:.3f}" stroke="{LINE}"/>' + t(26, 186, big, 26, INK, SERIF) + t(26 + 15 * len(big) + 10, 184, cap, 11, MUT)
        write(name, svg(f'{TW:.3f}', 210, f'{label}: {l1} {l2}', b))


def projects():
    for name, title, live, d1, d2, tags, foot in [
            ('project-trena.svg', 'Trena', True, 'Gym operations SaaS: members,', 'billing, access, mobile app.', 'Next.js · Flutter · Postgres', 'trena.pro'),
            ('project-rovelo.svg', 'Rovelo', True, 'Restaurant routines, schedules', 'and HACCP compliance.', 'Next.js · TypeScript · Redis', 'rovelo.fr'),
            ('project-validator.svg', 'Validator', False, 'MCP harness: typed evidence', 'graphs, validation gates.', 'MCP · Python · SQLite WAL', 'private research')]:
        status = 'LIVE' if live else 'PRIVATE'
        col, cw = (BLUE if live else MUT), 7 * len(status) + 28
        b = card(TW, 196) + t(26, 50, title, 28, INK, SERIF)
        b += f'<rect x="{TW-26-cw:.3f}" y="28" width="{cw}" height="22" rx="11" fill="none" stroke="{col}"/>'
        b += (f'<circle cx="{TW-26-cw+12:.3f}" cy="39" r="3" fill="{col}">'
              + ('<animate attributeName="opacity" values="1;.2;1" dur="2s" repeatCount="indefinite"/>' if live else '') + '</circle>')
        b += t(f'{TW-26-cw+21:.3f}', 43, status, 10, col)
        b += t(26, 88, d1, 13, INK, SANS) + t(26, 106, d2, 13, INK, SANS) + t(26, 136, tags, 10.5, MUT)
        b += f'<path d="M26 152H{TW-26:.3f}" stroke="{LINE}"/>' + t(26, 176, ('↗ ' if live else '◆ ') + foot, 11.5, col)
        write(name, svg(f'{TW:.3f}', 196, f'{title}: {d1} {d2}', b))


TITLES = {'building': ("What I'm building", ''), 'activity': ('Activity', 'refreshed daily'),
          'research': ('Research & systems', '01'), 'products': ('Products', '02'),
          'platform': ('Platform engineering', '03'), 'stack': ('Technologies', '04'), 'work': ('How I work', '05')}


def titles():
    for key, (label, tag) in TITLES.items():
        for mode, fg in (('light', INK), ('dark', PAPER)):
            b = (t(6, 44, label, 32, fg, SERIF) + t(874, 42, tag, 11, MUT, extra='text-anchor="end"')
                 + f'<path d="M6 58H874" stroke="{BLUE}" stroke-opacity=".5"/>')
            write(f'title-{key}-{mode}.svg', svg('880.000', 64, label, b))


def contributions():
    q = 'query($u:String!){user(login:$u){contributionsCollection{contributionCalendar{totalContributions weeks{contributionDays{date contributionCount}}}}}}'
    req = urllib.request.Request('https://api.github.com/graphql', json.dumps({'query': q, 'variables': {'u': USER}}).encode(),
                                 {'Authorization': f'bearer {os.environ["GH_TOKEN"]}', 'Content-Type': 'application/json'})
    cal = json.load(urllib.request.urlopen(req, timeout=30))['data']['user']['contributionsCollection']['contributionCalendar']
    return cal['totalContributions'], cal['weeks']


def level(c, top):
    return 0 if c == 0 else min(5, 1 + int(4 * c / max(top, 1)))


def heatmap(total, weeks):
    days = [d for w in weeks for d in w['contributionDays']]
    top = sorted(d['contributionCount'] for d in days)[int(len(days) * .95)] or 1
    cell, gap, x0, y0 = 12, 3, 46, 66
    b = card(W, 200) + t(26, 42, f'{total:,} contributions in the last year', 20, INK, SERIF)
    b += t(W-26, 40, '@' + USER, 11, MUT, extra='text-anchor="end"')
    for i, w in enumerate(weeks):
        for d in w['contributionDays']:
            r = dt.date.fromisoformat(d['date']).isoweekday() % 7
            b += (f'<rect x="{x0+i*(cell+gap)}" y="{y0+r*(cell+gap)}" width="{cell}" height="{cell}" rx="3" '
                  f'fill="{RAMP[level(d["contributionCount"], top)]}"><title>{d["date"]}: {d["contributionCount"]}</title></rect>')
    lx = W - 26 - 6 * 15 - 34
    b += t(lx - 8, 185, 'less', 10, MUT, extra='text-anchor="end"')
    b += ''.join(f'<rect x="{lx+i*15}" y="175" width="11" height="11" rx="3" fill="{c}"/>' for i, c in enumerate(RAMP))
    b += t(lx + 94, 185, 'more', 10, MUT)
    write('heatmap.svg', svg(W, 200, f'{total} GitHub contributions in the last year', b))


def stats(days):
    counts = [d['contributionCount'] for d in days]
    longest = cur = run = 0
    for c in counts:
        run = run + 1 if c else 0
        longest = max(longest, run)
    for c in reversed(counts[:-1] if counts and counts[-1] == 0 else counts):  # today may not be counted yet
        if not c:
            break
        cur += 1
    return cur, longest, max(days, key=lambda d: d['contributionCount'])


def activity(weeks):
    days = [d for w in weeks for d in w['contributionDays']]
    months = defaultdict(int)
    for d in days:
        months[d['date'][:7]] += d['contributionCount']
    keys = sorted(months)[-12:]
    top = max(months[k] for k in keys) or 1
    cur, longest, best = stats(days)
    b = card(W, 260) + t(26, 42, 'Contributions by month', 20, INK, SERIF)
    bw, gx, base, hmax = 34, 18, 214, 130
    for i, k in enumerate(keys):
        h, x = max(2, hmax * months[k] / top), 30 + i * (bw + gx)
        b += f'<rect x="{x}" y="{base-h:.1f}" width="{bw}" height="{h:.1f}" rx="5" fill="{BLUE if k == keys[-1] else RAMP[2]}"><title>{k}: {months[k]}</title></rect>'
        b += t(x + bw / 2, base + 18, dt.date.fromisoformat(k + '-01').strftime('%b'), 10, MUT, extra='text-anchor="middle"')
    sx = 30 + 12 * (bw + gx) + 10
    for j, (v, lab) in enumerate([(cur, 'day streak'), (longest, 'longest streak'),
                                  (best['contributionCount'], 'busiest day · ' + best['date'][5:])]):
        b += t(sx, 96 + j * 52, v, 28, INK, SERIF) + t(sx, 114 + j * 52, lab, 10, MUT)
    write('activity.svg', svg(W, 260, f'Contributions by month. Current streak {cur} days, longest {longest}.', b))


if __name__ == '__main__':
    assert stats([{'date': f'2026-01-0{i}', 'contributionCount': c} for i, c in enumerate([1, 0, 2, 3, 0], 1)])[:2] == (2, 2)
    os.makedirs(OUT, exist_ok=True)
    hero(); pillars(); projects(); titles()
    if os.environ.get('GH_TOKEN'):
        total, weeks = contributions()
        heatmap(total, weeks); activity(weeks)
    print('cards rendered')
