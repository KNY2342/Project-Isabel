from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / 'index.html').read_text(encoding='utf-8')
CSS = (ROOT / 'styles.css').read_text(encoding='utf-8')
JS = (ROOT / 'app.js').read_text(encoding='utf-8')

class Parser(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=set(); self.hrefs=[]; self.images=[]; self.forms=0; self.h1=0
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag=='a' and 'href' in a: self.hrefs.append(a['href'])
        if tag=='img': self.images.append(a)
        if tag=='form': self.forms += 1
        if tag=='h1': self.h1 += 1

class SiteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p=Parser(); cls.p.feed(HTML)
    def test_required_files(self):
        for path in ['index.html','styles.css','app.js','assets/favicon.svg','README.md','docs/PRIVACY.md','docs/LOCKED_PRINCIPLES.md']:
            self.assertTrue((ROOT/path).exists(), path)
    def test_single_h1(self): self.assertEqual(self.p.h1,1)
    def test_internal_anchors_resolve(self):
        for href in self.p.hrefs:
            if href.startswith('#') and len(href)>1: self.assertIn(href[1:],self.p.ids,href)
    def test_assets_resolve(self):
        for match in re.findall(r'(?:href|src)="([^"]+)"',HTML):
            if not match.startswith(('http','#','mailto:')): self.assertTrue((ROOT/match).exists(),match)
    def test_product_boundary(self):
        lowered=HTML.lower(); self.assertIn('does not place bets',lowered); self.assertIn('paper-test',lowered)
    def test_locked_decisions(self):
        for term in ['BET, WATCH, or REJECT','Probability over certainty','No signal is a valid signal']:
            self.assertIn(term,HTML)
    def test_form_is_explicit_demo(self):
        self.assertEqual(self.p.forms,1); self.assertIn('localStorage',JS); self.assertIn('stored only in this browser',HTML)
    def test_responsive_css(self):
        self.assertIn('@media(max-width:720px)',CSS); self.assertIn('prefers-reduced-motion',CSS)
    def test_accessibility_basics(self):
        for term in ['skip-link','aria-expanded','role="status"','autocomplete="email"']:
            self.assertIn(term,HTML)

if __name__=='__main__': unittest.main()
