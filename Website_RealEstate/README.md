# Website RealEstate — New City Land

Emlak / gayrimenkul firması için hazırlanmış statik tanıtım web sitesi. Saf HTML, CSS ve JavaScript ile geliştirilmiş, responsive (mobil uyumlu) tek sayfa tasarımdır.

## Yapı

```
Website_RealEstate/
├── index.html          # Ana sayfa
├── favicon.svg
├── style-guide.md      # Renk, tipografi ve tasarım rehberi
└── assets/
    ├── css/style.css   # Stiller
    ├── js/script.js    # Etkileşim (menü, slider vb.)
    └── images/         # Görseller (logo, hero, mülk fotoğrafları, avatarlar)
```

## Özellikler

- Responsive (mobil/masaüstü uyumlu) tasarım
- Mülk (property) tanıtım kartları
- Müşteri yorumları / hikâye bölümleri
- Hero görseli ve marka logosu (New City Land)
- Saf front-end — herhangi bir build adımı veya bağımlılık gerektirmez

## Çalıştırma

Hiçbir kurulum gerekmez; `index.html` dosyasını tarayıcıda açmanız yeterlidir:

```bash
# Doğrudan açma
start index.html        # Windows

# veya yerel sunucu ile
python -m http.server 8000
# tarayıcıda http://localhost:8000 adresini açın
```

> Not: `assets/_/` klasörü sitenin daha eski bir yedek/kopyasını içerir.
