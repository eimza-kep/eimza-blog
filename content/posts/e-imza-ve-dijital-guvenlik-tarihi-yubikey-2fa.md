---
title: "Dijital Kimliğin Evrimi: Kil Tabletlerden E-İmza ve YubiKey'lere İmzalamanın Tarihi"
description: "İnsanlığın imza tarihçesi, asimetrik şifrelemenin doğuşu, 5070 sayılı E-İmza Kanunu, 2FA teknolojileri ve YubiKey gibi donanımsal güvenlik anahtarlarının detaylı evrimi."
pubDate: "2026-09-17"
category: "Tarihçe & Teknoloji"
author: "E İmza Erzurum"
---

İnsanoğlunun "Bu benim sözümdür, bu belgeyi ben onaylıyorum" deme ihtiyacı, yazının icadından bile eskiye dayanır. Sümerlerde kil tabletlere basılan silindir mühürlerden, Orta Çağ Avrupası'nda kralların fermanlara damlattığı erimiş mum ve yüzük mühürlerine kadar uzanan bu onaylama süreci, temel bir güven ihtiyacının sonucudur. Yüzyıllar boyunca kağıt ve mürekkep ile atılan ıslak imza, kimlik doğrulamanın ve yasal bağlayıcılığın (inkar edilemezlik) yegane aracı oldu.

Ancak 20. yüzyılın sonlarında bilgisayarların, ardından internetin hayatımıza girmesiyle devasa bir sorun ortaya çıktı: **Fiziksel olarak yan yana olmadığımız, birbirimizi görmediğimiz dijital bir ağda, bir belgenin "gerçekten" bize ait olduğunu nasıl kanıtlayabilirdik?** Dijital veriler sonsuz kere, kopyalanabildiği ve üzerinde hiçbir iz bırakmadan değiştirilebildiği için, ıslak imzanın taranıp PDF'e yapıştırılması hukuki bir anlam ifade etmiyordu. İşte elektronik imza (e-imza) ve günümüzün modern 2FA (İki Faktörlü Kimlik Doğrulama) donanımları olan YubiKey'lerin hikayesi bu temel sorunun çözümüyle başladı.

![E-İmza, YubiKey ve Dijital Güvenlik Tarihi](/images/blog/e-imza-dijital-guvenlik-tarihi.webp)

## 1. Dijital Kimliğin Doğuşu: Kriptografi Devrimi (1970'ler)

E-imzanın ve modern siber güvenliğin temeli 1970'lerde atıldı. O döneme kadar şifreleme (kriptografi), göndericinin ve alıcının aynı "gizli anahtarı" bildiği simetrik bir yapıdaydı. Bu, İkinci Dünya Savaşı'ndaki Enigma makinesi mantığıydı. Ancak internet gibi açık bir ağda, gizli anahtarı karşı tarafa güvenli bir şekilde nasıl iletecektiniz? 

1976 yılında Whitfield Diffie ve Martin Hellman adında iki vizyoner araştırmacı, dünyayı değiştiren bir makale yayınladı: **"New Directions in Cryptography" (Kriptografide Yeni Yönelimler)**. Bu makale, **"Asimetrik Şifreleme" (Açık Anahtar Altyapısı - PKI)** kavramını ilk kez dünyaya duyurdu. 
Sistem devrim niteliğindeydi: Herkesin matematiken birbirine bağlı ancak birbirinden tersine mühendislikle türetilemeyen iki anahtarı olacaktı:
1. **Açık Anahtar (Public Key):** Herkese dağıtılabilen asma kilit.
2. **Özel Anahtar (Private Key):** Sadece sahibinde bulunan, bu asma kilidi açabilen tek anahtar.

Sadece bir yıl sonra, 1977'de MIT (Massachusetts Teknoloji Enstitüsü) araştırmacıları Ron Rivest, Adi Shamir ve Leonard Adleman bu teoriyi pratik bir algoritmaya dönüştürdü ve soyisimlerinin baş harflerinden oluşan meşhur **RSA Algoritmasını** icat etti. Bugün bilgisayarımıza taktığımız tüm e-imza cihazlarının, girdiğimiz bankacılık sitelerinin (HTTPS) temelinde bu üç adamın 1977'de bulduğu algoritma yatmaktadır. Eğer bir belge Özel Anahtar ile şifrelenirse, herkes Açık Anahtar ile o belgenin sadece ve sadece o Özel Anahtar sahibi tarafından şifrelendiğini doğrulayabilirdi. İşte dijital imzanın (digital signature) matematiksel doğuşu buydu.

## 2. Hukuki Zemin: Dünyada ve Türkiye'de E-İmza Kanunları

Matematiksel olarak dijital imzanın güvenilirliği kanıtlansa da, hukuk sisteminin bu soyut matematiği kabul etmesi yıllar aldı. Dünyada dijital imzayı ıslak imza ile eşdeğer tutan **ilk yasa 1995 yılında ABD'nin Utah eyaletinde (Utah Digital Signature Act)** kabul edildi. Bunu 1999 yılında Avrupa Birliği'nin E-İmza Direktifi (EU Directive 1999/93/EC) ve 2000 yılında dönemin ABD Başkanı Bill Clinton'ın dijital olarak imzalayarak yürürlüğe soktuğu ESIGN yasası izledi.

**Türkiye'nin E-İmza Serüveni (2004):**
Türkiye, dijital dönüşümde oldukça erken reaksiyon gösteren ülkelerden biri oldu. 23 Temmuz 2004 tarihinde yürürlüğe giren **5070 Sayılı Elektronik İmza Kanunu**, Türkiye'de e-imzanın ıslak imzaya eşdeğer hukuki sonuçlar doğuracağını resmileştirdi.
Bu yasa ile "Nitelikli Elektronik Sertifika" (NES) kavramı hayatımıza girdi. Türkiye'de e-imza altyapısının kurulmasında TÜBİTAK Kamu SM (Kamu Sertifikasyon Merkezi) öncü bir rol üstlendi. Başlangıçta devasa kart okuyucular ve büyük akıllı kartlarla başlayan serüven, zamanla USB bellek boyutundaki (Token) donanımlara küçüldü. Özellikle UYAP (Ulusal Yargı Ağı Bilişim Sistemi) projesiyle avukatlar ve hakimler; MERSİS ve e-Fatura gibi Gelir İdaresi projeleriyle de şirketler e-imza ile tanıştı. Bugün Türkiye'de milyonlarca aktif e-imza kullanıcısı bulunmaktadır.

## 3. Parolaların Çöküşü ve 2FA (İki Faktörlü Kimlik Doğrulama)

E-imza belgeleri yasal olarak imzalamak için kusursuz bir çözüm sunarken, internetin günlük kullanımında (epostalara girerken, sosyal medya hesaplarını yönetirken) e-imza takıp şifre girmek pratik değildi. İnsanlar bunun yerine sadece "Kullanıcı Adı ve Parola" kullanmaya devam etti. Ancak 2000'li yılların ortalarından itibaren veri ihlalleri, "Oltalama" (Phishing) saldırıları ve sızdırılan milyarlarca parola, tek faktörlü güvenliğin tamamen çöktüğünü gösterdi.

Bir sisteme güvenli giriş yapabilmek için siber güvenlikte 3 temel faktör vardır:
1. **Bildiğiniz bir şey:** Parolanız veya PIN kodunuz.
2. **Sahip olduğunuz bir şey:** Cep telefonunuz, akıllı kartınız veya güvenlik anahtarınız.
3. **Olduğunuz bir şey:** Parmak iziniz, retina veya yüz taramanız (Biyometri).

Sadece parola ("bildiğiniz bir şey") çalındığında sistem çöktüğü için, teknoloji devleri **İki Faktörlü Kimlik Doğrulamayı (2FA - Two Factor Authentication)** zorunlu kılmaya başladı. İlk başlarda bankaların gönderdiği SMS kodları (OTP) hayatımıza girdi. Ancak SMS, SIM kopyalama (SIM Swapping) saldırılarına karşı zayıftı. Daha sonra Google Authenticator, Microsoft Authenticator gibi zamana duyarlı şifre üreten (TOTP) mobil uygulamalar yaygınlaştı. Fakat hackerlar, sahte giriş ekranlarıyla kullanıcıları kandırarak bu mobil kodları da çalmayı (MFA Fatigue / Phishing) başardı. Gerçekten "kırılamaz" bir donanıma ihtiyaç vardı.

## 4. Donanımsal Güvenlik Anahtarları ve YubiKey Devrimi

İşte tam bu noktada oltalama (phishing) saldırılarını sıfıra indiren donanımsal güvenlik anahtarları (Security Keys) sahneye çıktı. 2007 yılında Stina Ehrensvärd ve Jakob Ehrensvärd tarafından İsveç'te kurulan **Yubico** şirketi, bugün dünyanın en çok bilinen donanımsal güvenlik anahtarı olan **YubiKey**'i icat etti.

YubiKey, görünüş olarak tıpkı e-imza USB tokenlarına benzer. Ancak amacı yasal belge imzalamak değil, hesaplara erişim sırasında "Sahip olunan şey" faktörünü fiziksel ve kriptografik bir zırha büründürmektir. 

**YubiKey Nasıl Çalışır ve FIDO Nedir?**
Yubico ve Google'ın öncülüğünde kurulan FIDO (Fast IDentity Online) Alliance birliği, şifresiz (passwordless) ve kırılamaz bir internet standardı olan WebAuthn/FIDO2'yi geliştirdi. 
Bir Gmail veya Binance hesabınıza YubiKey'inizi tanımladığınızda süreç şöyle işler:
* Giriş yaparken sistem sizden cihazınızı takıp üzerindeki dokunmatik sensöre parmağınızla dokunmanızı ister.
* Dokunduğunuz an cihaz, YubiKey'in içindeki özel anahtarı kullanarak o anki oturum isteğini kriptografik olarak imzalar.
* **Oltalama Koruması:** YubiKey, girmeye çalıştığınız sitenin gerçek URL'sini (örneğin gerçek `google.com` mu yoksa sahte `g00gle.com` mu) bilgisayarın tarayıcısından (Chrome, Safari) kriptografik olarak kontrol eder. Eğer sizi sahte bir siteye yönlendirdilerse, YubiKey o siteye yanıt vermeyi reddeder. Bu özellik, YubiKey'i oltalama saldırılarına karşı %100 korumalı hale getiren ana devrimdir.

| Özellik | Standart E-İmza (NES USB Token) | YubiKey (FIDO2 Güvenlik Anahtarı) |
| :--- | :--- | :--- |
| **Temel Amacı** | Belge, Fatura ve Beyannamelere yasal, ıslak imza eşdeğeri mühür vurmak. (Non-repudiation) | Dijital hesaplara (Mail, Banka, Sunucu) yetkisiz erişimi engellemek, güvenli giriş yapmak. (Authentication) |
| **Hukuki Statü** | 5070 Sayılı Kanun'a göre resmi geçerliliği vardır. T.C. Kimlik doğruludur. | Yasal bir belge onaylayıcısı değildir, hesap erişim güvenlik kalkanıdır. |
| **Pin / Dokunma** | İmza atmak için mutlaka PIN (şifre) girilmesi gerekir. | Çoğunlukla sadece cihaz üzerindeki altın renkli alana parmakla dokunmak yeterlidir. |
| **Yazılım Gereksinimi** | AKİS, ArkSigner gibi bilgisayara kurulan özel sürücüler (Middleware) ve Java gerektirir. | Sürücü gerektirmez (Plug-and-play). Modern tüm tarayıcılar FIDO standardını doğrudan tanır. |

## 5. İki Teknolojinin Kesişimi: PIV ve Akıllı Kartlar

Modern dijital güvenlikte e-imza (akıllı kartlar) ve YubiKey (FIDO2) aslında birbiriyle rekabet eden değil, birbirini tamamlayan, aynı kökenden (Asimetrik Şifreleme) beslenen iki kuzen gibidir. Hatta günümüzde üst düzey YubiKey serileri (YubiKey 5 Series), FIDO özelliklerinin yanı sıra içinde PIV (Personal Identity Verification - Kişisel Kimlik Doğrulama) adı verilen bir akıllı kart uygulaması barındırır. Bu sayede yazılımcılar, YubiKey'in içine PGP (Pretty Good Privacy) veya yazılım kod imzalama (Code Signing) sertifikalarını gömerek onu bir nevi kurumsal e-imza gibi de kullanabilmektedir. Ancak Türkiye'deki mali (e-Fatura vb.) ve yasal (UYAP) süreçler için sadece BTK ve Kamu SM onaylı, ulusal NES sertifikaları barındıran yerel e-imza tokenları geçerlidir.

## 6. Gelecek Nereye Gidiyor? Passkey ve Kuantum Tehdidi

Donanımsal güvenlik anahtarlarının başarısı, günümüzde "Passkey" (Geçiş Anahtarı) teknolojisini doğurdu. Apple (FaceID, TouchID), Google ve Microsoft, FIDO standartlarını artık donanımsal bir USB yerine doğrudan akıllı telefonlarımızın içindeki güvenli çiplere (Secure Enclave) entegre ediyor. Cihazımız hem "Sahip olduğumuz", biyometrimiz ise "Olduğumuz" şeyi doğrulayarak parolaları tamamen hayatımızdan çıkarmaya hazırlanıyor. 

Diğer yandan, 1970'lerde icat edilen RSA ve Asimetrik Şifrelemenin önünde devasa bir ufuk çizgisi var: **Kuantum Bilgisayarlar.** Kuantum bilgisayarlar yeterli işlem gücüne ulaştığında, günümüzdeki e-imzaların ve YubiKey'lerin kullandığı şifreleme algoritmalarını saniyeler içinde kırabilme potansiyeli taşıyor. Bu yüzden bugün, kriptografi dünyası kuantum-dirençli algoritmalar (Post-Quantum Cryptography) geliştirmek ve tüm bu e-imza altyapılarını yeni çağa güncellemek için var gücüyle çalışıyor.

## Sonuç: Erzurum'dan Dünyaya Dijital Güvenlik

Sümerlerin kil tabletlerine bastığı mühürlerden, Whitfield Diffie'nin asimetrik şifrelemesine ve Yubico'nun kırılmaz donanımlarına uzanan bu devasa tarih; aslında bilginin ve ticaretin güvenliğini sağlama arayışımızın bir özetidir.

Dünyadaki bu devasa teknolojik evrimin meyvesi olan, askeri standartlardaki kriptografik e-imza donanımları bugün günlük hayatımızın ayrılmaz bir parçası. **E İmza Erzurum** olarak, dünyanın en gelişmiş şifreleme teknolojilerine dayanan bu yasal donanımları, Erzurum Yakutiye'de Buhara Ofis Plaza'da, şehrimizin esnafı, tüccarı ve şirketleri için **sadece 15 dakikada** hazırlayıp teslim ediyoruz. Ticaretinizin ve verilerinizin dijital çağda güvende kalması, yüzyılların birikimi olan bu eşsiz teknoloji sayesinde artık parmaklarınızın ucunda.
