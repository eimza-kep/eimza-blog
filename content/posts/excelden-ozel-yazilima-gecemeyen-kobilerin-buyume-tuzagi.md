---
title: "Excel'e Sıkışan KOBİ'ler: Özel Yazılıma (ERP) Geçiş Sancısı"
slug: "excelden-ozel-yazilima-gecemeyen-kobilerin-buyume-tuzagi"
description: "Erzurum gibi şehirlerde büyümeye başlayan aile şirketlerinin neden Excel'de takılı kaldığı ve kurumsal yazılımlara (ERP) adaptasyon sorunu."
---

# Excel Tablolarında Boğulan KOBİ'lerin ERP Sancısı

Bir firmanın patronu bana geçen yıl şunu söyledi: "Hocam biz Excel'i çok iyi kullanıyoruz, her şeyimiz Excel'de." Sonra o Excel dosyasını açtık. 127 sütunluk bir canavar. Makrolar birbirine girmiş, formüller çoktan kırılmış, bazı hücrelerde 2019'dan kalma veriler var. Firmadaki 4 kişi aynı dosyanın 4 farklı kopyası üzerinde çalışıyor ve ay sonunda "hangisi doğru?" kavgası çıkıyor.

Bu tablo Erzurum'a, Kayseri'ye, Konya'ya özgü değil. Dünya genelinde KOBİ'lerin ezici çoğunluğu, **büyüme eşiğine geldiğinde Excel'in duvarına çarpıyor** ama o duvarı aşacak cesareti bulamıyor. Çünkü ERP (Kurumsal Kaynak Planlama) gibi özel yazılımlar; hem pahalı görünüyor, hem karmaşık görünüyor, hem de "mevcut düzeni bozacak" korkusu yaratıyor. Oysa asıl bozulan şey, Excel'deki o kırılgan düzen.

## Excel Tam Olarak Nerede Tıkanır?

Excel mükemmel bir araçtır — hesap tablosu olarak. Ama onu bir **işletme yönetim sistemi** gibi kullanmaya kalktığınızda şu noktada çöker:

| İşlev | Excel'de Ne Olur | ERP/Özel Yazılımda Ne Olur |
|:---|:---|:---|
| **Sipariş Gelişi** | WhatsApp'tan mesaj gelir, biri Excel'e yazar (ya da unutur) | Sipariş otomatik sisteme düşer, stok düşer, irsaliye hazırlanır |
| **Stok Kontrolü** | 4 farklı dosya, 4 farklı rakam, "hangisi doğru?" | Tek kaynak (Single Source of Truth), anlık güncelleme |
| **Fiyatlandırma** | "Bu müşteriye kaça vermiştik?" sorusu, cevap yok | Müşteri bazlı fiyat listeleri, geçmiş alım/satım analizi |
| **Cari Hesap** | "Şu firma bize ne kadar borçlu?" → 20 dk arama | Tek tıkla bakiye, vade analizi, otomatik hatırlatma |
| **Raporlama** | "Bu ay kâr ettik mi?" → "Bilmiyorum, muhasebeci söylesin" | Anlık kâr/zarar dashboardı, ürün bazlı maliyet analizi |

Gartner'ın 2024 yılında yayımladığı "Technology Adoption in Midsize Enterprises" araştırmasına göre, **yıllık cirosu 2-10 milyon dolar arasındaki firmaların %71'i hâlâ temel iş süreçlerini Excel veya benzeri hesap tablolarıyla yönetiyor.** Aynı rapor, bu firmalardan ERP'ye geçenlerin ortalama **%23 operasyonel verimlilik artışı** sağladığını gösteriyor.

## "Yazılım Pahalı" Yalanı

Erzurum'da bir firmaya ERP teklifi götürdüğümüzde ilk duyduğumuz cümle şudur: "Çok pahalı." Peki neye göre pahalı?

Bir düşünelim. O firmanın Excel'deki veri karmaşası yüzünden:
- Ay sonunda **2 gün** muhasebeci ile veri eşleştirme yapılıyor (2 kişi × 2 gün = 4 adam/gün iş gücü kaybı)
- Stok hatası yüzünden yılda en az **3-4 kez** yanlış sevkiyat yapılıyor (iade nakliyesi + müşteri kaybı)
- Müşteri borç takibi yapılamadığı için tahsil edilemeyen alacaklar birikiyor

Bu kayıpları topladığınızda, orta ölçekli bir ERP yazılımının **3-5 yıllık toplam maliyetini** tek yılda çıkarıyorsunuz. Yazılım pahalı değil; yazılımsızlık pahalı.

## Almanya'daki Mittelstand Modeli: Küçük Ama Dijital

Almanya ekonomisinin bel kemiği, "Mittelstand" olarak adlandırılan küçük ve orta ölçekli aile şirketleridir. Bu firmalar genellikle 50-500 çalışanlı, niş ürünlere odaklanmış, kuşaklar boyu aynı ailenin yönettiği yapılardır. Erzurum'daki veya Kayseri'deki aile şirketlerine çok benzerler.

Fark şu: Alman Mittelstand firmaları, **üretim ve iş süreçlerini dijitalleştirmeyi bir tercih değil, hayatta kalma şartı** olarak görüyor. Fraunhofer Enstitüsü'nün 2023 raporuna göre Mittelstand firmalarının **%89'u** en az bir ERP veya MES (Üretim Yürütme Sistemi) kullanıyor. Firma küçük olabilir ama verisi dijital, karar alma süreci veriye dayalı.

Erzurum'daki bir gıda üreticisi veya mobilyacı, çalışan sayısı olarak bir Alman Mittelstand firmasından farklı değil. Ama operasyonel olgunluk açısından 30 yıl geride. Bu fark, ne coğrafyadan ne de sermayeden kaynaklanıyor — tamamen **zihniyetten**.

## Geçişin Acı Vermeden Yapılması Mümkün mü?

Mümkün; ama koşullu. Sahada gördüğüm en büyük ERP başarısızlıklarının sebebi yazılımın kendisi değil, **geçiş sürecinin yönetilememesi**. Patron "Al şunu kur" diyor, yazılım firması uzaktan kurulumu yapıp gidiyor, personel 2 hafta sonra eski Excel'ine dönüyor.

Başarılı bir geçiş için gördüğüm en işe yarayan yöntem:

- **Paralel çalışma dönemi:** İlk 2-3 ay hem Excel'i hem yeni yazılımı birlikte kullan. Personele "Eski sisteminizi alıyorum" deme; "Yenisini de deneyin, hangisi rahat gelirse" de. İnsanlar zorlanınca kaçar, seçme hakkı verince dener.
- **Şampiyon kullanıcı (Champion User) ata:** Firmadaki en teknoloji meraklısı kişiyi bul, onu eğit, onu "iç danışman" yap. Dışarıdan gelen danışmana güvenmeyen esnaf, kendi çalışanına güvenir.
- **Küçük başla:** Tüm modülleri aynı anda açma. Önce sadece stok ve cari hesap ile başla. Personel buna alışınca üretim, sipariş yönetimi gibi modülleri ekle.

Dünya Bankası'nın 2022 "Small Business Digital Transformation Toolkit" raporunda da aynı yaklaşım önerilmektedir: **"Incremental digitization" (aşamalı dijitalleşme)**, KOBİ'lerde toptan dönüşümden %60 daha yüksek başarı oranına sahip.

## Korkuyu Yenmek İçin Rakibi İzlemek Yeterli

Bir Erzurum firmasına ERP anlatırken ikna edemiyordum. Sonra aynı sektördeki Gaziantep'li bir rakiplerinin, yazılım sayesinde sipariş-teslim süresini 7 günden 2 güne indirdiğini ve büyük zincir marketlerden iş aldığını gösterdim. Patron 10 dakikada karar verdi.

Rekabet baskısı, herhangi bir danışmanın sunumundan daha ikna edicidir. Erzurum'daki firmalar, Batı'daki veya Güneydoğu'daki rakiplerinin dijitalleşerek kazandığı hız ve maliyet avantajını görmezden gelmeye devam ederse, 5 yıl sonra o rakiplere alt bayilik yapmak zorunda kalacaklar. Excel'de "günü kurtarmak" ile yazılımda "geleceği kurmak" arasındaki fark budur.

---

*Kaynaklar: Gartner, "Technology Adoption in Midsize Enterprises" (2024) · Fraunhofer Institut, "Digitalization in German Mittelstand" (2023) · World Bank Group, "Small Business Digital Transformation Toolkit" (2022) · KOSGEB, KOBİ Stratejisi ve Eylem Planı (2024-2028)*
