import os
import re
import sys
import glob
import math
import shutil
import json
import html
from datetime import datetime, timezone
import email.utils
import yaml
import markdown

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

POSTS_DIR = os.path.join(os.path.dirname(__file__), "content", "posts")
DIST_DIR = os.path.join(os.path.dirname(__file__), "dist")
SITE_TITLE = "E-İmza & E-Dönüşüm Açık Kaynak"
SITE_DESC = "E-İmza, KEP, UYAP ve e-Dönüşüm araçları için modern açık kaynak rehber ve blog."
SITE_URL = "https://eimza-kep.github.io/eimza-blog"

def slugify(text):
    replacements = {
        'İ': 'i', 'I': 'i', 'ı': 'i', 'ğ': 'g', 'Ğ': 'g',
        'ü': 'u', 'Ü': 'u', 'ş': 's', 'Ş': 's', 'ö': 'o',
        'Ö': 'o', 'ç': 'c', 'Ç': 'c'
    }
    for tr, en in replacements.items():
        text = text.replace(tr, en)
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def format_rfc822(date_val):
    if not date_val:
        return email.utils.format_datetime(datetime.now(timezone.utc))
    try:
        if isinstance(date_val, datetime):
            if date_val.tzinfo is None:
                date_val = date_val.replace(tzinfo=timezone.utc)
            return email.utils.format_datetime(date_val)
        if isinstance(date_val, str):
            clean_str = date_val.strip()[:10]
            dt = datetime.strptime(clean_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
            return email.utils.format_datetime(dt)
        if hasattr(date_val, "timetuple"):
            dt = datetime.fromordinal(date_val.toordinal()).replace(tzinfo=timezone.utc)
            return email.utils.format_datetime(dt)
    except Exception:
        pass
    return email.utils.format_datetime(datetime.now(timezone.utc))

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
    
    title = meta.get("title", filename.replace("-", " ").title())
    date = meta.get("date", meta.get("pub_date", meta.get("pubDate", "")))
    if hasattr(date, "isoformat"):
        date = date.isoformat()
    elif isinstance(date, str):
        date = date.strip()
    else:
        date = str(date) if date else ""

    description = meta.get("description", meta.get("desc", ""))
    if not description:
        plain = re.sub(r'#+\s.*', '', body)
        plain = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', plain)
        plain = re.sub(r'[`*_>#-]', '', plain)
        plain = ' '.join(plain.split())
        description = plain[:170] + "..." if len(plain) > 170 else plain

    category = meta.get("category", "Genel")
    tags = meta.get("tags", [])
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",") if t.strip()]
    elif not isinstance(tags, list):
        tags = []

    body_clean = re.sub(r'!\[(.*?)\]\(/images/(.*?)\)', r'> 🖼️ *[\1]*\n', body)
    html_content = markdown.markdown(body_clean, extensions=["fenced_code", "tables", "toc", "nl2br"])

    return {
        "title": title,
        "slug": slugify(filename),
        "pub_date": date,
        "description": description,
        "category": category,
        "tags": tags,
        "html": html_content,
        "meta": meta
    }

def get_base_template(title, content, base_path="./", canonical_url=""):
    return f"""<!DOCTYPE html>
<html lang="tr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | {SITE_TITLE}</title>
    <meta name="description" content="{SITE_DESC}">
    <link rel="canonical" href="{canonical_url or SITE_URL}">
    <link rel="alternate" type="application/rss+xml" title="{SITE_TITLE} RSS 2.0" href="{base_path}feed.xml">
    <link rel="alternate" type="application/json" title="{SITE_TITLE} JSON Feed" href="{base_path}feed.json">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Inter', 'sans-serif'],
                    }},
                    colors: {{
                        gray: {{
                            50: '#fafafa', 100: '#f4f4f5', 200: '#e4e4e7',
                            800: '#27272a', 900: '#18181b', 950: '#09090b'
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        body {{ font-family: 'Inter', sans-serif; background-color: #fafafa; color: #09090b; }}
        .glass-header {{ background: rgba(255,255,255,0.85); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(0,0,0,0.06); }}
        .prose h1, .prose h2, .prose h3 {{ font-weight: 700; letter-spacing: -0.02em; margin-top: 1.5em; margin-bottom: 0.5em; }}
        .prose h1 {{ font-size: 2.25rem; }}
        .prose h2 {{ font-size: 1.5rem; }}
        .prose p {{ line-height: 1.7; color: #3f3f46; margin-bottom: 1.2em; }}
        .prose a {{ color: #000; text-decoration: underline; text-underline-offset: 4px; }}
        .prose pre {{ background: #09090b; color: #fafafa; padding: 1.5rem; border-radius: 8px; overflow-x: auto; margin-bottom: 1.5em; }}
        .prose code {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; font-size: 0.875em; }}
        .card-hover {{ transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1); border: 1px solid #e4e4e7; background: #fff; }}
        .card-hover:hover {{ border-color: #000; transform: translateY(-2px); box-shadow: 0 12px 32px -10px rgba(0,0,0,0.08); }}
    </style>
</head>
<body class="antialiased flex flex-col min-h-screen">
    <!-- Navbar -->
    <header class="glass-header sticky top-0 z-50">
        <div class="max-w-5xl mx-auto px-6 h-16 flex items-center justify-between">
            <a href="{base_path}" class="flex items-center gap-2 text-black hover:opacity-80 transition-opacity">
                <i class="ph-fill ph-code text-2xl text-black"></i>
                <span class="font-bold tracking-tight text-lg">eimza.dev</span>
            </a>
            <nav class="flex items-center gap-5 sm:gap-6">
                <a href="{base_path}" class="text-sm font-medium text-gray-700 hover:text-black transition-colors">Projeler</a>
                <a href="{base_path}hakkimizda.html" class="text-sm font-medium text-gray-700 hover:text-black transition-colors">Hakkımızda</a>
                <a href="{base_path}feed.xml" class="text-sm font-medium text-gray-700 hover:text-amber-600 flex items-center gap-1 transition-colors" title="RSS 2.0 Beslemesi">
                    <i class="ph-bold ph-rss-simple text-amber-500"></i> RSS
                </a>
                <a href="https://github.com/eimza-kep" target="_blank" class="text-sm font-medium bg-black text-white px-4 py-2 rounded-full hover:bg-gray-800 transition-colors flex items-center gap-2">
                    <i class="ph-fill ph-github-logo"></i> GitHub
                </a>
            </nav>
        </div>
    </header>

    <!-- Content -->
    <main class="flex-grow w-full">
        {content}
    </main>

    <footer class="border-t border-gray-200 mt-20 py-10 bg-white text-center">
        <div class="max-w-5xl mx-auto px-6 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-gray-500">
            <div class="flex items-center gap-2">
                <i class="ph-fill ph-check-circle text-green-500 text-base"></i>
                <span>%100 Açık Kaynak LegalTech & E-Dönüşüm İnisiyatifi</span>
            </div>
            <div class="flex items-center gap-4">
                <a href="{base_path}feed.xml" class="hover:text-black transition-colors flex items-center gap-1">
                    <i class="ph-bold ph-rss-simple text-amber-500"></i> RSS Beslemesi
                </a>
                <span>•</span>
                <a href="{base_path}feed.json" class="hover:text-black transition-colors">JSON Feed</a>
                <span>•</span>
                <a href="https://github.com/eimza-kep/eimza-blog" target="_blank" class="hover:text-black transition-colors">Kaynak Kod</a>
            </div>
        </div>
    </footer>
</body>
</html>"""

def generate_site():
    if os.path.exists(DIST_DIR):
        shutil.rmtree(DIST_DIR)
    os.makedirs(os.path.join(DIST_DIR, "posts"), exist_ok=True)

    files = glob.glob(os.path.join(POSTS_DIR, "*.md"))
    articles = []

    for f in files:
        articles.append(parse_markdown(f))

    # Sort newest first
    articles.sort(key=lambda x: x["pub_date"], reverse=True)

    # 1. Build Single Post Pages
    for art in articles:
        post_url = f"{SITE_URL}/posts/{art['slug']}.html"
        tag_pills = "".join([f'<span class="text-xs bg-gray-100 text-gray-700 px-2 py-0.5 rounded">#{html.escape(t)}</span> ' for t in art.get("tags", [])])
        
        post_html = f"""
        <article class="max-w-3xl mx-auto px-6 py-16">
            <a href="../" class="inline-flex items-center gap-2 text-sm font-medium text-gray-500 hover:text-black mb-8 transition-colors">
                <i class="ph ph-arrow-left"></i> Geri Dön
            </a>
            <div class="flex items-center gap-2 mb-3">
                <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-black text-white">{html.escape(art['category'])}</span>
                {f'<div class="flex gap-1">{tag_pills}</div>' if tag_pills else ''}
            </div>
            <h1 class="text-3xl sm:text-4xl font-bold tracking-tight text-black mb-4 leading-tight">{art["title"]}</h1>
            <div class="flex items-center gap-4 text-sm text-gray-500 mb-10 pb-10 border-b border-gray-100">
                <span class="flex items-center gap-1"><i class="ph ph-calendar-blank"></i> {art["pub_date"][:10] if art["pub_date"] else "Geliştiriliyor"}</span>
                <span class="flex items-center gap-1"><i class="ph ph-tag"></i> Açık Kaynak</span>
                <span class="flex items-center gap-1"><i class="ph ph-shield-check text-green-600"></i> Doğrulanmış Rehber</span>
            </div>
            <div class="prose">
                {art["html"]}
            </div>
        </article>
        """
        full_html = get_base_template(art["title"], post_html, base_path="../", canonical_url=post_url)
        with open(os.path.join(DIST_DIR, "posts", f"{art['slug']}.html"), "w", encoding="utf-8") as out:
            out.write(full_html)

    # 2. Extract Categories for Filter Chips
    cat_counts = {}
    for art in articles:
        c = art.get("category", "Genel")
        cat_counts[c] = cat_counts.get(c, 0) + 1
    sorted_categories = sorted(cat_counts.keys())

    filter_buttons_html = f"""
    <button class="filter-btn px-4 py-2 rounded-full text-xs font-semibold bg-black text-white transition-all shadow-sm" data-category="all">
        Tümü ({len(articles)})
    </button>
    """
    for cat in sorted_categories:
        count = cat_counts[cat]
        filter_buttons_html += f"""
        <button class="filter-btn px-4 py-2 rounded-full text-xs font-semibold bg-white text-gray-700 border border-gray-200 hover:bg-gray-100 transition-all shadow-sm" data-category="{html.escape(cat)}">
            {html.escape(cat)} ({count})
        </button>
        """

    # 3. Build Index Page Article Cards
    cards_html = ""
    for art in articles:
        cards_html += f"""
        <a href="posts/{art['slug']}.html" 
           class="article-card card-hover rounded-2xl p-6 flex flex-col justify-between h-full group"
           data-title="{html.escape(art['title'])}"
           data-desc="{html.escape(art.get('description', ''))}"
           data-category="{html.escape(art.get('category', 'Genel'))}"
           data-tags="{html.escape(','.join(art.get('tags', [])))}">
            <div>
                <div class="flex items-center justify-between gap-2 mb-3">
                    <span class="text-xs font-semibold px-2.5 py-1 rounded-full bg-gray-100 text-gray-800 group-hover:bg-black group-hover:text-white transition-colors">
                        {html.escape(art.get('category', 'Genel'))}
                    </span>
                    <span class="text-xs text-gray-400 flex items-center gap-1 font-mono">
                        <i class="ph ph-calendar-blank"></i> {art['pub_date'][:10] if art['pub_date'] else '2026'}
                    </span>
                </div>
                <h3 class="text-xl font-bold tracking-tight text-gray-900 mb-2 leading-snug group-hover:text-black">{html.escape(art["title"])}</h3>
                <p class="text-sm text-gray-600 line-clamp-3 mb-4 leading-relaxed">{html.escape(art.get('description', ''))}</p>
            </div>
            <div class="mt-4 pt-4 border-t border-gray-100 flex items-center justify-between text-sm text-gray-500 font-medium">
                <span class="group-hover:text-black transition-colors">Devamını Oku</span>
                <i class="ph ph-arrow-right group-hover:translate-x-1 text-black transition-transform"></i>
            </div>
        </a>
        """

    index_content = f"""
    <div class="max-w-5xl mx-auto px-6 pt-16 pb-10 text-center">
        <div class="inline-flex items-center gap-2 bg-black text-white text-xs font-bold px-3 py-1.5 rounded-full mb-6">
            <span class="w-2 h-2 rounded-full bg-green-400 animate-pulse"></span> %100 Açık Kaynak
        </div>
        <h1 class="text-4xl sm:text-6xl font-bold tracking-tighter text-black mb-6">
            Dijital Dönüşüm<br>Geliştirici Merkezi
        </h1>
        <p class="text-lg text-gray-600 max-w-2xl mx-auto leading-relaxed mb-8">
            E-İmza, KEP, UYAP, e-Fatura ve LegalTech ekosistemi için tamamen ücretsiz, açık kaynaklı kod kütüphaneleri, teknik kılavuzlar ve araçlar.
        </p>

        <!-- Canlı Arama Input Kutusu -->
        <div class="max-w-xl mx-auto mb-6 relative">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none text-gray-400">
                <i class="ph ph-magnifying-glass text-lg"></i>
            </div>
            <input type="text" id="searchInput" placeholder="Makale başlığı, etiket veya konu ara..." 
                   class="w-full pl-11 pr-10 py-3.5 rounded-full border border-gray-300 bg-white text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-black focus:border-transparent shadow-sm transition-all"
                   autocomplete="off" spellcheck="false">
            <button id="clearSearch" class="hidden absolute inset-y-0 right-0 pr-4 flex items-center text-gray-400 hover:text-black transition-colors" title="Aramayı Temizle">
                <i class="ph ph-x-circle text-lg"></i>
            </button>
        </div>

        <!-- Kategori Filtre Butonları -->
        <div class="flex flex-wrap items-center justify-center gap-2 mb-8" id="categoryFilters">
            {filter_buttons_html}
        </div>

        <div class="flex items-center justify-between text-xs text-gray-500 px-2 max-w-5xl mx-auto border-b border-gray-200 pb-3">
            <span id="resultsCount">Toplam {len(articles)} rehber listeleniyor</span>
            <span class="flex items-center gap-1.5"><i class="ph ph-lightning text-amber-500"></i> Vanilla JS Anlık Arama</span>
        </div>
    </div>

    <!-- Makaleler Izgarası -->
    <div class="max-w-5xl mx-auto px-6 pb-24">
        <div id="articlesGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {cards_html}
        </div>

        <!-- Boş Arama Durumu (Empty State) -->
        <div id="noResults" class="hidden text-center py-16 bg-white rounded-2xl border border-dashed border-gray-300 mt-6 p-8">
            <div class="w-16 h-16 rounded-full bg-gray-100 flex items-center justify-center mx-auto mb-4 text-gray-400 text-2xl">
                <i class="ph ph-magnifying-glass"></i>
            </div>
            <h4 class="text-lg font-bold text-gray-900 mb-1">Eşleşen rehber bulunamadı</h4>
            <p class="text-sm text-gray-500 max-w-sm mx-auto mb-4">Arama kriterlerinizle uyuşan herhangi bir teknik yazı bulunamadı. Farklı bir arama terimi deneyebilir veya kategoriyi sıfırlayabilirsiniz.</p>
            <button id="resetFilters" class="inline-flex items-center gap-1.5 px-4 py-2 text-xs font-semibold rounded-full bg-black text-white hover:bg-gray-800 transition-colors shadow-sm">
                <i class="ph ph-arrow-counter-clockwise"></i> Aramayı ve Filtreleri Temizle
            </button>
        </div>
    </div>

    <!-- Client-Side Vanilla JS Arama ve Filtreleme Motoru -->
    <script>
    (function() {{
        const searchInput = document.getElementById('searchInput');
        const clearSearch = document.getElementById('clearSearch');
        const filterBtns = document.querySelectorAll('.filter-btn');
        const articleCards = document.querySelectorAll('.article-card');
        const resultsCount = document.getElementById('resultsCount');
        const noResults = document.getElementById('noResults');
        const resetFiltersBtn = document.getElementById('resetFilters');

        let activeCategory = 'all';
        let searchQuery = '';

        function normalizeText(text) {{
            if (!text) return '';
            return text.toString()
                .toLowerCase()
                .replace(/İ/g, 'i')
                .replace(/I/g, 'i')
                .replace(/ı/g, 'i')
                .replace(/ğ/g, 'g')
                .replace(/Ğ/g, 'g')
                .replace(/ü/g, 'u')
                .replace(/Ü/g, 'u')
                .replace(/ş/g, 's')
                .replace(/Ş/g, 's')
                .replace(/ö/g, 'o')
                .replace(/Ö/g, 'o')
                .replace(/ç/g, 'c')
                .replace(/Ç/g, 'c')
                .replace(/[^a-z0-9]/g, ' ')
                .trim();
        }}

        function applyFilter() {{
            const queryNorm = normalizeText(searchQuery);
            let visibleCount = 0;

            articleCards.forEach(card => {{
                const titleNorm = normalizeText(card.getAttribute('data-title'));
                const descNorm = normalizeText(card.getAttribute('data-desc'));
                const catNorm = normalizeText(card.getAttribute('data-category'));
                const tagsNorm = normalizeText(card.getAttribute('data-tags'));

                const matchesCategory = (activeCategory === 'all') || (catNorm === normalizeText(activeCategory));
                
                let matchesSearch = true;
                if (queryNorm) {{
                    const terms = queryNorm.split(/\\s+/);
                    const fullHaystack = `${{titleNorm}} ${{descNorm}} ${{catNorm}} ${{tagsNorm}}`;
                    matchesSearch = terms.every(term => fullHaystack.includes(term));
                }}

                if (matchesCategory && matchesSearch) {{
                    card.style.display = '';
                    visibleCount++;
                }} else {{
                    card.style.display = 'none';
                }}
            }});

            if (resultsCount) {{
                resultsCount.textContent = `Toplam ${{visibleCount}} rehber listeleniyor`;
            }}

            if (noResults) {{
                if (visibleCount === 0) {{
                    noResults.classList.remove('hidden');
                }} else {{
                    noResults.classList.add('hidden');
                }}
            }}
        }}

        if (searchInput) {{
            searchInput.addEventListener('input', function(e) {{
                searchQuery = e.target.value;
                if (clearSearch) {{
                    if (searchQuery.trim().length > 0) {{
                        clearSearch.classList.remove('hidden');
                    }} else {{
                        clearSearch.classList.add('hidden');
                    }}
                }}
                applyFilter();
            }});
        }}

        if (clearSearch) {{
            clearSearch.addEventListener('click', function() {{
                if (searchInput) {{
                    searchInput.value = '';
                    searchInput.focus();
                }}
                searchQuery = '';
                clearSearch.classList.add('hidden');
                applyFilter();
            }});
        }}

        filterBtns.forEach(btn => {{
            btn.addEventListener('click', function() {{
                filterBtns.forEach(b => {{
                    b.classList.remove('bg-black', 'text-white');
                    b.classList.add('bg-white', 'text-gray-700', 'border', 'border-gray-200');
                }});
                btn.classList.add('bg-black', 'text-white');
                btn.classList.remove('bg-white', 'text-gray-700', 'border', 'border-gray-200');

                activeCategory = btn.getAttribute('data-category');
                applyFilter();
            }});
        }});

        if (resetFiltersBtn) {{
            resetFiltersBtn.addEventListener('click', function() {{
                if (searchInput) {{
                    searchInput.value = '';
                }}
                if (clearSearch) {{
                    clearSearch.classList.add('hidden');
                }}
                searchQuery = '';
                activeCategory = 'all';

                filterBtns.forEach(b => {{
                    if (b.getAttribute('data-category') === 'all') {{
                        b.classList.add('bg-black', 'text-white');
                        b.classList.remove('bg-white', 'text-gray-700', 'border', 'border-gray-200');
                    }} else {{
                        b.classList.remove('bg-black', 'text-white');
                        b.classList.add('bg-white', 'text-gray-700', 'border', 'border-gray-200');
                    }}
                }});

                applyFilter();
            }});
        }}
    }})();
    </script>
    """

    index_html = get_base_template("Açık Kaynak Projeler", index_content, base_path="./")
    with open(os.path.join(DIST_DIR, "index.html"), "w", encoding="utf-8") as out:
        out.write(index_html)

    # 4. Build About (Hakkımızda) Page
    about_content = """
    <article class="max-w-3xl mx-auto px-6 py-16">
        <h1 class="text-4xl font-bold tracking-tight text-black mb-8">Hakkımızda</h1>
        <div class="prose">
            <p class="text-lg"><strong>eimza.dev</strong> ve <strong>E-İmza.plus</strong> ekibi olarak, Türkiye'nin dijital dönüşüm süreçlerine ve hukuki teknolojilerine (LegalTech) yenilikçi, şeffaf ve açık kaynak kodlu çözümler sunmak amacıyla bir araya geldik.</p>
            <h2>Misyonumuz</h2>
            <p>On yıllardır süreklilik arz eden karmaşık e-imza kurulumları, bitmeyen Java sorunları ve parçalı entegrasyonlar hem son kullanıcıları hem de geliştiricileri yoruyor. Amacımız, tüm bu süreçleri modern web standartlarıyla (Vanilla JS, WebUSB, modern API'ler) yeniden inşa etmektir.</p>
            <h2>Neler Yapıyoruz?</h2>
            <ul>
                <li>%100 tarayıcı tabanlı (Client-Side) doküman editörleri ve araçlar.</li>
                <li>Elektronik imza, mali mühür ve KEP süreçleri için açık kaynak kütüphaneler.</li>
                <li>KOBİ'ler ve hukuk büroları için e-Dönüşüm otomasyon scriptleri.</li>
            </ul>
            <p>Tüm kaynak kodlarımız GitHub'da halka açıktır. Topluluğumuzun desteğiyle daha şeffaf bir dijital altyapı kurmak için çalışıyoruz.</p>
        </div>
    </article>
    """
    about_html = get_base_template("Hakkımızda", about_content, base_path="./")
    with open(os.path.join(DIST_DIR, "hakkimizda.html"), "w", encoding="utf-8") as out:
        out.write(about_html)

    # 5. Build RSS 2.0 Feed (feed.xml)
    rss_items = []
    for art in articles:
        desc = art.get("description", art["title"])
        pub_rfc = format_rfc822(art["pub_date"])
        item_xml = f"""    <item>
      <title>{html.escape(art["title"])}</title>
      <link>{SITE_URL}/posts/{art["slug"]}.html</link>
      <guid>{SITE_URL}/posts/{art["slug"]}.html</guid>
      <pubDate>{pub_rfc}</pubDate>
      <category>{html.escape(art.get("category", "Genel"))}</category>
      <description>{html.escape(desc)}</description>
    </item>"""
        rss_items.append(item_xml)

    rss_content = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{html.escape(SITE_TITLE)}</title>
    <link>{SITE_URL}</link>
    <description>{html.escape(SITE_DESC)}</description>
    <language>tr</language>
    <atom:link href="{SITE_URL}/feed.xml" rel="self" type="application/rss+xml" />
{"\n".join(rss_items)}
  </channel>
</rss>"""

    with open(os.path.join(DIST_DIR, "feed.xml"), "w", encoding="utf-8") as out:
        out.write(rss_content)

    # 6. Build JSON Feed 1.1 (feed.json)
    json_feed = {
        "version": "https://jsonfeed.org/version/1.1",
        "title": SITE_TITLE,
        "home_page_url": SITE_URL,
        "feed_url": f"{SITE_URL}/feed.json",
        "description": SITE_DESC,
        "items": [
            {
                "id": f"{SITE_URL}/posts/{art['slug']}.html",
                "url": f"{SITE_URL}/posts/{art['slug']}.html",
                "title": art["title"],
                "content_html": art["html"],
                "summary": art.get("description", ""),
                "date_published": art["pub_date"] if art["pub_date"] else None,
                "tags": art.get("tags", []),
                "category": art.get("category", "Genel")
            }
            for art in articles
        ]
    }
    with open(os.path.join(DIST_DIR, "feed.json"), "w", encoding="utf-8") as out:
        json.dump(json_feed, out, ensure_ascii=False, indent=2)

    print(f"Done! Built {len(articles)} articles, About page, feed.xml, and feed.json into {DIST_DIR}.")

if __name__ == "__main__":
    generate_site()
