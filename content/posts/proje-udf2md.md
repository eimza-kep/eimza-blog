---
title: "udf2md: UYAP UDF Dosyalarını Yapay Zekaya Hazır Markdown'a Dönüştürün"
date: "2026-09-22T01:07:00Z"
---

UYAP sisteminin ürettiği `.udf` dosya formatı ne ChatGPT, ne Gemini ne de Claude tarafından doğrudan okunabiliyor. Bu sorunu çözmek için **udf2md** adlı yeni bir açık kaynak araç geliştirdik!

## Ne Yapar?

`.udf` dosyanızı sürükleyip bırakıyorsunuz, araç tarayıcınızda (hiçbir sunucuya veri göndermeden) XML yapısını analiz ederek temiz bir Markdown belgesine dönüştürüyor. Paragraflar, kalın/italik formatlar, tablolar ve görseller korunuyor.

## Neden Markdown?

Markdown, tüm büyük LLM'lerin en iyi anladığı formattır. Yapılandırılmış, hafif ve evrensel uyumlu.

## %100 Gizlilik

Hukuki belgeler hassastır. Araç tamamen tarayıcı tabanlı (client-side) çalışır, internetsiz bile kullanılabilir.

👉 **GitHub:** [github.com/eimza-kep/udf2md](https://github.com/eimza-kep/udf2md)
