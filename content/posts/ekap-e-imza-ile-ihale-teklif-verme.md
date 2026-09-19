---
title: "EKAP İhalesine e-İmza ile Teklif Nasıl Verilir? e-Teklif İmzalama Hataları ve Çözümleri"
description: "Kamu İhale Kurumu (EKAP) üzerinden e-imza ile e-teklif hazırlama adımları, Java hatalarının çözümü ve ihaleye saatler kala yaşanabilecek krizlerin önlenmesi."
pubDate: "2026-09-17"
category: "E-İmza"
author: "E İmza Erzurum"
---

Günümüzde kamu kurumlarının, belediyelerin, üniversitelerin ve devlet hastanelerinin açtığı ihalelerin büyük çoğunluğu Kamu İhale Kurumu'nun Elektronik Kamu Alımları Platformu (EKAP) üzerinden **e-İhale (elektronik ihale)** usulüyle yapılmaktadır. Fiziki zarfların, kargo gecikmelerinin ve evrak kalabalığının yerini alan bu sistemin kalbinde ise **e-İmza** yer alır.

Erzurum'daki müteahhitlerimiz, medikal firmalarımız ve kamuya ürün/hizmet sağlayan tedarikçilerimiz için ihaleye saniyeler kala teklif zarfını imzalayamamak en büyük kabustur. Bu rehberde, EKAP üzerinden e-teklif hazırlamanın teknik aşamalarını ve en sık karşılaşılan imzalama hatalarının kesin çözümlerini ele alıyoruz.

![EKAP e-İmza Teklif İmzalama Ekranı](/images/blog/ekap-e-imza-teklif-verme.webp)

## EKAP e-Teklif Sürecinde E-İmzanın Rolü

EKAP sistemine giriş yapmak için e-Devlet kapısı kullanılabilse de, hazırladığınız ihalenin idari şartnamesi, birim fiyat teklif mektubu ve geçici teminat mektubu beyanlarından oluşan **e-Teklif paketinin şifrelenmesi ve imzalanması yasal olarak sadece e-İmza ile mümkündür.**

İhaleye yetkili olarak teklif sunacak şirket müdürü veya vekilin, kendi T.C. kimlik numarasına tanımlı Nitelikli Elektronik Sertifika (NES) barındıran geçerli bir e-imzası bulunmalıdır. (Şirketin mali mührü bu işlem için kullanılamaz).

### Teklif Göndermeden Önce Hazırlık Adımları

İhale saatine 15 dakika kala e-imzayı bilgisayara takmak, telafisi olmayan bir hatadır. Sistem ön hazırlık gerektirir:
1. **EKAP e-İmza Uygulamasını İndirin:** EKAP web tabanlı çalışsa da belgeleri şifrelemek için bilgisayarınıza özel bir istemci (e-imza uygulaması) indirmeniz istenir.
2. **Java Kontrolü:** Bilgisayarınızda güncel bir Java (JRE) sürümünün yüklü olduğundan emin olun.
3. **Sürücülerin Çalışması:** E-imzanızın (AKİS, ArkSigner vb.) sürücülerinin güncel ve okuyucunun aktif olduğunu mutlaka kontrol edin.

## Sık Karşılaşılan EKAP e-İmza Hataları ve Çözüm Yolları

EKAP sisteminde teklif zarfınızı oluşturup "İmzala ve Gönder" butonuna bastığınızda bazen sistem uyarı verebilir. İşte sahadaki tecrübelerimize göre en sık yaşanan sorunlar:

| Karşılaşılan Hata / Sorun | Olası Neden | Kesin Çözüm Adımı |
| :--- | :--- | :--- |
| **"E-İmza Kütüphanesi Başlatılamadı"** | EKAP uygulamasının kart sürücüsünü bulamaması (32/64 bit uyumsuzluğu). | Doğru akisp11.dll dosyasının seçildiğinden veya kart donanım sürücüsünün eksiksiz kurulduğundan emin olun. |
| **Sertifika Listesi Boş Geliyor** | USB okunmuyor, PIN kilitli veya sertifika süresi bitmiş. | PIN uygulamasından (Örn: Arkİmza) kilit kontrolü yapın. USB portunu değiştirin. |
| **"Java Security Exception" Engeli** | İşletim sisteminizin veya Java'nın güvenlik ayarları uygulamanın çalışmasına izin vermiyordur. | Java Control Panel üzerinden `Security` sekmesine girip EKAP adresini `Exception Site List`'e (Güvenli Liste) ekleyin. |

![EKAP e-İmza Kütüphane Hatası Çözümü](/images/blog/ekap-e-imza-hata-cozumu.webp)

## İhale Öncesi Krizlere Erzurum'dan Acil Müdahale

İhale teklifinizin gönderim saati 14:00 ve saat 13:00'te e-imzanızın kilitlendiğini veya kaybolduğunu fark ettiniz. Kargo ile yeni bir imza sipariş etmek veya Ankara'daki çağrı merkezlerine bağlanıp saatlerce beklemek, milyonluk ihaleyi kaçırmanıza neden olabilir.

Böyle acil durumlarda **E İmza Erzurum** olarak yanınızdayız. Erzurum Yakutiye'deki ofisimize sadece kimliğinizle gelerek **15 dakika içinde yeni e-imzanızı teslim alabilir**, bilgisayarınızı getirirseniz EKAP kurulumlarınızı bizzat test edebiliriz. 

> **İhaleyi Şansa Bırakmayın:**
> EKAP ihalelerine girecekseniz ve e-imzanızın geçerlilik süresinden veya sistem kurulumundan şüphe ediyorsanız, bize **0442 606 08 86** numarasından hemen ulaşın. Teknik altyapınızı ihaleden günler önce güvenle hazırlayalım.
