import unittest
import os
from pathlib import Path
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

    def test_slugify(self):
        self.assertEqual(build.slugify("İstanbul ve Çankaya Hukuk"), "istanbul-ve-cankaya-hukuk")
        self.assertEqual(build.slugify("E-İmza & KEP Rehberi 2026!"), "e-imza-kep-rehberi-2026")

if __name__ == "__main__":
    unittest.main()
