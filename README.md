# E-İmza & Dijital Dönüşüm Blog Portalı

Bu blog, **Antigravity AI Ajanı** tarafından otomatik olarak yönetilmek ve yayınlanmak üzere kurulmuştur.

## Canlı Yayın Adresleri
* **Cloudflare Pages:** [https://eimza-blog.pages.dev](https://eimza-blog.pages.dev)
* **GitHub Pages:** [https://eimza-kep.github.io/eimza-blog/](https://eimza-kep.github.io/eimza-blog/)

## Nasıl Çalışır?
1. Yeni makaleler `content/posts/` klasörüne Markdown (`.md`) formatında eklenir.
2. Depoya commit/push yapıldığında **GitHub Actions** devreye girer:
   - `build.py` çalıştırılarak tüm makaleler statik HTML'e derlenir.
   - Cloudflare Pages ve GitHub Pages'e aynı anda 15-20 saniyede otomatik yüklenir.
