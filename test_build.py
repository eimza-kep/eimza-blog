import unittest
import os
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime, timezone
import build

class TestBlogBuild(unittest.TestCase):
    def test_content_posts_directory(self):
        posts_dir = Path("content") / "posts"
        self.assertTrue(posts_dir.exists())
        md_files = list(posts_dir.glob("*.md"))
        self.assertGreater(len(md_files), 10, "En az 10 markdown makale bulunmalı")

    def test_build_execution(self):
        try:
            build.generate_site()
        except Exception as e:
            self.fail(f"build.generate_site() hata fırlattı: {e}")

        dist_dir = Path("dist")
        self.assertTrue(dist_dir.exists())
        self.assertTrue((dist_dir / "index.html").exists())
        self.assertTrue((dist_dir / "hakkimizda.html").exists())
        self.assertTrue((dist_dir / "feed.xml").exists())
        self.assertTrue((dist_dir / "feed.json").exists())

    def test_slugify(self):
        self.assertEqual(build.slugify("İstanbul ve Çankaya Hukuk"), "istanbul-ve-cankaya-hukuk")
        self.assertEqual(build.slugify("E-İmza & KEP Rehberi 2026!"), "e-imza-kep-rehberi-2026")
        self.assertEqual(build.slugify("Mali Mühür ve e-Defter Çözümleri"), "mali-muhur-ve-e-defter-cozumleri")

    def test_format_rfc822(self):
        formatted = build.format_rfc822("2026-10-15")
        self.assertTrue("2026" in formatted)
        self.assertTrue("Oct" in formatted)

    def test_client_side_search_elements(self):
        index_file = Path("dist") / "index.html"
        self.assertTrue(index_file.exists())
        content = index_file.read_text(encoding="utf-8")
        
        # Verify Search Input and Buttons
        self.assertIn('id="searchInput"', content)
        self.assertIn('id="clearSearch"', content)
        self.assertIn('id="categoryFilters"', content)
        self.assertIn('id="resultsCount"', content)
        self.assertIn('id="noResults"', content)
        self.assertIn('id="resetFilters"', content)
        
        # Verify Article Card Data Attributes
        self.assertIn('class="article-card', content)
        self.assertIn('data-title=', content)
        self.assertIn('data-category=', content)
        self.assertIn('data-desc=', content)
        
        # Verify Vanilla JS Script
        self.assertIn('normalizeText', content)
        self.assertIn('applyFilter', content)
        self.assertIn('searchInput.addEventListener', content)

    def test_rss_and_json_feeds(self):
        # RSS 2.0 XML
        rss_file = Path("dist") / "feed.xml"
        self.assertTrue(rss_file.exists())
        rss_text = rss_file.read_text(encoding="utf-8")
        self.assertIn('<rss version="2.0"', rss_text)
        self.assertIn('<channel>', rss_text)
        self.assertIn('<item>', rss_text)
        self.assertIn('<pubDate>', rss_text)
        
        # Parse XML to verify valid syntax
        root = ET.fromstring(rss_text)
        channel = root.find("channel")
        self.assertIsNotNone(channel)
        items = channel.findall("item")
        self.assertGreater(len(items), 10)

        # JSON Feed 1.1
        json_file = Path("dist") / "feed.json"
        self.assertTrue(json_file.exists())
        json_data = json.loads(json_file.read_text(encoding="utf-8"))
        self.assertEqual(json_data.get("version"), "https://jsonfeed.org/version/1.1")
        self.assertGreater(len(json_data.get("items", [])), 10)

if __name__ == "__main__":
    unittest.main()
