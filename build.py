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
    date = meta.get("date", meta.get("pub_date", ""))
    
    if hasattr(date, "isoformat"):
        date = date.isoformat()
    
    body_clean = re.sub(r'!\[(.*?)\]\(/images/(.*?)\)', r'> 🖼️ *[\1]*\n', body)
    html_content = markdown.markdown(body_clean, extensions=["fenced_code", "tables", "toc", "nl2br"])

    return {
        "title": title,
        "slug": slugify(filename),
        "pub_date": date,
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
        .glass-header {{ background: rgba(255,255,255,0.8); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(0,0,0,0.05); }}
        .prose h1, .prose h2, .prose h3 {{ font-weight: 700; letter-spacing: -0.02em; margin-top: 1.5em; margin-bottom: 0.5em; }}
        .prose h1 {{ font-size: 2.25rem; }}
        .prose h2 {{ font-size: 1.5rem; }}
        .prose p {{ line-height: 1.7; color: #3f3f46; margin-bottom: 1.2em; }}
        .prose a {{ color: #000; text-decoration: underline; text-underline-offset: 4px; }}
        .prose pre {{ background: #09090b; color: #fafafa; padding: 1.5rem; border-radius: 8px; overflow-x: auto; margin-bottom: 1.5em; }}
        .prose code {{ font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace; font-size: 0.875em; }}
        .card-hover {{ transition: all 0.2s ease; border: 1px solid #e4e4e7; background: #fff; }}
        .card-hover:hover {{ border-color: #000; transform: translateY(-2px); box-shadow: 0 10px 30px -10px rgba(0,0,0,0.05); }}
    </style>
</head>
<body class="antialiased flex flex-col min-h-screen">
    <!-- Navbar -->
    <header class="glass-header sticky top-0 z-50">
        <div class="max-w-5xl mx-auto px-6 h-16 flex items-center justify-between">
            <a href="{base_path}" class="flex items-center gap-2 text-black hover:opacity-80 transition-opacity">
                <i class="ph-fill ph-code text-2xl"></i>
                <span class="font-bold tracking-tight text-lg">eimza.dev</span>
            </a>
            <nav class="flex items-center gap-6">
                <a href="{base_path}" class="text-sm font-medium text-gray-600 hover:text-black">Projeler</a>
                <a href="{base_path}hakkimizda.html" class="text-sm font-medium text-gray-600 hover:text-black">Hakkımızda</a>
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
        <p class="text-sm text-gray-500 flex items-center justify-center gap-2">
            <i class="ph-fill ph-check-circle text-green-500"></i>
            Açık Kaynak LegalTech & E-Dönüşüm İnisiyatifi
        </p>
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
        post_html = f"""
        <article class="max-w-3xl mx-auto px-6 py-16">
            <a href="../" class="inline-flex items-center gap-2 text-sm font-medium text-gray-500 hover:text-black mb-8 transition-colors">
                <i class="ph ph-arrow-left"></i> Geri Dön
            </a>
            <h1 class="text-3xl sm:text-4xl font-bold tracking-tight text-black mb-4 leading-tight">{art["title"]}</h1>
            <div class="flex items-center gap-4 text-sm text-gray-500 mb-10 pb-10 border-b border-gray-100">
                <span class="flex items-center gap-1"><i class="ph ph-calendar-blank"></i> {art["pub_date"][:10] if art["pub_date"] else "Geliştiriliyor"}</span>
                <span class="flex items-center gap-1"><i class="ph ph-tag"></i> Açık Kaynak</span>
            </div>
            <div class="prose">
                {art["html"]}
            </div>
        </article>
        """
        full_html = get_base_template(art["title"], post_html, base_path="../", canonical_url=post_url)
        with open(os.path.join(DIST_DIR, "posts", f"{art['slug']}.html"), "w", encoding="utf-8") as out:
            out.write(full_html)

    # 2. Build Index Page
    cards_html = ""
    for art in articles:
        cards_html += f"""
        <a href="posts/{art['slug']}.html" class="card-hover rounded-2xl p-6 flex flex-col justify-between h-full group">
            <div>
                <div class="w-10 h-10 rounded-full bg-gray-100 flex items-center justify-center text-gray-800 mb-4 group-hover:bg-black group-hover:text-white transition-colors">
                    <i class="ph-fill ph-code-block text-xl"></i>
                </div>
                <h3 class="text-xl font-bold tracking-tight text-gray-900 mb-2 leading-snug">{art["title"]}</h3>
            </div>
            <div class="mt-6 flex items-center justify-between text-sm text-gray-500 font-medium">
                <span>Devamını Oku</span>
                <i class="ph ph-arrow-right group-hover:translate-x-1 transition-transform"></i>
            </div>
        </a>
        """

    index_content = f"""
    <div class="max-w-5xl mx-auto px-6 pt-20 pb-16 text-center">
        <div class="inline-flex items-center gap-2 bg-black text-white text-xs font-bold px-3 py-1.5 rounded-full mb-6">
            <span class="w-2 h-2 rounded-full bg-green-400 animate-pulse"></span> %100 Açık Kaynak
        </div>
        <h1 class="text-4xl sm:text-6xl font-bold tracking-tighter text-black mb-6">
            Dijital Dönüşüm<br>Geliştirici Merkezi
        </h1>
        <p class="text-lg text-gray-600 max-w-2xl mx-auto leading-relaxed">
            E-İmza, KEP, UYAP, e-Fatura ve LegalTech ekosistemi için tamamen ücretsiz, açık kaynaklı kod kütüphaneleri ve projeler.
        </p>
    </div>

    <div class="max-w-5xl mx-auto px-6 pb-24">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            {cards_html}
        </div>
    </div>
    """

    index_html = get_base_template("Açık Kaynak Projeler", index_content, base_path="./")
    with open(os.path.join(DIST_DIR, "index.html"), "w", encoding="utf-8") as out:
        out.write(index_html)

    # 3. Build About (Hakkımızda) Page
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

    print(f"Done! Built {len(articles)} articles and new About page into {DIST_DIR}.")

if __name__ == "__main__":
    generate_site()
