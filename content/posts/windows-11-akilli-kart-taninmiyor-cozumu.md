---
title: "Windows 11'de 'Akıllı Kart Tanınmıyor' (Smart Card) Hatası ve e-İmza Sürücü Çözümleri"
description: "Yeni alınan veya güncellenen Windows 11 bilgisayarlarda e-imza USB'sinin okunmaması, 'Akıllı kart takın' hatası ve AKİS/ArkSigner sürücü güncellemeleri."
pubDate: "2026-09-17"
category: "Teknik Destek"
author: "E İmza Erzurum"
---

Teknoloji hızla gelişiyor ve şirketlerimiz, mali müşavir ofislerimiz, hekimlerimiz bilgisayarlarını yeni nesil sistemlere geçiriyor. Özellikle yeni alınan veya işletim sistemi güncellenen **Windows 11** bilgisayarlarda, daha dün başka cihazda sorunsuz çalışan e-imza veya mali mühür aniden okunamamaya başlar.

E-imza USB token'ınızı taktığınızda bilgisayardan "uyarı" sesi gelir ancak GİB, MERSİS veya UYAP ekranlarında "Akıllı Kart Bulunamadı", "Lütfen Akıllı Kartınızı Takın" veya "Smart Card Tanınmıyor" gibi hatalar alıyorsanız, sorun cihazınızın bozulması değil, işletim sisteminin kart okuyucu sürücülerini tanımamasıdır.

![Windows 11 Akıllı Kart Hatası](/images/blog/windows-11-akilli-kart-taninmiyor.webp)

## Windows 11 Neden E-İmza'yı Görmez?

Windows 11, güvenlik ve donanım mimarisinde Windows 10'a göre ciddi değişiklikler barındırır. Sorunun temelinde yatan üç ana neden vardır:

1. **Eksik veya Eski Sürücü (Driver):** E-imza çipini (SIM kartı) okuyan USB aygıtının (Örn: ACS, Aladdin, Gemalto) sürücüsü Windows 11 ile uyumlu değildir.
2. **AKİS/Ara Yazılım Uyumsuzluğu:** TÜBİTAK Kamu SM tarafından üretilen çiplerin bilgisayarla konuşmasını sağlayan AKİS (Akıllı Kart İşletim Sistemi) yazılımının eski bir 32-bit versiyonunun kurulu olmasıdır.
3. **Akıllı Kart Hizmetinin Durması:** Windows'un arka planında çalışan "Smart Card (Akıllı Kart)" servisinin işletim sistemi tarafından uykuya alınması veya durdurulmasıdır.

## Adım Adım Çözüm Rehberi

Bu sorunu çözmek için bilgisayarcı aramanıza gerek yok, aşağıdaki adımları sırasıyla uygulayarak sorunu çoğunlukla çözebilirsiniz.

### 1. Windows Akıllı Kart Hizmetini Kontrol Edin
Bilgisayarınız e-imzayı fiziksel olarak görse bile Windows servisi kapalıysa yazılımlar imzanızı bulamaz.
* Klavyeden `Windows + R` tuşlarına aynı anda basın.
* Çalıştır penceresine `services.msc` yazıp Enter'a basın.
* Açılan Hizmetler listesinde **"Akıllı Kart" (Smart Card)** hizmetini bulun.
* Üzerine sağ tıklayıp "Özellikler" deyin. "Başlangıç Türü" kısmını **Otomatik** yapın ve hizmet duruyorsa **"Başlat"** butonuna tıklayın.

### 2. Eski Sürücüleri Tamamen Kaldırın
Çakışmaları önlemek için eski sürücü kalıntılarını temizlemek şarttır.
* "Denetim Masası > Program Ekle/Kaldır"a gidin.
* Sisteminizde yüklü olan "AKİS Yönetici", "ArkSigner", "Java" ve kart okuyucu sürücülerini (ACS, Gemalto vb.) bularak kaldırın.
* Bilgisayarınızı yeniden başlatın.

### 3. Windows 11 Uyumlu Yeni Sürücüleri Yükleyin
* E-imzanızın markasına veya Kamu SM altyapısına uygun olan **güncel (64-bit)** AKİS veya ilgili ara yazılımı resmi sitelerinden indirin.
* Kart okuyucunuzun modeline (USB token üzerindeki marka, genelde ACS CCID'dir) uygun Windows 11 sürücüsünü kurun.
* Yeni nesil 64-bit Java (JRE) sürümünü kurun.

| Donanım / Yazılım | İndirilmesi Gereken (Önerilen) |
| :--- | :--- |
| **Java Sürümü** | Java 8 Update 300 ve üzeri (Tercihen 64-bit) |
| **AKİS Kart İzleme Aracı** | Windows 64-Bit uyumlu son sürüm (Kamu SM'den) |
| **USB Okuyucu Sürücüsü** | ACS (Advanced Card Systems) PC/SC Driver |

![Windows Hizmetler Akıllı Kart Servisi](/images/blog/windows-smart-card-hizmeti.webp)

### 4. AKİS Kart İzleme Aracı İle Test Edin
Tüm kurulumları yaptıktan sonra USB cihazınızı takın. Bilgisayarınızın arama çubuğuna `Akis Kart İzleme Aracı` yazıp açın. Eğer program açıldığında adınızı, soyadınızı ve sertifikanızı görüyorsanız, Windows 11 sorununuz çözülmüş demektir. Artık GİB veya UYAP sistemlerinde imza atabilirsiniz.

## Teknik Detaylarla Uğraşmak İstemiyor Musunuz?

Yeni aldığınız bilgisayarda işlerinizin durması can sıkıcıdır. Yukarıdaki adımlar karmaşık geldiyse veya uygulamanıza rağmen "Akıllı Kart Tanınmıyor" hatası devam ediyorsa, riske girmeyin.

> **Erzurum'da Hızlı Teknik Destek:**
> **E İmza Erzurum** olarak, Windows 11 uyumluluk sorunlarınızı uzak masaüstü bağlantısıyla dakikalar içinde veya Erzurum'daki ofisinize gelerek bizzat çözüyoruz. E-imzanızın düzgün çalışmasını garanti altına almak için **0442 606 08 86** numarasından hemen bize ulaşın.
