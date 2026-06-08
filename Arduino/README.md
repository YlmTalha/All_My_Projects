# Arduino — Potansiyometre ile Ses Kontrolü (SES)

Bir Arduino'ya bağlı potansiyometreyi çevirerek Windows bilgisayarın ana ses seviyesini (master volume) kontrol eden proje. Arduino, potansiyometrenin analog değerini (0–1023) seri port üzerinden bilgisayara gönderir; bilgisayardaki program bu değeri ses seviyesine çevirir.

## Yapı

```
Arduino/SES/
├── SES.PY     # Python sürümü — pycaw ile ses kontrolü (önerilen)
├── ses1.c     # C sürümü — Windows waveOut API ile ses kontrolü
└── .vscode/   # VS Code yapılandırması
```

## Çalışma Mantığı

1. Arduino, potansiyometre değerini `Serial.println()` ile gönderir (COM3 üzerinden, 9600 baud).
2. Bilgisayardaki program seri porttan değeri okur.
3. Değer `0.0 – 1.0` aralığına ölçeklenir ve sistem ses seviyesi ayarlanır.

## Gereksinimler

**Python sürümü (`SES.PY`):**
```bash
pip install pyserial pycaw comtypes
python SES.PY
```

**C sürümü (`ses1.c`):**
```bash
gcc ses1.c -o ses -lwinmm
./ses
```

> Not: `SERIAL_PORT` / `COM_PORT` değerini Aygıt Yöneticisi'nden Arduino'nun bağlı olduğu doğru COM portu ile güncelleyin.

## Donanım

- Arduino (Uno vb.)
- Potansiyometre (analog pine bağlı)
- USB kablo (seri haberleşme için)

> Bu proje yalnızca **Windows** üzerinde çalışır (pycaw / waveOut Windows API'leridir).
