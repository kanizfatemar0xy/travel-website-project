"""Local, dependency-free checks for the GitHub Pages site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import unittest

ROOT = Path(__file__).resolve().parents[1]

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.images = []
        self.ids = set()
        self.viewport = False
        self.lang = False
        self.password_input = False
        self.forms = []
    def handle_starttag(self, tag, attrs):
        props = dict(attrs)
        if tag == 'html':
            self.lang = bool(props.get('lang'))
        if tag == 'meta' and props.get('name') == 'viewport':
            self.viewport = True
        if 'id' in props:
            self.ids.add(props['id'])
        if tag == 'a':
            self.links.append(props.get('href', ''))
        if tag == 'img':
            self.images.append(props)
        if tag == 'input' and props.get('type', '').lower() == 'password':
            self.password_input = True
        if tag == 'form':
            self.forms.append(props)

class TestSite(unittest.TestCase):
    def test_html_navigation_and_assets(self):
        pages = list(ROOT.glob('*.html'))
        self.assertGreater(len(pages), 0)
        for page in pages:
            with self.subTest(page=page.name):
                parser = PageParser()
                parser.feed(page.read_text(encoding='utf-8'))
                self.assertTrue(parser.lang, 'missing html language')
                self.assertTrue(parser.viewport, 'missing mobile viewport')
                self.assertFalse(parser.password_input, 'static site must not collect passwords')
                for form in parser.forms:
                    self.assertNotEqual(form.get('method', '').lower(), 'post', 'no static POST backend')
                for image in parser.images:
                    self.assertTrue(image.get('alt'), f'missing image alt: {image}')
                    src = image.get('src', '')
                    if src and not src.startswith(('http:', 'https:', 'data:')):
                        self.assertTrue((page.parent / unquote(src.split('?', 1)[0])).is_file(), f'missing image {src}')
                for url in parser.links:
                    self.assertNotEqual(url, '#', 'placeholder navigation link')
                    self.assertTrue(url.strip(), 'empty href')
                    parsed = urlsplit(url)
                    if parsed.scheme or parsed.netloc or url.startswith(('mailto:', 'tel:')):
                        continue
                    target = (page.parent / unquote(parsed.path)).resolve() if parsed.path else page
                    self.assertTrue(target.is_file(), f'broken local href {url}')
                    if parsed.fragment and target.suffix == '.html':
                        other = PageParser()
                        other.feed(target.read_text(encoding='utf-8'))
                        self.assertIn(unquote(parsed.fragment), other.ids, f'missing anchor {url}')

if __name__ == '__main__':
    unittest.main()
