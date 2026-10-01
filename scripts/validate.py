#!/usr/bin/env python3
"""Check generated pages for broken local links and malformed feeds."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import xml.etree.ElementTree as ET
import json

ROOT=Path(__file__).resolve().parents[1]
errors=[]

class Links(HTMLParser):
    def __init__(self,page):super().__init__();self.page=page
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        for key in ('src','href'):
            value=attrs.get(key,'')
            if not value or value.startswith(('#','data:','mailto:','tel:')):continue
            url=urlsplit(value)
            if url.scheme or url.netloc:continue
            path=unquote(url.path)
            if not path:continue
            target=(self.page.parent/path).resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                errors.append(f'{self.page.relative_to(ROOT)}: missing {value}')

def main():
    pages=[ROOT/'index.html',*sorted((ROOT/'posts').glob('*.html')),*sorted((ROOT/'galleries').glob('*.html'))]
    for page in pages:
        Links(page).feed(page.read_text())
    for name in ('feed.xml','sitemap.xml'):
        ET.parse(ROOT/name)
    posts=json.loads((ROOT/'posts.json').read_text())
    assert posts,'The blog has no posts'
    for post in posts:
        assert (ROOT/'posts'/f"{post['slug']}.html").exists(),post['slug']
        assert (ROOT/post['cover']).exists(),post['cover']
    if errors:raise SystemExit('\n'.join(errors))
    print(f'Validated {len(pages)} HTML pages, all local links, {len(posts)} post(s), RSS and sitemap.')

if __name__=='__main__':main()
