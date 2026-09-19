import os
import re
import sys
import glob
import math
import shutil
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

def get_base_template(title, content, base_path="./", canonical_url=""):
    return f"""<!DOCTYPE html>
<html lang="tr" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | {SITE_TITLE}</title>
    <meta name="description" content="{SITE_DESC}">
    <link rel="canonical" href="{canonical_url or SITE_URL}">
    <link rel="alternate" type="application/rss+xml" title="{SITE_TITLE} (RSS 2.0)" href="{SITE_URL}/feed.xml">
    <link rel="alternate" type="application/json" title="{SITE_TITLE} (JSON Feed)" href="{SITE_URL}/feed.json">
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
        <div class="max-w-6xl mx-auto px-4 sm:px-6 h-16 flex items-center justify-between">
            <a href="{base_path}" class="flex items-center gap-3 group">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-500 flex items-center justify-center text-white font-bold shadow-md group-hover:scale-105 transition-transform">
                    ✍️
                </div>
                <div>
                    <span class="font-bold text-lg text-slate-900 block leading-tight">E-İmza & E-Dönüşüm</span>
                    <span class="text-xs text-slate-500 font-medium">Ulusal Bilgi ve Portal Ağı</span>
                </div>
            </a>
            <div class="flex items-center gap-3">
                <a href="{base_path}#portallar" class="hidden sm:inline text-xs font-bold text-slate-600 hover:text-emerald-600 transition-colors">Portallar</a>
                <a href="{base_path}#araclar" class="hidden sm:inline text-xs font-bold text-slate-600 hover:text-emerald-600 transition-colors">Açık Kaynak</a>
                <a href="https://telegra.ph/Türkiye-E-Dönüşüm--E-İmza-Rehberi-09-19" target="_blank" rel="noopener" class="text-xs bg-sky-50 hover:bg-sky-100 text-sky-700 font-bold px-2.5 py-1.5 rounded-lg transition-colors flex items-center gap-1 border border-sky-200">
                    <span>📱 Telegram</span> ↗
                </a>
                <a href="https://dev.to/eimza" target="_blank" rel="noopener" class="text-xs bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold px-2.5 py-1.5 rounded-lg transition-colors flex items-center gap-1 border border-slate-200">
                    <span>DEV.to</span> ↗
                </a>
                <a href="https://github.com/eimza-kep" target="_blank" rel="noopener" class="text-xs bg-slate-900 hover:bg-slate-800 text-white font-bold px-2.5 py-1.5 rounded-lg transition-colors flex items-center gap-1">
                    <span>GitHub</span> ↗
                </a>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="flex-grow max-w-6xl w-full mx-auto px-4 sm:px-6 py-8">
        {content}
    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-slate-200 mt-16 py-10 text-center text-sm text-slate-500">
        <div class="max-w-6xl mx-auto px-4">
            <div class="flex flex-wrap justify-center gap-6 text-xs font-semibold text-slate-600 mb-4">
                <a href="https://eimza-rehberi.pages.dev" target="_blank" class="hover:text-emerald-600">E-İmza Rehberi</a>
                <a href="https://kep-akademisi.pages.dev" target="_blank" class="hover:text-emerald-600">KEP Akademisi</a>
                <a href="https://mali-muhur-merkezi.pages.dev" target="_blank" class="hover:text-emerald-600">Mali Mühür</a>
                <a href="https://efatura-atolyesi.pages.dev" target="_blank" class="hover:text-emerald-600">e-Fatura Atölyesi</a>
                <a href="https://edonusum-kobi.pages.dev" target="_blank" class="hover:text-emerald-600">KOBİ Dönüşüm</a>
                <a href="https://uyap-teknik-destek.pages.dev" target="_blank" class="hover:text-emerald-600">UYAP Destek</a>
                <a href="https://dijital-kimlik-guvenlik.pages.dev" target="_blank" class="hover:text-emerald-600">Kimlik & PKI Lab</a>
                <a href="{base_path}feed.xml" target="_blank" class="text-emerald-600 hover:text-emerald-700 font-bold">📡 RSS</a>
            </div>
            <p class="font-semibold text-slate-700">© 2026 E-İmza ve E-Dönüşüm Ekosistemi</p>
            <p class="text-xs mt-1 text-slate-400">Cloudflare Pages & GitHub Pages ile %100 Otonom ve Yüksek Hızlı Dağıtık Altyapı.</p>
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
                <a href="../" class="inline-flex items-center gap-1 text-sm font-semibold text-emerald-600 hover:text-emerald-700 mb-4 transition-colors">
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
                <a href="../" class="text-sm font-semibold text-emerald-600 hover:text-emerald-700">
                    ← Tüm Yazılara Dön
                </a>
                <a href="#top" class="text-xs text-slate-400 hover:text-slate-600">
                    ↑ Başa Dön
                </a>
            </div>
        </article>
        """
        full_html = get_base_template(art['title'], post_html, base_path="../", canonical_url=post_url)
        with open(os.path.join(DIST_DIR, "posts", f"{art['slug']}.html"), "w", encoding="utf-8") as out:
            out.write(full_html)

    # 2. Build Index Page
    cards_html = ""
    if not articles:
        cards_html = """
        <div class="col-span-full text-center py-16 bg-white rounded-2xl border border-slate-200 p-8 shadow-sm">
            <div class="text-4xl mb-3">📝</div>
            <h3 class="text-lg font-bold text-slate-800">Henüz Yayınlanmış Makale Bulunmuyor</h3>
            <p class="text-sm text-slate-500 mt-2">Yeni makaleler ve teknik rehberler çok yakında burada yayınlanacaktır.</p>
        </div>
        """
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
                    <a href="posts/{art['slug']}.html">
                        {art['title']}
                    </a>
                </h2>
                <p class="text-sm text-slate-600 line-clamp-3 mb-4 leading-relaxed">
                    {art['description'] or art['body_preview']}
                </p>
            </div>
            <div class="flex items-center justify-between pt-4 border-t border-slate-100 text-xs text-slate-500 font-medium">
                <span>⏱️ {art['reading_time']} dk okuma</span>
                <a href="posts/{art['slug']}.html" class="text-emerald-600 font-bold hover:text-emerald-700 flex items-center gap-1">
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
    <div class="text-center py-10 sm:py-16">
        <div class="inline-flex items-center gap-2 bg-emerald-50 border border-emerald-200 text-emerald-800 text-xs font-bold px-3.5 py-1.5 rounded-full mb-6 shadow-sm">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span> 🌐 Türkiye E-Dönüşüm & Dijital İmza Yayın Ekosistemi
        </div>
        <h1 class="text-3xl sm:text-5xl lg:text-6xl font-black text-slate-900 tracking-tight leading-tight max-w-4xl mx-auto">
            E-İmza, KEP ve Mali Mühürde <span class="bg-gradient-to-r from-emerald-600 via-teal-600 to-cyan-600 bg-clip-text text-transparent">Eksiksiz Rehberiniz</span>
        </h1>
        <p class="text-slate-600 max-w-2xl mx-auto mt-5 text-base sm:text-lg leading-relaxed">
            Kurumsal şirketler, KOBİ'ler, serbest meslek sahipleri ve yazılım geliştiriciler için 7 özel tematik portal, açık kaynak araçlar ve teknik kılavuzlar.
        </p>
        <div class="flex flex-wrap items-center justify-center gap-3 mt-8">
            <a href="#portallar" class="bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-sm px-6 py-3 rounded-xl shadow-md shadow-emerald-600/20 transition-all">
                Tematik Portalları Keşfet ↓
            </a>
            <a href="#araclar" class="bg-white hover:bg-slate-100 text-slate-700 font-bold text-sm px-6 py-3 rounded-xl border border-slate-200 shadow-sm transition-all">
                Açık Kaynak Araçlar 🛠️
            </a>
        </div>
    </div>

    <!-- 7 Thematic Portals Section (Cloudflare Pages) -->
    <div id="portallar" class="mt-8 mb-16 scroll-mt-20">
        <div class="flex items-center justify-between mb-8 pb-4 border-b border-slate-200">
            <div>
                <span class="text-xs font-bold text-emerald-600 uppercase tracking-wider">Cloudflare Edge Ağı</span>
                <h2 class="text-2xl sm:text-3xl font-black text-slate-900 mt-0.5">7 Özel E-Dönüşüm Portalı</h2>
            </div>
            <span class="text-xs bg-slate-100 text-slate-600 px-3 py-1 rounded-full font-semibold border border-slate-200">7 Farklı Tasarım & Niş Odak</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <!-- Portal 1 -->
            <a href="https://eimza-rehberi.pages.dev" target="_blank" rel="noopener" class="group bg-white rounded-2xl p-6 border border-slate-200 hover:border-indigo-400 hover:shadow-xl hover:-translate-y-1 transition-all flex flex-col justify-between">
                <div>
                    <div class="w-12 h-12 rounded-xl bg-indigo-50 text-indigo-600 flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition-transform">
                        ✍️
                    </div>
                    <div class="flex items-center gap-2 mb-2">
                        <span class="bg-indigo-50 text-indigo-700 text-[11px] font-bold px-2 py-0.5 rounded-full border border-indigo-100">E-İmza & 5070</span>
                        <span class="text-[11px] text-slate-400 font-medium">eimza-rehberi.pages.dev</span>
                    </div>
                    <h3 class="text-lg font-bold text-slate-900 group-hover:text-indigo-600 transition-colors mb-2">E-İmza Rehberi</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        5070 Sayılı Kanun, USB Token donanımları, AKİS sürücü kurulumları ve Nitelikli Elektronik Sertifika (NES) başvuru süreçleri.
                    </p>
                </div>
                <div class="pt-4 mt-4 border-t border-slate-100 flex items-center justify-between text-xs font-bold text-indigo-600">
                    <span>Portala Git</span>
                    <span class="group-hover:translate-x-1 transition-transform">→</span>
                </div>
            </a>

            <!-- Portal 2 -->
            <a href="https://kep-akademisi.pages.dev" target="_blank" rel="noopener" class="group bg-slate-900 rounded-2xl p-6 border border-slate-800 hover:border-amber-400/50 hover:shadow-xl hover:-translate-y-1 transition-all flex flex-col justify-between text-slate-200">
                <div>
                    <div class="w-12 h-12 rounded-xl bg-amber-500/10 text-amber-400 flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition-transform">
                        📜
                    </div>
                    <div class="flex items-center gap-2 mb-2">
                        <span class="bg-amber-500/10 text-amber-300 text-[11px] font-bold px-2 py-0.5 rounded-full border border-amber-500/20">KEP & Tebligat</span>
                        <span class="text-[11px] text-slate-400 font-medium">kep-akademisi.pages.dev</span>
                    </div>
                    <h3 class="text-lg font-bold text-white group-hover:text-amber-400 transition-colors mb-2">KEP Akademisi</h3>
                    <p class="text-xs text-slate-400 leading-relaxed">
                        Kayıtlı Elektronik Posta ile noter masrafsız ihtarname, delil statüsü, PTT KEP ve TÜRKKEP entegrasyonu.
                    </p>
                </div>
                <div class="pt-4 mt-4 border-t border-slate-800 flex items-center justify-between text-xs font-bold text-amber-400">
                    <span>Portala Git</span>
                    <span class="group-hover:translate-x-1 transition-transform">→</span>
                </div>
            </a>

            <!-- Portal 3 -->
            <a href="https://mali-muhur-merkezi.pages.dev" target="_blank" rel="noopener" class="group bg-[#150709] rounded-2xl p-6 border border-rose-950 hover:border-rose-500/50 hover:shadow-xl hover:-translate-y-1 transition-all flex flex-col justify-between text-rose-100">
                <div>
                    <div class="w-12 h-12 rounded-xl bg-rose-900/30 text-rose-400 flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition-transform">
                        🔴
                    </div>
                    <div class="flex items-center gap-2 mb-2">
                        <span class="bg-rose-900/40 text-rose-300 text-[11px] font-bold px-2 py-0.5 rounded-full border border-rose-800/40">Mali Mühür</span>
                        <span class="text-[11px] text-rose-300/60 font-medium">mali-muhur-merkezi.pages.dev</span>
                    </div>
                    <h3 class="text-lg font-bold text-white group-hover:text-rose-400 transition-colors mb-2">Mali Mühür Merkezi</h3>
                    <p class="text-xs text-rose-200/70 leading-relaxed">
                        TÜBİTAK Kamu SM başvuru süreçleri, şirket kuruluşu, e-Defter berat krizleri ve süresi dolan mühür çözümleri.
                    </p>
                </div>
                <div class="pt-4 mt-4 border-t border-rose-950 flex items-center justify-between text-xs font-bold text-rose-400">
                    <span>Portala Git</span>
                    <span class="group-hover:translate-x-1 transition-transform">→</span>
                </div>
            </a>

            <!-- Portal 4 -->
            <a href="https://efatura-atolyesi.pages.dev" target="_blank" rel="noopener" class="group bg-[#0f071f] rounded-2xl p-6 border border-purple-950 hover:border-purple-500/50 hover:shadow-xl hover:-translate-y-1 transition-all flex flex-col justify-between text-slate-200">
                <div>
                    <div class="w-12 h-12 rounded-xl bg-purple-900/30 text-purple-400 flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition-transform">
                        🧾
                    </div>
                    <div class="flex items-center gap-2 mb-2">
                        <span class="bg-purple-900/40 text-purple-300 text-[11px] font-bold px-2 py-0.5 rounded-full border border-purple-800/40">e-Fatura & e-SMM</span>
                        <span class="text-[11px] text-purple-300/60 font-medium">efatura-atolyesi.pages.dev</span>
                    </div>
                    <h3 class="text-lg font-bold text-white group-hover:text-purple-400 transition-colors mb-2">e-Fatura Atölyesi</h3>
                    <p class="text-xs text-slate-400 leading-relaxed">
                        GİB 5.000/30.000 TL portal kesimi, e-Arşiv, e-İrsaliye karekod zorunluluğu ve serbest meslek makbuzu rehberi.
                    </p>
                </div>
                <div class="pt-4 mt-4 border-t border-purple-950 flex items-center justify-between text-xs font-bold text-purple-400">
                    <span>Portala Git</span>
                    <span class="group-hover:translate-x-1 transition-transform">→</span>
                </div>
            </a>

            <!-- Portal 5 -->
            <a href="https://edonusum-kobi.pages.dev" target="_blank" rel="noopener" class="group bg-white rounded-2xl p-6 border border-slate-200 hover:border-teal-400 hover:shadow-xl hover:-translate-y-1 transition-all flex flex-col justify-between">
                <div>
                    <div class="w-12 h-12 rounded-xl bg-teal-50 text-teal-700 flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition-transform">
                        🏭
                    </div>
                    <div class="flex items-center gap-2 mb-2">
                        <span class="bg-teal-50 text-teal-700 text-[11px] font-bold px-2 py-0.5 rounded-full border border-teal-100">KOBİ & ERP</span>
                        <span class="text-[11px] text-slate-400 font-medium">edonusum-kobi.pages.dev</span>
                    </div>
                    <h3 class="text-lg font-bold text-slate-900 group-hover:text-teal-700 transition-colors mb-2">E-Dönüşüm KOBİ</h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Anadolu KOBİ'leri ve esnaflar için dijital dönüşüm maliyet analizi, KOSGEB teşvikleri ve ERP entegrasyonu.
                    </p>
                </div>
                <div class="pt-4 mt-4 border-t border-slate-100 flex items-center justify-between text-xs font-bold text-teal-700">
                    <span>Portala Git</span>
                    <span class="group-hover:translate-x-1 transition-transform">→</span>
                </div>
            </a>

            <!-- Portal 6 -->
            <a href="https://uyap-teknik-destek.pages.dev" target="_blank" rel="noopener" class="group bg-[#061a12] rounded-2xl p-6 border border-emerald-950 hover:border-emerald-500/50 hover:shadow-xl hover:-translate-y-1 transition-all flex flex-col justify-between text-slate-200">
                <div>
                    <div class="w-12 h-12 rounded-xl bg-emerald-900/30 text-emerald-400 flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition-transform">
                        ⚖️
                    </div>
                    <div class="flex items-center gap-2 mb-2">
                        <span class="bg-emerald-900/40 text-emerald-300 text-[11px] font-bold px-2 py-0.5 rounded-full border border-emerald-800/40">UYAP & Hukuk</span>
                        <span class="text-[11px] text-emerald-300/60 font-medium">uyap-teknik-destek.pages.dev</span>
                    </div>
                    <h3 class="text-lg font-bold text-white group-hover:text-emerald-400 transition-colors mb-2">UYAP Teknik Destek</h3>
                    <p class="text-xs text-emerald-100/70 leading-relaxed">
                        Avukatlar ve hukuk büroları için UYAP Java güvenlik izinleri, UDF editör onarımı ve e-Duruşma bağlantı çözümleri.
                    </p>
                </div>
                <div class="pt-4 mt-4 border-t border-emerald-950 flex items-center justify-between text-xs font-bold text-emerald-400">
                    <span>Portala Git</span>
                    <span class="group-hover:translate-x-1 transition-transform">→</span>
                </div>
            </a>

            <!-- Portal 7 -->
            <a href="https://dijital-kimlik-guvenlik.pages.dev" target="_blank" rel="noopener" class="group bg-[#030712] rounded-2xl p-6 border border-cyan-950 hover:border-cyan-400/50 hover:shadow-xl hover:-translate-y-1 transition-all flex flex-col justify-between text-slate-200 md:col-span-2 lg:col-span-3">
                <div>
                    <div class="w-12 h-12 rounded-xl bg-cyan-950/60 text-cyan-400 flex items-center justify-center text-2xl mb-4 group-hover:scale-110 transition-transform">
                        🔐
                    </div>
                    <div class="flex items-center gap-2 mb-2">
                        <span class="bg-cyan-950/60 text-cyan-300 text-[11px] font-bold px-2 py-0.5 rounded-full border border-cyan-800/40">PKI & Siber Güvenlik</span>
                        <span class="text-[11px] text-cyan-400/60 font-medium">dijital-kimlik-guvenlik.pages.dev</span>
                    </div>
                    <h3 class="text-lg font-bold text-white group-hover:text-cyan-400 transition-colors mb-2">Dijital Kimlik & Siber Güvenlik Laboratuvarı</h3>
                    <p class="text-xs text-slate-400 leading-relaxed max-w-3xl">
                        Açık Anahtarlı Altyapı (PKI), asimetrik şifreleme matematiği, YubiKey FIDO2 donanımları, akıllı kart çipleri ve kurumsal Zero Trust güvenlik mimarileri.
                    </p>
                </div>
                <div class="pt-4 mt-4 border-t border-cyan-950 flex items-center justify-between text-xs font-bold text-cyan-400">
                    <span>Laboratuvarı İncele</span>
                    <span class="group-hover:translate-x-1 transition-transform">→</span>
                </div>
            </a>
        </div>
    </div>

    <!-- Developer & Mobile Channels (Dev.to & Telegram) -->
    <div class="mb-16 bg-gradient-to-br from-slate-900 to-slate-800 rounded-3xl p-8 sm:p-12 text-white shadow-xl">
        <div class="max-w-3xl mb-8">
            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Çok Kanallı Entegrasyon</span>
            <h2 class="text-2xl sm:text-3xl font-black mt-1">Geliştirici & Mobil Kanallarımız</h2>
            <p class="text-slate-300 text-sm mt-2">
                Teknik makalelerimiz DEV.to geliştirici platformunda, anlık duyuru ve hızlı başvuru notlarımız ise Telegram / Telegra.ph ağında yayınlanmaktadır.
            </p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
            <a href="https://dev.to/eimza" target="_blank" rel="noopener" class="bg-white/5 border border-white/10 hover:border-emerald-400/50 rounded-2xl p-6 transition-all hover:bg-white/10 group">
                <div class="flex items-center justify-between mb-4">
                    <span class="text-3xl">💻</span>
                    <span class="text-xs bg-white/10 text-emerald-300 px-3 py-1 rounded-full font-semibold">Geliştirici Blogu</span>
                </div>
                <h3 class="text-lg font-bold text-white group-hover:text-emerald-300 transition-colors">DEV.to @eimza</h3>
                <p class="text-xs text-slate-300 mt-2 leading-relaxed">
                    Yazılım mühendisleri ve sistem yöneticileri için PKI mimarisi, akıllı kart Java/C# entegrasyonu ve kod örnekleri.
                </p>
                <div class="text-xs font-bold text-emerald-400 mt-4 flex items-center gap-1">
                    DEV.to Profilini Gör →
                </div>
            </a>

            <a href="https://telegra.ph/Türkiye-E-Dönüşüm--E-İmza-Rehberi-09-19" target="_blank" rel="noopener" class="bg-white/5 border border-white/10 hover:border-sky-400/50 rounded-2xl p-6 transition-all hover:bg-white/10 group">
                <div class="flex items-center justify-between mb-4">
                    <span class="text-3xl">📱</span>
                    <span class="text-xs bg-white/10 text-sky-300 px-3 py-1 rounded-full font-semibold">Mobil Hızlı Rehber</span>
                </div>
                <h3 class="text-lg font-bold text-white group-hover:text-sky-300 transition-colors">Telegra.ph & Telegram</h3>
                <p class="text-xs text-slate-300 mt-2 leading-relaxed">
                    Sıfır bekleme süreli Instant View uyumlu kılavuzlar, acil durum PIN kurtarma ve operasyonel tebligat rehberleri.
                </p>
                <div class="text-xs font-bold text-sky-400 mt-4 flex items-center gap-1">
                    Hızlı Rehberi Oku →
                </div>
            </a>
        </div>
    </div>

    <!-- 10 Open Source GitHub Utilities Section -->
    <div id="araclar" class="mb-16 scroll-mt-20">
        <div class="flex items-center justify-between mb-8 pb-4 border-b border-slate-200">
            <div>
                <span class="text-xs font-bold text-emerald-600 uppercase tracking-wider">GitHub @eimza-kep</span>
                <h2 class="text-2xl sm:text-3xl font-black text-slate-900 mt-0.5">10 Açık Kaynak E-Dönüşüm Aracı</h2>
            </div>
            <a href="https://github.com/eimza-kep" target="_blank" rel="noopener" class="text-xs bg-slate-900 hover:bg-slate-800 text-white px-3.5 py-1.5 rounded-lg font-bold transition-colors flex items-center gap-1">
                Tüm Repolar ↗
            </a>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            <!-- Repo 1 -->
            <div class="bg-white rounded-xl p-5 border border-slate-200 hover:border-emerald-300 shadow-sm transition-all flex flex-col justify-between">
                <div>
                    <span class="text-xs font-mono font-bold text-emerald-600">eimza-kep /</span>
                    <h3 class="font-bold text-slate-900 text-sm mt-0.5">gib-java-guvenlik-cozucu</h3>
                    <p class="text-xs text-slate-600 mt-2 leading-relaxed">
                        GİB e-Beyanname ve e-Fatura Java güvenlik istisna ve sertifika yapılandırma scripti.
                    </p>
                </div>
                <a href="https://github.com/eimza-kep/gib-java-guvenlik-cozucu" target="_blank" rel="noopener" class="text-xs font-bold text-emerald-600 hover:text-emerald-700 mt-4 flex items-center gap-1">
                    İncele & İndir →
                </a>
            </div>

            <!-- Repo 2 -->
            <div class="bg-white rounded-xl p-5 border border-slate-200 hover:border-emerald-300 shadow-sm transition-all flex flex-col justify-between">
                <div>
                    <span class="text-xs font-mono font-bold text-emerald-600">eimza-kep /</span>
                    <h3 class="font-bold text-slate-900 text-sm mt-0.5">mali-muhur-eimza-suresi-kontrol</h3>
                    <p class="text-xs text-slate-600 mt-2 leading-relaxed">
                        TÜBİTAK Kamu SM & e-İmza sertifika geçerlilik kalan gün sayısını sorgulama aracı.
                    </p>
                </div>
                <a href="https://github.com/eimza-kep/mali-muhur-eimza-suresi-kontrol" target="_blank" rel="noopener" class="text-xs font-bold text-emerald-600 hover:text-emerald-700 mt-4 flex items-center gap-1">
                    İncele & İndir →
                </a>
            </div>

            <!-- Repo 3 -->
            <div class="bg-white rounded-xl p-5 border border-slate-200 hover:border-emerald-300 shadow-sm transition-all flex flex-col justify-between">
                <div>
                    <span class="text-xs font-mono font-bold text-emerald-600">eimza-kep /</span>
                    <h3 class="font-bold text-slate-900 text-sm mt-0.5">akilli-kart-surucu-teshis</h3>
                    <p class="text-xs text-slate-600 mt-2 leading-relaxed">
                        AKİS, Safenet ve Gemalto akıllı kart donanımını otomatik tanıyan ve sürücü durumunu raporlayan araç.
                    </p>
                </div>
                <a href="https://github.com/eimza-kep/akilli-kart-surucu-teshis" target="_blank" rel="noopener" class="text-xs font-bold text-emerald-600 hover:text-emerald-700 mt-4 flex items-center gap-1">
                    İncele & İndir →
                </a>
            </div>

            <!-- Repo 4 -->
            <div class="bg-white rounded-xl p-5 border border-slate-200 hover:border-emerald-300 shadow-sm transition-all flex flex-col justify-between">
                <div>
                    <span class="text-xs font-mono font-bold text-emerald-600">eimza-kep /</span>
                    <h3 class="font-bold text-slate-900 text-sm mt-0.5">python-pdf-eimza-dogrulayici</h3>
                    <p class="text-xs text-slate-600 mt-2 leading-relaxed">
                        ETSI PAdES-BES ve B-LTV dijital imzalarını ve zaman damgasını doğrulayan Python kütüphanesi.
                    </p>
                </div>
                <a href="https://github.com/eimza-kep/python-pdf-eimza-dogrulayici" target="_blank" rel="noopener" class="text-xs font-bold text-emerald-600 hover:text-emerald-700 mt-4 flex items-center gap-1">
                    İncele & İndir →
                </a>
            </div>

            <!-- Repo 5 -->
            <div class="bg-white rounded-xl p-5 border border-slate-200 hover:border-emerald-300 shadow-sm transition-all flex flex-col justify-between">
                <div>
                    <span class="text-xs font-mono font-bold text-emerald-600">eimza-kep /</span>
                    <h3 class="font-bold text-slate-900 text-sm mt-0.5">awesome-turkiye-e-donusum</h3>
                    <p class="text-xs text-slate-600 mt-2 leading-relaxed">
                        Türkiye E-Dönüşüm ekosistemi, mevzuatlar, kütüphaneler ve rehberlerin kürasyon listesi.
                    </p>
                </div>
                <a href="https://github.com/eimza-kep/awesome-turkiye-e-donusum" target="_blank" rel="noopener" class="text-xs font-bold text-emerald-600 hover:text-emerald-700 mt-4 flex items-center gap-1">
                    İncele & İndir →
                </a>
            </div>

            <!-- Repo 6 -->
            <div class="bg-white rounded-xl p-5 border border-slate-200 hover:border-emerald-300 shadow-sm transition-all flex flex-col justify-between">
                <div>
                    <span class="text-xs font-mono font-bold text-emerald-600">eimza-kep /</span>
                    <h3 class="font-bold text-slate-900 text-sm mt-0.5">uyap-editor-hizli-onarim</h3>
                    <p class="text-xs text-slate-600 mt-2 leading-relaxed">
                        Avukatlar için UYAP UDF editör açılmama, Java bellek ve ekran ölçekleme sorunlarını çözen araç.
                    </p>
                </div>
                <a href="https://github.com/eimza-kep/uyap-editor-hizli-onarim" target="_blank" rel="noopener" class="text-xs font-bold text-emerald-600 hover:text-emerald-700 mt-4 flex items-center gap-1">
                    İncele & İndir →
                </a>
            </div>

            <!-- Repo 7 -->
            <div class="bg-white rounded-xl p-5 border border-slate-200 hover:border-emerald-300 shadow-sm transition-all flex flex-col justify-between">
                <div>
                    <span class="text-xs font-mono font-bold text-emerald-600">eimza-kep /</span>
                    <h3 class="font-bold text-slate-900 text-sm mt-0.5">kep-adresi-dogrulayici</h3>
                    <p class="text-xs text-slate-600 mt-2 leading-relaxed">
                        RFC uyumlu hs01, hs02, hs03 uzantılı KEP e-posta adreslerini ve operatör yetkisini doğrulayan araç.
                    </p>
                </div>
                <a href="https://github.com/eimza-kep/kep-adresi-dogrulayici" target="_blank" rel="noopener" class="text-xs font-bold text-emerald-600 hover:text-emerald-700 mt-4 flex items-center gap-1">
                    İncele & İndir →
                </a>
            </div>

            <!-- Repo 8 -->
            <div class="bg-white rounded-xl p-5 border border-slate-200 hover:border-emerald-300 shadow-sm transition-all flex flex-col justify-between">
                <div>
                    <span class="text-xs font-mono font-bold text-emerald-600">eimza-kep /</span>
                    <h3 class="font-bold text-slate-900 text-sm mt-0.5">e-fatura-xml-goruntuleyici</h3>
                    <p class="text-xs text-slate-600 mt-2 leading-relaxed">
                        GİB UBL-TR 1.2 formatındaki e-fatura XML dosyalarını modern HTML olarak render eden görüntüleyici.
                    </p>
                </div>
                <a href="https://github.com/eimza-kep/e-fatura-xml-goruntuleyici" target="_blank" rel="noopener" class="text-xs font-bold text-emerald-600 hover:text-emerald-700 mt-4 flex items-center gap-1">
                    İncele & İndir →
                </a>
            </div>

            <!-- Repo 9 -->
            <div class="bg-white rounded-xl p-5 border border-slate-200 hover:border-emerald-300 shadow-sm transition-all flex flex-col justify-between">
                <div>
                    <span class="text-xs font-mono font-bold text-emerald-600">eimza-kep /</span>
                    <h3 class="font-bold text-slate-900 text-sm mt-0.5">eimza-pin-bloke-asistani</h3>
                    <p class="text-xs text-slate-600 mt-2 leading-relaxed">
                        PUK kodu ile akıllı kart kilit açma ve yeni PIN belirleme adımlarını yönlendiren asistan.
                    </p>
                </div>
                <a href="https://github.com/eimza-kep/eimza-pin-bloke-asistani" target="_blank" rel="noopener" class="text-xs font-bold text-emerald-600 hover:text-emerald-700 mt-4 flex items-center gap-1">
                    İncele & İndir →
                </a>
            </div>

            <!-- Repo 10 -->
            <div class="bg-white rounded-xl p-5 border border-slate-200 hover:border-emerald-300 shadow-sm transition-all flex flex-col justify-between sm:col-span-2 lg:col-span-3">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                    <div>
                        <span class="text-xs font-mono font-bold text-emerald-600">eimza-kep /</span>
                        <h3 class="font-bold text-slate-900 text-sm mt-0.5">gib-edefter-berat-xml-dogrulayici</h3>
                        <p class="text-xs text-slate-600 mt-1 leading-relaxed">
                            GİB e-Defter ve berat XML dosyalarının şema geçerliliğini ve mali mühür imzasını doğrulayan kütüphane.
                        </p>
                    </div>
                    <a href="https://github.com/eimza-kep/gib-edefter-berat-xml-dogrulayici" target="_blank" rel="noopener" class="text-xs font-bold text-emerald-600 hover:text-emerald-700 flex-shrink-0 flex items-center gap-1">
                        İncele & İndir →
                    </a>
                </div>
            </div>
        </div>
    </div>

    <!-- Articles Section -->
    <div class="mb-12">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6 pb-4 border-b border-slate-200">
            <div>
                <span class="text-xs font-bold text-emerald-600 uppercase tracking-wider">Bilgi Bankası</span>
                <h2 class="text-2xl sm:text-3xl font-black text-slate-900 mt-0.5">Teknik Makaleler & Rehberler</h2>
            </div>
            <!-- Search Input -->
            <div class="w-full sm:w-72">
                <input type="text" id="searchInput" placeholder="Makale ara... (ör: USB Token, KEP)" class="w-full px-4 py-2 rounded-xl border border-slate-200 bg-white focus:outline-none focus:ring-2 focus:ring-emerald-500 text-xs shadow-sm">
            </div>
        </div>

        <div class="flex flex-wrap items-center gap-2 mb-6" id="catFilter">
            {cat_filters_html}
        </div>

        <!-- Articles Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6" id="articlesGrid">
            {cards_html}
        </div>
    </div>

    <script>
        const searchInput = document.getElementById('searchInput');
        const catBtns = document.querySelectorAll('.cat-btn');
        const cards = document.querySelectorAll('.article-card');
        let currentCat = 'all';

        function filterCards() {{
            const query = (searchInput ? searchInput.value : '').toLowerCase().trim();
            cards.forEach(card => {{
                const title = card.getAttribute('data-title') || '';
                const cat = card.getAttribute('data-category') || '';
                const matchesSearch = !query || title.includes(query);
                const matchesCat = currentCat === 'all' || cat === currentCat;
                if (matchesSearch && matchesCat) {{
                    card.style.display = 'flex';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}

        if (searchInput) {{
            searchInput.addEventListener('input', filterCards);
        }}

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

    full_index_html = get_base_template("Ana Sayfa", index_content, base_path="./", canonical_url=SITE_URL)
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

    # 4. Build RSS 2.0 Feed & JSON Feed
    rss_items = []
    json_items = []
    for art in articles:
        link = f"{SITE_URL}/posts/{art['slug']}.html"
        desc = art['description'] or art['body_preview']
        esc_title = art['title'].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        rss_items.append(f"""    <item>
      <title>{esc_title}</title>
      <link>{link}</link>
      <guid isPermaLink="true">{link}</guid>
      <pubDate>{art['pub_date']} 00:00:00 +0300</pubDate>
      <category>{art['category']}</category>
      <description><![CDATA[{desc}]]></description>
    </item>""")
        json_items.append({
            "id": link,
            "url": link,
            "title": art['title'],
            "summary": desc,
            "date_published": f"{art['pub_date']}T00:00:00+03:00",
            "tags": [art['category']] if art['category'] else []
        })

    rss_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{SITE_TITLE}</title>
    <link>{SITE_URL}</link>
    <description>{SITE_DESC}</description>
    <language>tr</language>
    <atom:link href="{SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>
{chr(10).join(rss_items)}
  </channel>
</rss>"""

    with open(os.path.join(DIST_DIR, "feed.xml"), "w", encoding="utf-8") as out:
        out.write(rss_xml)
    with open(os.path.join(DIST_DIR, "rss.xml"), "w", encoding="utf-8") as out:
        out.write(rss_xml)

    import json as json_mod
    json_feed = {
        "version": "https://jsonfeed.org/version/1.1",
        "title": SITE_TITLE,
        "home_page_url": SITE_URL,
        "feed_url": f"{SITE_URL}/feed.json",
        "description": SITE_DESC,
        "items": json_items
    }
    with open(os.path.join(DIST_DIR, "feed.json"), "w", encoding="utf-8") as out:
        json_mod.dump(json_feed, out, ensure_ascii=False, indent=2)

    with open(os.path.join(DIST_DIR, "robots.txt"), "w", encoding="utf-8") as out:
        out.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")

    print(f"Done! Built {len(articles)} articles into {DIST_DIR} with RSS & JSON feeds.")

if __name__ == "__main__":
    generate_site()

