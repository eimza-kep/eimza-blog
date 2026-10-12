---
title: "macOS Sequoia (15.x) ve Apple Silicon (M1-M4) Üzerinde E-İmza & Mali Mühür Kurulumu"
description: "Apple Silicon mimarili Mac bilgisayarlarda macOS 15 Sequoia sürümünde AKİS, TÜBİTAK Kamu SM ve UYAP e-imza kurulumlarının eksiksiz adım adım rehberi."
category: "E-İmza & Donanım"
pubDate: "2026-10-12"
author: "Antigravity Sistem Mühendisliği"
---

Apple'ın **Apple Silicon** işlemcileri (M1, M2, M3, M4) ve yeni nesil **macOS Sequoia (15.x)** işletim sistemi, yüksek güvenlik standartları nedeniyle akıllı kart (USB Token) sürücülerinde bazı yeni yapılandırmalar gerektirmektedir.

Bu teknik kılavuzda, macOS Sequoia altında E-İmza ve Mali Mühür cihazlarının sorunsuz çalışması için izlenmesi gereken adımları paylaşıyoruz.

---

## 1. Mimari Gereksinimler: Rosetta 2 ve Yerel ARM64 Kütüphaneleri

TÜBİTAK BİLGEM AKİS ve özel ESHS sürücülerinin bir kısmı yerel Apple Silicon (ARM64) dylib kütüphaneleri sağlarken, eski UYAP ve Java imzalama applet'ları Rosetta 2 emülasyonuna ihtiyaç duyabilir.

Terminal üzerinden Rosetta 2 durumunu kontrol edin veya kurun:

```bash
/usr/sbin/softwareupdate --install-rosetta --agree-to-license
```

---

## 2. Akıllı Kart Servisinin (PCSC-Lite) Doğrulanması

macOS Sequoia'da `com.apple.ifdreader` ve yerleşik SmartCard servisleri arka planda çalışır. USB Token'ınızın macOS tarafından algılanıp algılanmadığını doğrulamak için Terminal'de şu komutu çalıştırın:

```bash
pcsctool
# Veya sistem bilgi dökümü:
system_profiler SPUSBDataType | grep -A 5 -i "SmartCard"
```

Eğer USB kart okuyucu listeleniyor ancak kart durumu görünmüyorsa:
1. USB-C çevirici adaptörünüzün veri aktarımını desteklediğinden emin olun.
2. Mac Sistem Ayarları > Gizlilik ve Güvenlik > Aksesuarların Bağlanmasına İzin Ver seçeneğini "Her Zaman" veya "Yeni Aksesuarlar İçin Sor" olarak ayarlayın.

---

## 3. AKİS ve PKCS#11 Kütüphane Yolları

macOS Sequoia altında UYAP Doküman Editörü, Chrome veya Mozilla Firefox'un akıllı kartı görebilmesi için PKCS#11 kütüphane yolunun doğru belirtilmesi gerekir.

Standart yerleşim yolları:
* **AKİS 64-bit ARM:** `/Library/OpenSC/lib/opensc-pkcs11.dylib` veya `/usr/local/lib/libakisp11.dylib`
* **Kamu SM Kart Sürücüsü:** `/Applications/AKIS/libakisp11.dylib`
* **SafeNet / Gemalto:** `/Library/Frameworks/eToken.framework/Versions/A/libeToken.dylib`

Firefox kullanıcıları:
1. Ayarlar > Gizlilik ve Güvenlik > Güvenlik Cihazları (Security Devices) menüsüne gidin.
2. **Yükle (Load)** butonuna tıklayın.
3. Modül Adı: `AKIS PKCS#11`
4. Modül Dosyası Yolu: `/usr/local/lib/libakisp11.dylib`

---

## 4. Java 21 LTS ve UYAP Editör Bellek Optimizasyonu

macOS Sequoia ile tam uyumlu çalışmak için Azul Zulu JDK veya Eclipse Temurin OpenJDK 21 LTS sürümü önerilir.

Terminal üzerinden UYAP editörünü yüksek bellek ve doğru PKCS#11 yapılandırmasıyla başlatmak için:

```bash
java -Xms512m -Xmx2048m -Dsun.security.smartcardio.library=/System/Library/Frameworks/PCSC.framework/PCSC -jar /Applications/UYAPEditor/uyap.jar
```

---

## 5. Özet ve Kontrol Listesi

- [x] macOS Sequoia güncellemesi sonrası Sistem İzinlerinde USB erişimi onaylandı mı?
- [x] AKİS Kart İzleme Aracı açıldığında kartın ATR kodu ve sertifika sahibi okunabiliyor mu?
- [x] Java çalışma zamanında PCSC Framework kütüphanesi aktif mi?
- [x] E-İmza sertifikasının geçerlilik süresi dolmamış mı?

Bu adımlarla, macOS Sequoia üzerinde hem e-Devlet, hem UYAP, hem de kurumsal GİB e-Belge portal işlemlerinizi sıfır hatayla gerçekleştirebilirsiniz.
