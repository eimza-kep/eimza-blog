# Türkiye E-Dönüşüm & Dijital İmza Yayın Ekosistemi

[![CI Tests](https://github.com/eimza-kep/eimza-blog/actions/workflows/ci.yml/badge.svg)](https://github.com/eimza-kep/eimza-blog/actions/workflows/ci.yml)
[![GitHub Pages](https://github.com/eimza-kep/eimza-blog/actions/workflows/deploy.yml/badge.svg)](https://github.com/eimza-kep/eimza-blog/actions/workflows/deploy.yml)
[![Canlı Blog](https://img.shields.io/badge/Demo-Canl%C4%B1%20Blog-brightgreen.svg)](https://eimza-kep.github.io/eimza-blog/)
[![RSS 2.0 Feed](https://img.shields.io/badge/RSS-2.0%20Feed-orange.svg)](https://eimza-kep.github.io/eimza-blog/feed.xml)
[![JSON Feed](https://img.shields.io/badge/JSON-Feed%201.1-blue.svg)](https://eimza-kep.github.io/eimza-blog/feed.json)

Bu merkez depo (**eimza-blog**), Türkiye'deki e-imza, KEP, mali mühür, e-fatura ve dijital dönüşüm konularında kurulmuş çok kanallı dijital yayın ve açık kaynak ağının ana merkezidir.

---

## ⚡ Temel Özellikler

- **%100 İstemci Taraflı Canlı Arama (Vanilla JS):** Herhangi bir harici npm/CDN bağımlılığı olmaksızın makale başlıkları, özetleri, etiketleri ve kategorilerinde anlık arama.
- **Kategori Filtreleme Çipleri:** E-İmza & Donanım, E-Dönüşüm, Başvuru Rehberi, Pratik İpuçları gibi niş kategorilerde tek tıkla filtreleme ve sayaç.
- **RSS 2.0 & JSON Feed 1.1:** Tüm standart RSS okuyucular ve otomasyonlar için RFC-822 uyumlu `feed.xml` ve `feed.json` yayını.
- **Sıfır Sunucu Maliyeti & Maksimum Hız:** Saf Python ile Markdown'dan statik HTML'e dönüştürme; GitHub Pages & Cloudflare Pages ile CDN üzerinden sıfır bekleme süresiyle sunum.

---

## 🚀 Kurulum ve Yerel Geliştirme (Local Development)

Projeyi yerel bilgisayarınızda çalıştırmak ve test etmek için aşağıdaki adımları izleyin:

### 1. Gereksinimler
- **Python 3.9+** (Python 3.10, 3.11 veya 3.12 önerilir)
- **Git**

### 2. Depoyu Klonlayın
```bash
git clone https://github.com/eimza-kep/eimza-blog.git
cd eimza-blog
```

### 3. Sanal Ortam Oluşturun ve Bağımlılıkları Yükleyin
```bash
# Sanal ortam oluşturma (isteğe bağlı ancak önerilir)
python -m venv venv

# Sanal ortamı aktive edin
# Windows:
venv\Scripts\activate
# Linux / macOS:
source venv/bin/activate

# Gerekli bağımlılıkları yükleyin
pip install -r requirements.txt
```

### 4. Blogu Derleyin (Build)
Markdown dosyalarını derleyip `dist/` klasörüne HTML, CSS, RSS (`feed.xml`) ve JSON (`feed.json`) çıktıları üretmek için:
```bash
python build.py
```
*Derleme tamamlandığında `Done! Built X articles, About page, feed.xml, and feed.json into .../dist.` çıktısını göreceksiniz.*

### 5. Yerel Web Sunucusunu Başlatın
Oluşturulan `dist/` klasörünü yerelde görüntülemek için:
```bash
python -m http.server -d dist 8000
```
Tarayıcınızda [http://localhost:8000](http://localhost:8000) adresine giderek blogu, arama çubuğunu ve kategori filtrelerini inceleyebilirsiniz.

### 6. Birim Testleri Çalıştırın
Tüm yapılandırmaları, slug üretimini, arama filtre bileşenlerini ve feed sözdizimini doğrulamak için:
```bash
python -m unittest test_build.py
```

---

## ✍️ Yeni Makale veya Rehber Ekleme

`content/posts/` klasörü altına yeni bir `.md` dosyası ekleyerek sisteme yeni içerik kazandırabilirsiniz.

Örnek dosya yapısı: `content/posts/yeni-rehber-basligi.md`

```markdown
---
title: "macOS Sequoia Üzerinde AKİS E-İmza Kurulumu"
description: "Apple Silicon M serisi işlemcili Mac'lerde e-imza kartlarının yapılandırılması ve UYAP entegrasyonu."
category: "E-İmza & Donanım"
pubDate: "2026-10-23"
author: "Teknik Ekip"
tags: ["akis", "macos", "e-imza", "uyap"]
---

# macOS Sequoia Üzerinde AKİS E-İmza Kurulumu

İçerik buraya Markdown formatında yazılır...
```

Yeni dosyayı kaydettikten sonra `python build.py` komutu ile `dist/` içeriğini güncelleyebilirsiniz.

---

## 🌐 Özel Tematik Portallar (Cloudflare Pages)

Her biri bağımsız tasarıma, özgün renk paletine ve odaklanmış bir niş kitleye sahip 7 Cloudflare Pages portalı:

| # | Portal Adı | Niş Odak & Konu | Canlı URL |
|---|---|---|---|
| 1 | **E-İmza Rehberi** | 5070 Sayılı Kanun, USB Token donanımları, AKİS sürücüleri, NES | [eimzabilgi.site](https://eimzabilgi.site) |
| 2 | **KEP Akademisi** | Kayıtlı Elektronik Posta, noter masrafsız ihtarname, delil güvenliği | [keprehberi.site](https://keprehberi.site) |
| 3 | **Mali Mühür Merkezi** | TÜBİTAK Kamu SM başvuru, şirket kuruluşu, e-Defter kriz yönetimi | [malimuhur.site](https://malimuhur.site) |
| 4 | **e-Fatura Atölyesi** | GİB Portal, e-Arşiv, e-İrsaliye karekod, serbest meslek makbuzu (e-SMM) | [efaturabilgi.site](https://efaturabilgi.site) |
| 5 | **E-Dönüşüm KOBİ** | KOBİ'ler ve esnaflar için ERP uyumu, KOSGEB teşvikleri, maliyet analizi | [edonusumkobi.site](https://edonusumkobi.site) |
| 6 | **UYAP Teknik Destek** | Avukatlar için UYAP Java güvenlik izinleri, UDF editör onarımı | [uyapteknikdestek.site](https://uyapteknikdestek.site) |
| 7 | **Dijital Kimlik Lab** | PKI mimarisi, kriptografi, RSA/ECC, YubiKey FIDO2, Zero Trust | [kimlikguvenlik.site](https://kimlikguvenlik.site) |

---

## 🛠️ Açık Kaynak E-Dönüşüm Araçları (GitHub Repoları)

Organik arama trafiği ve geliştirici güveni oluşturan 10 açık kaynak GitHub projesi:

1. [eimza-kep/gib-java-guvenlik-cozucu](https://github.com/eimza-kep/gib-java-guvenlik-cozucu) - GİB Java güvenlik istisna ve sertifika yapılandırma scripti
2. [eimza-kep/mali-muhur-eimza-suresi-kontrol](https://github.com/eimza-kep/mali-muhur-eimza-suresi-kontrol) - Mali mühür ve e-imza kalan geçerlilik süresi sorgulama aracı
3. [eimza-kep/akilli-kart-surucu-teshis](https://github.com/eimza-kep/akilli-kart-surucu-teshis) - Windows/Linux AKİS, Safenet, Gemalto kart tanılama yardımcısı
4. [eimza-kep/python-pdf-eimza-dogrulayici](https://github.com/eimza-kep/python-pdf-eimza-dogrulayici) - ETSI PAdES-BES/B-LTV dijital imza doğrulama kütüphanesi
5. [eimza-kep/awesome-turkiye-e-donusum](https://github.com/eimza-kep/awesome-turkiye-e-donusum) - Türkiye E-Dönüşüm ekosistemi açık kaynak ve mevzuat arşivi
6. [eimza-kep/uyap-editor-hizli-onarim](https://github.com/eimza-kep/uyap-editor-hizli-onarim) - UYAP UDF editör açılmama ve Java hata onarım aracı
7. [eimza-kep/kep-adresi-dogrulayici](https://github.com/eimza-kep/kep-adresi-dogrulayici) - RFC uyumlu hs01/hs02/hs03 KEP adresi sözdizim doğrulayıcı
8. [eimza-kep/e-fatura-xml-goruntuleyici](https://github.com/eimza-kep/e-fatura-xml-goruntuleyici) - GİB UBL-TR 1.2 XML faturaları HTML olarak render eden görüntüleyici
9. [eimza-kep/eimza-pin-bloke-asistani](https://github.com/eimza-kep/eimza-pin-bloke-asistani) - PUK kodu ile akıllı kart kilit açma ve yeni PIN belirleme asistanı
10. [eimza-kep/gib-edefter-berat-xml-dogrulayici](https://github.com/eimza-kep/gib-edefter-berat-xml-dogrulayici) - GİB e-Defter ve berat XML dosyaları şema ve imza doğrulayıcı

---

## 🏛️ Yayın Bağlantıları

* **GitHub Pages:** [https://eimza-kep.github.io/eimza-blog/](https://eimza-kep.github.io/eimza-blog/)
* **Cloudflare Mirror:** [https://eimza-blog.pages.dev](https://eimza-blog.pages.dev)
* **RSS 2.0 Feed:** [https://eimza-kep.github.io/eimza-blog/feed.xml](https://eimza-kep.github.io/eimza-blog/feed.xml)
* **JSON Feed 1.1:** [https://eimza-kep.github.io/eimza-blog/feed.json](https://eimza-kep.github.io/eimza-blog/feed.json)
* **DEV.to Mühendislik Blogu:** [dev.to/eimza](https://dev.to/eimza)
* **Telegram / Telegra.ph Mobil Kılavuz:** [telegra.ph/Türkiye-E-Dönüşüm--E-İmza-Rehberi-09-19](https://telegra.ph/Türkiye-E-Dönüşüm--E-İmza-Rehberi-09-19)

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) kapsamında açık kaynak olarak geliştirilmektedir.
