"""Ensure the professional portfolio stays complete and accurately linked."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO = ROOT / "portfolio.html"
ACCOUNT = "kanizfatemar0xy"
PROJECT_NAMES = (
    "Bitcoin Volatility Forecasting",
    "Fuzzy Password Strength Checker",
    "WanderGallery",
    "Travel With Me",
    "London Weather",
    "GridWorld Q-Learning",
)
REPOS = (
    "Bitcoin_dissertation",
    "-Fuzzy-Logic-and-Neural-Networks",
    "travel-website-project",
    "travel-website",
    "London-Weather-Data-Science",
    "GridWorld-Q-Learning",
)

class ProjectParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.project_ids = []
        self.links = []
        self.page_ids = set()
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.page_ids.add(a["id"])
        if tag == "article" and a.get("id", "").startswith("p0"):
            self.project_ids.append(a["id"])
        if tag == "a":
            self.links.append(a.get("href", ""))

class PortfolioChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = PORTFOLIO.read_text(encoding="utf-8")
        cls.html = ProjectParser()
        cls.html.feed(cls.text)

    def test_projects_are_numbered_in_order(self):
        self.assertEqual(self.html.project_ids, ["p01", "p02", "p03", "p04", "p05", "p06"])

    def test_dedicated_repository_links_exist(self):
        for repo in REPOS:
            with self.subTest(repo=repo):
                self.assertIn(f"https://github.com/{ACCOUNT}/{repo}", self.html.links)

    def test_all_navigation_anchors_exist(self):
        for link in self.html.links:
            if link.startswith("#"):
                with self.subTest(anchor=link):
                    self.assertIn(link[1:], self.html.page_ids)

    def test_page_has_contact_and_realistic_scope(self):
        self.assertIn("linkedin.com/in/kaniz-fatema-roxy", self.text)
        self.assertIn("real-data model results remain unverified", self.text)
        self.assertIn("Private repository", self.text)
        self.assertEqual(len(re.findall(r'class="project-card"', self.text)), 6)

if __name__ == "__main__":
    unittest.main()
