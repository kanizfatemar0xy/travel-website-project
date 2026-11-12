"""Verify the original clean portfolio layout, six projects, and privacy choices."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "portfolio.html").read_text(encoding="utf-8")
OWNER = "kanizfatemar0xy"
PUBLIC_REPOS = (
    "Bitcoin_dissertation",
    "-Fuzzy-Logic-and-Neural-Networks",
    "travel-website-project",
    "travel-website",
    "London-Weather-Data-Science",
    "GridWorld-Q-Learning",
)

class IndexParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.anchors = set()
        self.images = 0
        self.projects = 0
    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "id" in attributes:
            self.anchors.add(attributes["id"])
        if tag == "a":
            self.links.append(attributes.get("href", ""))
        if tag == "img":
            self.images += 1
        if tag == "article" and "project" in attributes.get("class", "").split():
            self.projects += 1

class PortfolioTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc = IndexParser()
        cls.doc.feed(HTML)

    def test_featured_numbering_stays_sequential(self):
        self.assertEqual(re.findall(r'<span class="label">([0-9][0-9]) ·', HTML),
                         ["01", "02", "03", "04", "05", "06"])

    def test_public_project_repository_links(self):
        for repo in PUBLIC_REPOS:
            with self.subTest(repo=repo):
                self.assertIn(f"https://github.com/{OWNER}/{repo}", self.doc.links)

    def test_no_profile_photograph_or_social_preview_image(self):
        self.assertEqual(self.doc.images, 0)
        self.assertNotIn("avatars.githubusercontent.com", HTML)
        self.assertNotIn('property="og:image"', HTML)

    def test_navigation_and_contact(self):
        for url in self.doc.links:
            if url.startswith("#"):
                self.assertIn(url[1:], self.doc.anchors)
        self.assertIn("linkedin.com/in/kaniz-fatema-roxy", HTML)
        self.assertIn("Private repository", HTML)
        self.assertEqual(self.doc.projects, 7)  # Six public + private Android project

    def test_project_limitations_are_retained(self):
        self.assertIn("final forecasting results", HTML)
        self.assertIn("benchmark passed on the fixed map", HTML)

if __name__ == "__main__":
    unittest.main()
