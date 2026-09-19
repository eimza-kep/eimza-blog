---
title: "Hekimler İçin SGK Medula e-Reçete: e-İmza Kurulumu ve 'Sertifika Okunamadı' Hatası Çözümü"
description: "Erzurum'daki doktorlar, diş hekimleri ve aile hekimleri için SGK Medula e-reçete sisteminde yaşanan e-imza kilitlenmeleri, Java hataları ve hızlı çözüm yolları."
pubDate: "2026-09-17"
category: "E-İmza"
author: "E İmza Erzurum"
---

Erzurum Şehir Hastanesi'nde, Atatürk Üniversitesi Araştırma Hastanesi'nde, ASM'lerde veya kendi özel muayenehanesinde görev yapan hekimlerimiz için **e-İmza**, tıpkı stetoskop gibi günlük mesleğin ayrılmaz bir parçasıdır. Sağlık Bakanlığı ve SGK mevzuatları gereği, hastaya yazılan e-reçetelerin, düzenlenen raporların ve Medula sistemine girilen tüm verilerin elektronik ortamda yasal olarak imzalanması zorunludur.

Ancak poliklinik kapısında onlarca hasta beklerken, bilgisayar ekranında beliren **"Sertifika Okunamadı"** veya **"E-İmza Uygulaması Başlatılamıyor"** hatası, hekimler için ciddi bir stres kaynağıdır. Bu rehberde, Medula sisteminde e-imza ile reçete yazarken yaşanan teknik krizleri ve bu krizlerin kalıcı çözüm yöntemlerini ele alıyoruz.

![Hekim e-Reçete ve e-İmza Medula Sistemi](/images/blog/medula-e-recete-e-imza.webp)

## E-Reçete Yazabilmek İçin Teknik Gereksinimler

SGK Medula ve AHBS (Aile Hekimliği Bilgi Sistemi) yazılımlarının e-imza modülleri büyük oranda Java altyapısına dayanır. Sistemin sorunsuz çalışması için hekimin bilgisayarında şu bileşenlerin tam ve birbiriyle uyumlu çalışması şarttır:

1. **E-İmza Cihazı (Nitelikli Elektronik Sertifika):** Geçerliliği devam eden, T.C. Kimlik numarasına tanımlı kişisel e-imza (Genelde USB token şeklindedir).
2. **Akıllı Kart Sürücüleri:** AKİS, ArkSigner, Safesign gibi USB'nin çipini okuyacak donanım sürücüleri.
3. **Güncel Java (JRE):** Tarayıcı veya masaüstü uygulamanın sertifika ile iletişimini sağlayan yazılım köprüsü.

### Medula e-Reçete Sisteminde En Sık Karşılaşılan E-İmza Hataları

Hekimlerimizden bize gelen acil destek taleplerinde şu üç hata başı çekmektedir:

| Hata Kodu / Mesajı | Olası Sebebi | Çözüm Önerisi |
| :--- | :--- | :--- |
| **"Sertifika (Akıllı Kart) Okunamadı"** | USB tam takılmamış, kart sürücüsü (AKİS vb.) yüklü değil veya e-imza süresi dolmuş. | Farklı bir USB girişine takın. Akis Kart İzleme Aracı'nı açıp sertifikayı görüp görmediğinizi test edin. |
| **"PIN Kilitli / Bloke Edildi"** | Yoğunlukta PIN (şifre) 3 kez üst üste yanlış girilmiş. | E-imza sağlayıcınızın (Örn: Kamu SM veya özel servis) kilit çözme uygulamasından PUK kodu ile sıfırlama yapın. |
| **"Java Security Exception / Blocked"** | Medula veya hastane yazılımının adresi Java güvenlik ayarlarına eklenmemiştir. | Denetim Masası > Java Control Panel > Security yolunu izleyip Exception Site List alanına Medula adresini ekleyin. |

## Hastanelerde "Ortak Bilgisayar" Sendromu

Hekimlerimizin en çok zorlandığı konulardan biri de hastanelerdeki nöbet sistemidir. Sabah kendi polikliniğinde sorunsuz e-reçete yazan hekim, akşam acil servise indiğinde başka bir bilgisayara e-imzasını taktığında sistem çalışmayabilir.

Bu durum genellikle bilgisayarlar arası işletim sistemi farklılıklarından (32-bit / 64-bit Java uyuşmazlığı) veya farklı e-imza firmalarının birbirini ezen sürücülerinden kaynaklanır. **Tavsiyemiz:** Sürekli nöbet tuttuğunuz bilgisayarlara bir kez kalıcı "e-imza kütüphanesi" tanımı yaptırmanızdır.

![Medula e-İmza Java Hatası Çözümü](/images/blog/medula-java-e-imza-hata.webp)

## Erzurum'daki Hekimlerimize "Öncelikli" Yerinde Destek

Poliklinikte hasta varken bilgisayar başında çağrı merkeziyle saatlerce sorun çözmeye çalışmak bir hekimin yaşayacağı en kötü deneyimdir.

Biz **E İmza Erzurum** olarak, doktorlarımızın ve sağlık çalışanlarımızın zamanının ne kadar kıymetli olduğunun farkındayız. 
* Yeni e-imza taleplerinizi **muayenehanenize veya hastanenize kadar gelerek** yerinde teslim ediyor,
* Medula, e-Nabız ve AHBS e-reçete kurulumlarınızı bizzat bilgisayarınızda test ediyoruz.
* Mevcut e-imzanız (farklı bir firmadan alınmış olsa bile) kilitlendiğinde veya okumadığında teknik destek sağlıyoruz.

> **Hekimlerimize Özel Kesintisiz Destek:**
> E-reçete sisteminiz e-imzanızı görmüyorsa veya e-imzanızın süresi dolduysa vakit kaybetmeyin. **0442 606 08 86** numaralı telefonumuzdan bize ulaşın veya WhatsApp hattımızdan yazın. Yakutiye Buhara Ofis Plaza'dan yola çıkıp sorununuzu en hızlı şekilde çözelim.
