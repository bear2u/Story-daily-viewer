#!/usr/bin/env python3
"""Build a plain HTML blog from content/*.json and matching Markdown files."""
from pathlib import Path
import json,re,html,sys,datetime
import markdown

ROOT=Path(__file__).resolve().parents[1]
BASE='https://bear2u.github.io/Story-daily-viewer/'
escape=html.escape

def shell(title,description,body,prefix='',canonical='',cover='assets/posts/generative-agents/cover.webp'):
    return f'''<!doctype html><html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{escape(description,quote=True)}">
<meta name="theme-color" content="#faf9f6">
<meta property="og:title" content="{escape(title,quote=True)}">
<meta property="og:description" content="{escape(description,quote=True)}">
<meta property="og:type" content="article">
<meta property="og:image" content="{BASE}{cover}">
<title>{escape(title)} · Story Daily</title>
<link rel="canonical" href="{BASE}{canonical}">
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{prefix}assets/site.css">
<link rel="alternate" type="application/rss+xml" title="Story Daily" href="{prefix}feed.xml">
<script src="{prefix}assets/site.js" defer></script></head><body>
<a class="skip" href="#main">본문으로 건너뛰기</a>
<header class="site-header"><div class="header-inner"><a class="brand" href="{prefix}index.html"><span class="brand-mark" aria-hidden="true">s</span>Story Daily<small>하루 한 편의 발견</small></a><nav class="header-nav" aria-label="주 메뉴"><a href="{prefix}index.html#archive">모든 글</a><a href="https://github.com/bear2u/Story-daily-viewer" target="_blank" rel="noopener">GitHub ↗</a></nav></div></header>
{body}
<footer class="site-footer"><div>Story Daily · 호기심이 이어지는 기록<br>논문과 이야기, 쉽게 읽고 오래 기억하기.</div><div><a href="{prefix}feed.xml">RSS 구독</a> &nbsp; · &nbsp; <a href="https://github.com/bear2u/Story-daily-viewer">소스 코드 ↗</a></div></footer>
</body></html>'''

def render_parts(post):
    raw=(ROOT/'content'/post['markdown']).read_text()
    raw=re.sub(r'<!--.*?-->','',raw,flags=re.S)
    raw=re.sub(r'^# .+\n','',raw,count=1)
    parts=[p.strip() for p in re.split(r'^---\s*$',raw,flags=re.M) if p.strip()]
    blocks=[]
    for i,part in enumerate(parts):
        rendered=markdown.markdown(part,extensions=['nl2br','tables','sane_lists'])
        def figure(match):
            alt=html.unescape(match.group(1));src=html.unescape(match.group(2))
            return f'<figure><button class="figure-button" type="button" data-zoom aria-label="그림 크게 보기: {escape(alt,quote=True)}"><img src="../{escape(src,quote=True)}" alt="{escape(alt,quote=True)}" loading="lazy" decoding="async"></button><figcaption>{escape(alt)}</figcaption><div class="zoom-hint">그림을 누르면 크게 볼 수 있음 ↗</div></figure>'
        rendered=re.sub(r'<p>\s*<img alt="([^"]*)" src="([^"]+)"\s*/?>\s*</p>',figure,rendered)
        rendered=re.sub(r'<a href="(https?://[^"]+)"',r'<a target="_blank" rel="noopener" href="\1"',rendered)
        blocks.append(f'<section class="part" id="part-{i+1}">{rendered}</section>')
    return '\n'.join(blocks),len(parts)

def article(post):
    parts,count=render_parts(post)
    chapters=post['chapters']
    toc=''.join(f'<a href="#part-{i+1}">{escape(label)}</a>' for i,label in enumerate(chapters))
    tags=''.join(f'<span class="pill">{escape(t)}</span>' for t in post['tags'])
    attribution = f'<a href="../{escape(post["attribution_url"],quote=True)}">그림 출처·이용 조건 ↗</a>' if post.get('attribution_url') else ''
    body=f'''<div class="reading-progress" aria-hidden="true"></div>
<main id="main"><div class="article-heading"><a class="back-link" href="../index.html#archive">← 모든 글로 돌아가기</a><div class="meta">{tags}<span>·</span><time datetime="{post['date']}">{post['date'].replace('-','. ')}</time><span>·</span><span>{post['reading_minutes']}분 읽기</span></div>
<h1>{escape(post['title'])}</h1><p class="lead">{escape(post['excerpt'])}</p>
<div class="article-details"><strong>{escape(post['paper_title'])}</strong><br>{escape(post['authors'])} · {escape(post['paper_year'])} · {escape(post['venue'])}<br>원문 그림과 함께 읽는 {count}파트 해설 · 판본 및 출처 확인: {post['verified_date']}</div></div>
<div class="article-layout"><aside class="toc" aria-label="글 목차"><p class="toc-title">이 글의 흐름</p>{toc}</aside><article class="article-body">{parts}<div class="article-end"><div class="source-links">{attribution}<a href="{post['source_url']}" target="_blank" rel="noopener">논문 원문 ↗</a><a href="../galleries/{post['slug']}.html">이미지로 보기 →</a><a href="../index.html#archive">다른 글 보기 →</a></div><p>해설 속 논문 그림과 연구 결과의 권리는 각 원 저자에게 있습니다. 그림은 연구 내용을 설명하기 위해 출처와 함께 수록했습니다.</p></div></article></div></main>
<button class="top-button" type="button" data-top hidden>맨 위로 ↑</button><dialog class="image-dialog" aria-label="논문 그림 확대"><button class="dialog-close" type="button">닫기 ×</button><img src="" alt=""><p class="dialog-caption"></p></dialog>'''
    return shell(post['title'],post['excerpt'],body,'../',f"posts/{post['slug']}.html",post['cover'])

def homepage(posts):
    p=posts[0]
    tags=sorted({t for p in posts for t in p['tags']})
    filters='<button type="button" class="filter" data-filter="all" aria-pressed="true">전체</button>'+''.join(f'<button type="button" class="filter" data-filter="{escape(t,quote=True)}" aria-pressed="false">{escape(t)}</button>' for t in tags)
    cards=[]
    for post in posts:
        search=' '.join([post['title'],post['excerpt'],post['paper_title'],*post['tags']])
        cards.append(f'''<a class="story-card" data-story data-tags="{escape('|'.join(post['tags']),quote=True)}" data-search="{escape(search,quote=True)}" href="posts/{post['slug']}.html"><div class="card-image"><img src="{post['cover']}" alt="{escape(post['cover_alt'],quote=True)}" loading="lazy"></div><div class="card-copy"><span class="pill">{escape(post['tags'][0])}</span><h3>{escape(post['title'])}</h3><p>{escape(post['excerpt'])}</p><div class="card-bottom"><time datetime="{post['date']}">{post['date'].replace('-','. ')}</time><span>{post['reading_minutes']}분 읽기 ↗</span></div></div></a>''')
    body=f'''<main class="page" id="main"><section class="intro"><div><div class="eyebrow">THE DAILY CURIOSITY</div><h1>매일 한 편,<br><span>호기심을 깨우는</span> 이야기.</h1><p>재미있는 논문을 원문 그림과 함께 읽습니다.<br>낯선 연구가 익숙한 이야기로 이어지는 곳.</p></div><div class="issue-count"><strong>{len(posts):02d}</strong>편의 발견이 쌓였어요</div></section>
<a class="feature" href="posts/{p['slug']}.html"><div class="feature-art"><span class="image-label">INSIDE THE PAPER</span><img src="{p['cover']}" alt="{escape(p['cover_alt'],quote=True)}" fetchpriority="high"></div><div class="feature-copy"><div class="meta"><span class="pill">최근 이야기</span><time datetime="{p['date']}">{p['date'].replace('-','. ')}</time><span>· {p['reading_minutes']}분 읽기</span></div><h2>{escape(p['title'])}</h2><p class="excerpt">{escape(p['excerpt'])}</p><span class="read-link">이야기 읽기 <span aria-hidden="true">⟶</span></span></div></a>
<section class="archive" id="archive"><div class="archive-top"><h2 class="archive-title">모아 둔 이야기 <span style="color:var(--muted);font-size:14px;font-weight:400" data-visible-count>{len(posts)}</span></h2><label class="search-box"><span aria-hidden="true">⌕</span><input type="search" placeholder="제목, 논문, 주제 검색" aria-label="글 검색" data-search></label></div><div class="filters" aria-label="주제 필터">{filters}</div><div class="story-grid">{''.join(cards)}</div><div class="empty" data-empty role="status" hidden>검색 결과가 없어요.<br>다른 키워드로 찾아보세요.<button type="button" data-reset>전체 글 보기</button></div></section></main>'''
    return shell('매일 한 편의 발견','재미있는 논문과 이야기를 원문 그림과 함께 읽는 Story Daily.',body,cover=p['cover'])

def main():
    posts=[json.loads(p.read_text()) for p in (ROOT/'content').glob('*.json')]
    posts.sort(key=lambda p:(p.get('published_at',p['date']),p['slug']),reverse=True)
    if not posts: raise SystemExit('No posts found')
    (ROOT/'posts').mkdir(exist_ok=True)
    for post in posts:
        page=article(post)
        (ROOT/'posts'/f"{post['slug']}.html").write_text(page)
    (ROOT/'index.html').write_text(homepage(posts))
    (ROOT/'posts.json').write_text(json.dumps(posts,ensure_ascii=False,indent=2))
    items=''.join(f"<item><title>{escape(p['title'])}</title><link>{BASE}posts/{p['slug']}.html</link><guid>{BASE}posts/{p['slug']}.html</guid><description>{escape(p['excerpt'])}</description><pubDate>{datetime.datetime.fromisoformat(p['date']).strftime('%a, %d %b %Y')} 00:00:00 +0900</pubDate></item>" for p in posts)
    (ROOT/'feed.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>Story Daily</title><link>{BASE}</link><description>매일 한 편의 발견</description><language>ko</language>{items}</channel></rss>')
    urls=[BASE]+[f"{BASE}posts/{p['slug']}.html" for p in posts]
    (ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{u}</loc></url>' for u in urls)+'</urlset>')
    (ROOT/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n')
    print(f'Built {len(posts)} post(s).')

if __name__=='__main__':main()
