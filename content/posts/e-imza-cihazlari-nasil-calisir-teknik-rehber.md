---
title: "E-İmza Cihazları (USB Token) Nasıl Çalışır? Çipin İçindeki Teknik Dünya"
description: "E-imza cihazlarının (USB Token) çalışma mantığı, asimetrik şifreleme (PKI), akıllı kart teknolojisi ve yazılım mimarisi hakkında detaylı teknik rehber."
pubDate: "2026-09-17"
category: "Teknik Rehber"
author: "E İmza Erzurum"
---

Günlük iş hayatımızda bilgisayarımıza taktığımız, şekil olarak sıradan bir flash belleği (USB) andıran e-imza cihazları, aslında içerisinde askeri düzeyde güvenlik barındıran minyatür birer bilgisayardır. 

Erzurum'daki ofisimize gelen birçok kullanıcımız, *"Bu ufacık cihaz nasıl oluyor da ıslak imzamın yerine geçiyor? Flash belleğe kopyalasam olmaz mı?"* diye haklı bir soru soruyor. Cevap net: **Hayır, kopyalayamazsınız.** Çünkü e-imza cihazları veriyi sadece depolayan değil, veriyi "şifreleyen" aktif donanımlardır. Gelin, bu cihazların arkasındaki büyüleyici teknolojiye ve çalışma mantığına teknik bir mercekle bakalım.

![E-İmza Cihazı USB Token İç Yapısı](/images/blog/e-imza-cihazi-usb-token-nasil-calisir.webp)

## 1. Cihazın Kalbi: Akıllı Kart (Smart Card) ve Kripto Çip

Bir e-imza cihazının dışındaki plastik veya metal kasa sadece bir USB okuyucudur (Card Reader - genellikle ACS, Gemalto veya Aladdin markadır). Asıl sihir, bu kasanın içine yerleştirilmiş olan, telefonlarımızdaki SIM karta benzeyen **Akıllı Kart (Smart Card)** çipindedir.

Bu çip sıradan bir hafıza çipi değildir; içerisinde kendi işlemcisi (CPU), RAM'i ve güvenli depolama alanı olan mikro bir **Kriptografik İşlemci'dir.** 
E-İmza üretim aşamasında (bizim 15 dakikada ofisimizde yaptığımız işlem), sizin T.C. kimlik bilgilerinizi taşıyan "Nitelikli Elektronik Sertifika" (NES) ve eşsiz bir "Özel Anahtar" (Private Key) bu çipin içine yazılır.

**En Kritik Güvenlik Kuralı:** Çipin donanımsal mimarisi gereği, içine yazılan "Özel Anahtar" hiçbir yazılım, virüs veya hacker tarafından **çipten dışarı çıkarılamaz (kopyalanamaz).** İmzalama işlemi bilgisayarınızın RAM'inde değil, fiziksel olarak doğrudan bu çipin içinde gerçekleşir.

## 2. Asimetrik Şifreleme (PKI - Public Key Infrastructure)

E-imzanın hukuki olarak "inkar edilemez" olmasını sağlayan teknoloji **Asimetrik Şifreleme** algoritmasıdır. Sistem iki anahtar ile çalışır:

* **Özel Anahtar (Private Key):** Sadece sizin e-imza çipinizin içinde hapis durumdadır. Dünyada sadece bir tanedir. Belgeyi şifrelemek (imzalamak) için kullanılır.
* **Açık Anahtar (Public Key):** Herkese açıktır, imzaladığınız belgenin içine gömülür. İmzanın size ait olup olmadığını doğrulamak (kilidi açmak) için kullanılır.

### Ekranda "İmzala" Butonuna Bastığınızda Arka Planda Ne Olur?
1. **Özet Çıkarma (Hashing):** İmzalayacağınız belgenin (örneğin bir PDF veya e-Fatura XML'i) SHA-256 gibi algoritmalarla dijital bir "özeti" (hash) çıkarılır. Belgedeki tek bir nokta değişse bile bu özet tamamen değişir.
2. **Çipe Gönderim:** Çıkarılan bu özet, USB bağlantısı üzerinden çipin içine gönderilir.
3. **Çip İçi Şifreleme:** Siz doğru **PIN kodunu** girdiğinizde, çip uyanır. Kendi içindeki Özel Anahtarı kullanarak bu belge özetini şifreler (kilitler).
4. **Mühürlü Belge:** Şifrelenmiş özet ve sizin Açık Anahtarınız belgeye iliştirilir. Artık belge e-imzalıdır! Karşı taraf belgeyi açtığında, açık anahtar gizli anahtarı doğrularsa imza geçerli sayılır.

## 3. Bilgisayar ile İletişim: Sürücüler (Middleware) ve Java

Çipin içindeki bu muazzam matematiğin GİB, UYAP veya MERSİS gibi web siteleriyle konuşabilmesi için bir tercümana ihtiyacı vardır.

* **Donanım Sürücüsü (CCID Driver):** USB portunun kart okuyucuya elektrik vermesini ve tanımasını sağlar.
* **Ara Yazılım (Middleware - AKİS / ArkSigner vb.):** TÜBİTAK Kamu SM veya e-imza firmaları tarafından sağlanan yazılımlardır. (Örn: `akisp11.dll`). Windows işletim sisteminin, akıllı kartın içindeki sertifikayı okuyabilmesini sağlayan köprüdür.
* **Java (JRE) / İstemci Yazılımı:** İnternet tarayıcınızın (Chrome, Edge), bilgisayarınızın donanımına (USB) doğrudan müdahale etmesi güvenlik gereği yasaktır. Java veya e-imza özel istemcileri, web sitesi ile sizin USB çipiniz arasında güvenli bir tünel açarak imzalama komutunu iletir. ("Java Security" hatalarının sebebi tam olarak bu köprünün güvenlik duvarına takılmasıdır).

| Bileşen | Görevi (Analoji) |
| :--- | :--- |
| **GİB / UYAP Sitesi** | Evrağı getiren kurye |
| **Java / İstemci** | Kuryeyi kapıda karşılayan güvenlik görevlisi |
| **AKİS (Ara Yazılım)** | Güvenlik görevlisinin konuştuğu ofis asistanı |
| **Çip (Smart Card)** | Mührü basan Şirket Patronu (Özel Anahtar) |

![E-İmza PKI Çalışma Mantığı](/images/blog/e-imza-pki-calisma-mantigi.webp)

## 4. Donanımsal Güvenlik (CC EAL4+ Standardı) ve PIN Blokesi

E-imza çiplerimiz, uluslararası donanım güvenliği standardı olan **Common Criteria EAL4+ (veya üzeri)** sertifikasına sahiptir. Bu, çipin fiziksel olarak parçalanıp elektron mikroskobu altında incelense dahi içindeki şifreyi vermeyeceği anlamına gelir.

Eğer e-imzanız çalınırsa, bulan kişi çipe erişmek için PIN kodunuzu tahmin etmek zorundadır. Ancak donanım, **peş peşe 3 kez yanlış PIN girildiğinde kendini "Fiziksel olarak" kilitler (bloke eder).** Bu kilit ancak e-imza sahibinin bildiği çok daha uzun bir **PUK kodu** ile açılabilir. PUK kodu da 3 kez yanlış girilirse, çip kendini kalıcı olarak imha eder (kullanılamaz hale gelir) ve verileriniz güvende kalır.

> **Yüksek Teknoloji, Erzurum'da Elinizin Altında**
> Bu kadar karmaşık ve yüksek güvenlikli kriptografik cihazları elde etmek için günlerce beklemenize gerek yok. **E İmza Erzurum** olarak, uluslararası güvenlik standartlarına (EAL4+) ve TÜBİTAK mevzuatına %100 uygun e-imza cihazlarınızı, Yakutiye Buhara Ofis Plaza'da, son teknoloji altyapımızla **sadece 15 dakika içinde** üreterek çipinizi aktif hale getiriyoruz. Teknik detaylara takılmadan güvenli imza atmak için bize **0442 606 08 86** numarasından ulaşabilirsiniz.
