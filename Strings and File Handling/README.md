# Strings and File Handling — Log İşleyici

Bir sunucu log dosyasını okuyup içindeki satırları seviyelerine göre ayrı dosyalara ayıran Python ödevi. Dosya işleme (file handling) ve string arama konularını kapsar.

## Yapı

```
Strings and File Handling/
├── 230408032_Assignment1.py   # Ana program
├── server_logs.txt            # Girdi: işlenecek log dosyası
├── error_logs.txt             # Çıktı: ERROR satırları
├── info_logs.txt              # Çıktı: INFO satırları
└── warning_logs.txt           # Çıktı: WARNING satırları
```

## Ne Yapar?

`server_logs.txt` dosyasını satır satır okur ve:

- `ERROR` içeren satırları → `error_logs.txt`
- `INFO` içeren satırları → `info_logs.txt`
- `WARNING` içeren satırları → `warning_logs.txt`

dosyalarına yazar. Ayrıca toplam **ERROR** sayısını ekrana yazdırır. Boş satırlar atlanır.

## Çalıştırma

```bash
python 230408032_Assignment1.py
```

> Program çalışma dizinindeki `server_logs.txt` dosyasını girdi olarak kullanır ve çıktı dosyalarını aynı dizine yazar.
