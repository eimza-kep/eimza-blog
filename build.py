import os
import re
import glob
import math
import shutil
import yaml
import markdown

POSTS_DIR = os.path.join(os.path.dirname(__file__), "content", "posts")
DIST_DIR = os.path.join(os.path.dirname(__file__), "dist")
SITE_TITLE = "E-İmza & Dijital Dönüşüm Rehberi"
SITE_DESC = "E-İmza, KEP, Mali Mühür, e-Fatura, GİB Çözümleri ve Anadolu KOBİ'lerinin Dijitalleşme Rehberi."
SITE_URL = "https://eimza-blog.pages.dev"

def slugify(text):
    text = text.lower()
    replacements = {
        'ı': 'i', 'ğ': 'g', 'ü': 'u', 'ş': 's', 'ö': 'o', 'ç': 'c',
        'İ': 'i', 'Ğ': 'g', 'Ü': 'u', 'Ş': 's', 'Ö': 'o', 'Ç': 'c'
    }
    for tr, en in replacements.items():
        text = text.replace(tr, en)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def parse_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    meta = {}
    body = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            try:
                meta = yaml.safe_load(parts[1]) or {}
            except Exception as e:
                print(f"Error parsing yaml in {file_path}: {e}")
            body = parts[2].strip()

    filename = os.path.splitext(os.path.basename(file_path))[0]
    slug = slugify(filename)

    title = meta.get("title", filename.replace("-", " ").title())
    description = meta.get("description", "")
    pub_date = str(meta.get("pubDate", "2026-09-19"))
    category = meta.get("category", "Genel")
    author = meta.get("author", "E-İmza Rehberi")

    # Word count and reading time
    words = len(re.findall(r'\w+', body))
    reading_time = max(1, math.ceil(words / 200))

    # Strip local relative images that don't exist, replace with placeholder style
    body_clean = re.sub(r'!\[(.*?)\]\(/images/(.*?)\)', r'> 📸 *[\1]*\n', body)

    html_content = markdown.markdown(
        body_clean,
        extensions=["fenced_code", "tables", "toc", "nl2br"]
    )

    return {
        "slug": slug,
        "title": title,
        "description": description,
        "pub_date": pub_date,
        "category": category,
        "author": author,
        "reading_time": reading_time,
        "html_content": html_content,
        "body_preview": re.sub(r'<[^>]+>', '', html_content)[:220] + "..."
    }

def get_base_template(title, content, canonical_url=""):
    return f"""<!DOCTYPE html>
<html lang="tr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | {SITE_TITLE}</title>
    <meta name="description" content="{SITE_DESC}">
    <link rel="canonical" href="{canonical_url or SITE_URL}">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        primary: {{ 50: '#f0fdf4', 100: '#dcfce7', 500: '#22c55e', 600: '#16a34a', 700: '#15803d', 900: '#14532d' }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        .prose h1, .prose h2, .prose h3, .prose h4 {{ color: #1e293b; font-weight: 700; margin-top: 1.5rem; margin-bottom: 0.75rem; }}
        .prose h2 {{ font-size: 1.5rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem; }}
        .prose h3 {{ font-size: 1.25rem; }}
        .prose p {{ margin-bottom: 1.25rem; line-height: 1.75; color: #334155; }}
        .prose ul, .prose ol {{ margin-left: 1.5rem; margin-bottom: 1.25rem; list-style-type: disc; }}
        .prose li {{ margin-bottom: 0.5rem; color: #334155; }}
        .prose blockquote {{ border-left: 4px solid #22c55e; padding-left: 1rem; color: #64748b; font-style: italic; margin: 1.5rem 0; background: #f8fafc; padding: 0.75rem 1rem; border-radius: 0 0.5rem 0.5rem 0; }}
        .prose code {{ background: #f1f5f9; padding: 0.2rem 0.4rem; border-radius: 0.25rem; font-size: 0.9em; font-family: monospace; color: #0f172a; }}
        .prose pre {{ background: #0f172a; color: #f8fafc; padding: 1rem; border-radius: 0.5rem; overflow-x: auto; margin-bottom: 1.5rem; }}
        .prose strong {{ color: #0f172a; }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased flex flex-col min-h-screen">
    <!-- Header -->
    <header class="bg-white border-b border-slate-200 sticky top-0 z-50 shadow-sm backdrop-blur-md bg-white/90">
        <div class="max-w-5xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
            <a href="/" class="flex items-center gap-3 group">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-500 flex items-center justify-center text-white font-bold shadow-md group-hover:scale-105 transition-transform">
                    ✍️
                </div>
                <div>
                    <span class="font-bold text-lg text-slate-900 block leading-tight">E-İmza & Dönüşüm</span>
                    <span class="text-xs text-slate-500 font-medium">Dijital Bilgi ve Rehber Portalı</span>
                </div>
            </a>
            <div class="flex items-center gap-4">
                <a href="/" class="text-sm font-semibold text-slate-600 hover:text-emerald-600 transition-colors">Ana Sayfa</a>
                <a href="https://dev.to/eimza" target="_blank" rel="noopener" class="text-xs bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold px-3 py-1.5 rounded-lg transition-colors flex items-center gap-1.5">
                    <span>DEV.to</span> ↗
                </a>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="flex-grow max-w-5xl w-full mx-auto px-4 sm:px-6 py-8">
        {content}
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-slate-200 mt-16 py-8 text-center text-sm text-slate-500">
        <div class="max-w-5xl mx-auto px-4">
            <p class="font-semibold text-slate-700">© 2026 E-İmza ve Dijital Dönüşüm Portalı</p>
            <p class="text-xs mt-1">Cloudflare Pages & GitHub Pages ile %100 Otonom Yayınlanmaktadır.</p>
        </div>
    </footer>
</body>
</html>
"""

def generate_site():
    if os.path.exists(DIST_DIR):
        shutil.rmtree(DIST_DIR)
    os.makedirs(os.path.join(DIST_DIR, "posts"), exist_ok=True)

    files = glob.glob(os.path.join(POSTS_DIR, "*.md"))
    articles = []

    print(f"Parsing {len(files)} articles...")
    for f in files:
        art = parse_markdown(f)
        articles.append(art)

    # Sort newest first
    articles.sort(key=lambda x: x["pub_date"], reverse=True)

    # Collect categories
    categories = sorted(list(set(a["category"] for a in articles if a["category"])))

    # 1. Build Single Post Pages
    for art in articles:
        post_url = f"{SITE_URL}/posts/{art['slug']}.html"
        post_html = f"""
        <article class="bg-white rounded-2xl p-6 sm:p-10 shadow-sm border border-slate-200 max-w-3xl mx-auto">
            <div class="mb-6">
                <a href="/" class="inline-flex items-center gap-1 text-sm font-semibold text-emerald-600 hover:text-emerald-700 mb-4 transition-colors">
                    ← Tüm Yazılara Dön
                </a>
                <div class="flex flex-wrap items-center gap-2 mb-3">
                    <span class="bg-emerald-50 text-emerald-700 text-xs font-bold px-2.5 py-1 rounded-full border border-emerald-200">
                        {art['category']}
                    </span>
                    <span class="text-xs text-slate-400">•</span>
                    <span class="text-xs text-slate-500 font-medium">📅 {art['pub_date']}</span>
                    <span class="text-xs text-slate-400">•</span>
                    <span class="text-xs text-slate-500 font-medium">⏱️ {art['reading_time']} dk okuma</span>
                </div>
                <h1 class="text-2xl sm:text-4xl font-extrabold text-slate-900 tracking-tight leading-tight">
                    {art['title']}
                </h1>
                {f'<p class="text-lg text-slate-600 mt-4 leading-relaxed font-normal">{art["description"]}</p>' if art['description'] else ''}
                <div class="flex items-center gap-3 mt-6 pt-4 border-t border-slate-100 text-sm text-slate-600">
                    <span class="font-semibold text-slate-800">👤 {art['author']}</span>
                </div>
            </div>

            <div class="prose text-slate-700 max-w-none pt-4">
                {art['html_content']}
            </div>

            <div class="mt-12 pt-6 border-t border-slate-200 flex justify-between items-center">
                <a href="/" class="text-sm font-semibold text-emerald-600 hover:text-emerald-700">
                    ← Tüm Yazılara Dön
                </a>
                <a href="#top" class="text-xs text-slate-400 hover:text-slate-600">
                    ↑ Başa Dön
                </a>
            </div>
        </article>
        """
        full_html = get_base_template(art['title'], post_html, post_url)
        with open(os.path.join(DIST_DIR, "posts", f"{art['slug']}.html"), "w", encoding="utf-8") as out:
            out.write(full_html)

    # 2. Build Index Page
    cards_html = ""
    for art in articles:
        cards_html += f"""
        <div class="article-card bg-white rounded-2xl p-6 shadow-sm border border-slate-200 hover:shadow-md hover:border-emerald-300 transition-all flex flex-col justify-between" data-category="{art['category'].lower()}" data-title="{art['title'].lower()}">
            <div>
                <div class="flex items-center justify-between gap-2 mb-3">
                    <span class="bg-emerald-50 text-emerald-700 text-xs font-bold px-2.5 py-0.5 rounded-full border border-emerald-100">
                        {art['category']}
                    </span>
                    <span class="text-xs text-slate-400 font-medium">
                        {art['pub_date']}
                    </span>
                </div>
                <h2 class="text-lg font-bold text-slate-900 leading-snug hover:text-emerald-600 transition-colors mb-2">
                    <a href="/posts/{art['slug']}.html">
                        {art['title']}
                    </a>
                </h2>
                <p class="text-sm text-slate-600 line-clamp-3 mb-4 leading-relaxed">
                    {art['description'] or art['body_preview']}
                </p>
            </div>
            <div class="flex items-center justify-between pt-4 border-t border-slate-100 text-xs text-slate-500 font-medium">
                <span>⏱️ {art['reading_time']} dk okuma</span>
                <a href="/posts/{art['slug']}.html" class="text-emerald-600 font-bold hover:text-emerald-700 flex items-center gap-1">
                    Devamını Oku →
                </a>
            </div>
        </div>
        """

    cat_filters_html = '<button class="cat-btn px-3 py-1.5 rounded-lg text-xs font-bold bg-emerald-600 text-white transition-colors" data-cat="all">Tümü</button>'
    for c in categories:
        cat_filters_html += f'<button class="cat-btn px-3 py-1.5 rounded-lg text-xs font-bold bg-white text-slate-600 border border-slate-200 hover:border-emerald-300 transition-colors" data-cat="{c.lower()}">{c}</button>'

    index_content = f"""
    <!-- Hero Section -->
    <div class="text-center py-8 sm:py-12">
        <h1 class="text-3xl sm:text-5xl font-black text-slate-900 tracking-tight">
            E-İmza & Dijital Dönüşüm Bilgi Merkezi
        </h1>
        <p class="text-slate-600 max-w-2xl mx-auto mt-4 text-base sm:text-lg">
            KOBİ'ler, serbest meslek sahipleri ve kurumlar için güncel teknik rehberler, e-dönüşüm çözümleri ve sektörel analizler.
        </p>

        <!-- Search & Filter Bar -->
        <div class="max-w-xl mx-auto mt-8 flex flex-col sm:flex-row gap-2">
            <div class="relative flex-grow">
                <input type="text" id="searchInput" placeholder="Makalelerde ara... (ör: USB Token, Mali Mühür, Java)" class="w-full px-4 py-3 rounded-xl border border-slate-200 bg-white focus:outline-none focus:ring-2 focus:ring-emerald-500 text-sm shadow-sm">
            </div>
        </div>

        <div class="flex flex-wrap items-center justify-center gap-2 mt-4" id="catFilter">
            {cat_filters_html}
        </div>
    </div>

    <!-- Articles Grid -->
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-4" id="articlesGrid">
        {cards_html}
    </div>

    <script>
        const searchInput = document.getElementById('searchInput');
        const catBtns = document.querySelectorAll('.cat-btn');
        const cards = document.querySelectorAll('.article-card');
        let currentCat = 'all';

        function filterCards() {{
            const query = searchInput.value.toLowerCase().trim();
            cards.forEach(card => {{
                const title = card.getAttribute('data-title');
                const cat = card.getAttribute('data-category');
                const matchesSearch = !query || title.includes(query);
                const matchesCat = currentCat === 'all' || cat === currentCat;
                if (matchesSearch && matchesCat) {{
                    card.style.display = 'flex';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}

        searchInput.addEventListener('input', filterCards);

        catBtns.forEach(btn => {{
            btn.addEventListener('click', () => {{
                catBtns.forEach(b => {{
                    b.classList.remove('bg-emerald-600', 'text-white');
                    b.classList.add('bg-white', 'text-slate-600');
                }});
                btn.classList.remove('bg-white', 'text-slate-600');
                btn.classList.add('bg-emerald-600', 'text-white');
                currentCat = btn.getAttribute('data-cat');
                filterCards();
            }});
        }});
    </script>
    """

    full_index_html = get_base_template("Ana Sayfa", index_content, SITE_URL)
    with open(os.path.join(DIST_DIR, "index.html"), "w", encoding="utf-8") as out:
        out.write(full_index_html)

    # 3. Build Sitemap & Robots.txt
    sitemap_items = [f"<url><loc>{SITE_URL}/</loc><priority>1.0</priority></url>"]
    for art in articles:
        sitemap_items.append(f"<url><loc>{SITE_URL}/posts/{art['slug']}.html</loc><lastmod>{art['pub_date']}</lastmod><priority>0.8</priority></url>")
    
    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    {''.join(sitemap_items)}
</urlset>"""

    with open(os.path.join(DIST_DIR, "sitemap.xml"), "w", encoding="utf-8") as out:
        out.write(sitemap_xml)

    with open(os.path.join(DIST_DIR, "robots.txt"), "w", encoding="utf-8") as out:
        out.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")

    print(f"Done! Built {len(articles)} articles into {DIST_DIR}")

if __name__ == "__main__":
    generate_site()
