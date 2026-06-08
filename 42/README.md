# 42 School — C Çalışmaları

42 School metodolojisine göre yapılan C dili alıştırmaları. Klasör; yoğun başlangıç eğitimi olan **Piscine (Havuz)** ve ana eğitimdeki **libft** kütüphane çalışmasını içerir.

## Yapı

```
42/
├── AnaEgitim/
│   └── libft/          # Standart C fonksiyonlarının yeniden yazımı (ft_isalpha, ft_isdigit ...)
└── Havuz/
    ├── C00 – C08/      # Günlük C modülleri (her modülde ex00, ex01 ... alıştırmaları)
    ├── rush00/         # Hafta sonu grup projesi
    └── Shell00/        # Kabuk (shell) alıştırmaları
```

## Modüller

- **C00–C07:** Karakter/sayı yazdırma, döngüler, string işlemleri, pointer'lar, özyineleme (recursion), `argc/argv` ve bellek yönetimi.
- **C08:** Header dosyaları, `typedef`, struct ve fonksiyon pointer'ları.
- **Shell00:** Temel kabuk komutları ve git alıştırmaları.
- **libft:** `<ctype.h>` ve `<string.h>` gibi standart fonksiyonların `ft_` ön ekli kendi implementasyonları.

## Derleme

Her alıştırma tek başına derlenebilir:

```bash
cc -Wall -Wextra -Werror dosya.c -o program
./program
```

## Kurallar (Norm)

Kod 42'nin **Norm** standardına göre yazılmıştır: yasak fonksiyonlar yok, fonksiyonlar kısa ve tek sorumluluklu, global değişken kullanımı sınırlı.
