---
title: "GİB e-Belge ve e-Defter Portalı 'Java Security Blocked' Engeli Kesin Çözümü"
description: "Mali müşavirler ve şirketlerin GİB portallarında e-imza veya mali mühür kullanırken sıkça karşılaştığı Java güvenlik (Security Exception) engelinin adımlarla çözümü."
pubDate: "2026-09-17"
category: "Teknik Destek"
author: "E İmza Erzurum"
---

Mali müşavirlerin, şirketlerin muhasebe departmanlarının ve serbest meslek erbaplarının e-Dönüşüm sürecinde en çok vakit geçirdiği platform Gelir İdaresi Başkanlığı'nın (GİB) sunduğu e-Belge, e-Defter ve İnteraktif Vergi Dairesi portallarıdır. 

Fatura kesmek, defter beratı göndermek veya MERSİS'te işlem yapmak için e-imzanızı/mali mührünüzü taktınız, "İmzala" butonuna bastınız ve karşınıza o can sıkıcı pencere çıktı: **"Application Blocked by Java Security"** veya **"Security Exception"**.

Bu uyarı, cihazınızın bozulduğu anlamına gelmez; tamamen bilgisayarınızdaki Java yazılımının güvenlik protokolleriyle ilgili bir ayar eksikliğidir. Bu rehberde, Erzurum'daki muhasebecilerimizin en çok şikayet ettiği bu Java engelini dakikalar içinde nasıl kalıcı olarak çözeceğinizi anlatıyoruz.

![Java Security Blocked Hatası Ekranı](/images/blog/gib-java-security-blocked.webp)

## Java Neden GİB Portallarını Engelliyor?

Java platformu, internet üzerinden bilgisayarınızın donanımlarına (bu durumda USB portuna takılı e-imzanıza) erişmek isteyen uygulamaları varsayılan olarak "potansiyel risk" (güvenlik açığı) kabul eder. 

Özellikle Oracle'ın Java 8 ve üzeri sürümlerindeki katı güvenlik politikaları gereği, sertifikası güncel olmayan veya Java'nın "Güvenilir Siteler" listesine (Exception Site List) manuel olarak eklenmemiş hiçbir web sayfasının bilgisayarınızdaki e-imza kütüphanesini çalıştırmasına izin verilmez.

## Adım Adım Java Güvenlik Engeli Çözümü

Ekranda "Blocked" hatası aldığınızda, tarayıcıyı kapatıp açmak veya e-imzayı çıkarıp takmak işe yaramaz. Şu adımları sırasıyla uygulamalısınız:

### 1. Adım: Java Control Panel'i Açın
* Bilgisayarınızın ekranının sol altındaki Windows "Başlat" (Arama) çubuğuna tıklayın.
* Klavyeden `Configure Java` veya `Java` yazın ve çıkan uygulamayı açın. 
* Karşınıza "Java Control Panel" adlı küçük bir pencere çıkacaktır.

### 2. Adım: Security (Güvenlik) Sekmesine Geçiş
* Üstteki sekmelerden **Security** (Güvenlik) sekmesine tıklayın.
* Ekranda "Enable Java content for browser and Web Start applications" kutucuğunun işaretli olduğundan emin olun.
* Güvenlik seviyesinin (Security Level) "High" (Yüksek) olarak ayarlı olduğunu göreceksiniz. (Bunu Very High yapmayın).

### 3. Adım: Exception Site List (İstisna Listesi) Ekleme
* Aynı pencerenin alt kısmında yer alan **"Edit Site List..."** butonuna tıklayın.
* Açılan yeni kutucukta **"Add"** (Ekle) butonuna basın.
* İmza atmaya çalıştığınız, hata veren sitenin tam adresini (Örneğin: `https://earsivportal.efatura.gov.tr/` veya `https://ebelge.gib.gov.tr/`) kopyalayın ve boş satıra yapıştırın.
* **Önemli:** Adresin mutlaka `https://` veya `http://` ile başlaması ve sonunda `/` (slash) işareti olması işi garantiye alır.

| Sık Kullanılan İstisna Adresleri | Kullanım Yeri |
| :--- | :--- |
| `https://earsivportal.efatura.gov.tr/` | GİB e-Arşiv / e-SMM Fatura Kesimi |
| `https://mersis.gtb.gov.tr/` | Ticaret Bakanlığı MERSİS İşlemleri |
| `https://ekap.kik.gov.tr/` | Kamu İhale Kurumu (e-Teklif) |

### 4. Adım: Kaydet ve Tarayıcıyı Yeniden Başlat
* Adresleri ekledikten sonra "OK" butonuna basarak pencereleri kapatın. 
* Karşınıza bir güvenlik uyarısı çıkarsa "Continue" diyerek devam edin.
* En kritik nokta: **Açık olan tüm Google Chrome, Edge veya Firefox tarayıcılarınızı tamamen kapatın.**
* Tarayıcıyı yeniden açıp GİB portalına girdiğinizde Java uygulamasının artık engellenmediğini, küçük bir onay (Run) penceresi çıkararak imza atmanıza izin verdiğini göreceksiniz.

![Java Exception Site List Ekleme](/images/blog/java-exception-site-list-ekleme.webp)

## Erzurum'da Çözemediğiniz Java Sorunları İçin Buradayız

Bazen bilgisayarda birden fazla Java sürümü yüklü olduğunda veya Windows güvenlik duvarı (Antivirüs) devreye girdiğinde, yukarıdaki adımları yapsanız bile e-imzanız çalışmayabilir. Fatura kesmek veya defter göndermek için vaktiniz daralıyorsa strese girmeyin.

> **Teknik Destek İçin Bizi Arayın:**
> **E İmza Erzurum** olarak, mali müşavirlerimizin ve firmalarımızın e-Dönüşüm krizlerinde yanındayız. Uzak masaüstü bağlantısı ile veya Erzurum merkez ofisinize gelerek Java ve e-imza sorunlarınızı kalıcı olarak çözüyoruz. Detaylı bilgi ve destek için **0442 606 08 86** numarasından hemen bize ulaşabilirsiniz.
