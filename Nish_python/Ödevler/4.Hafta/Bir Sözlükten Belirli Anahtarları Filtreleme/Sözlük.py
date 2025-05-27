def filtrele(sozluk, anahtarlar):
    return {anahtar: sozluk[anahtar] for anahtar in anahtarlar if anahtar in sozluk}

ogrenci_bilgileri = {
    "isim": "Talha",
    "soyisim": "Yilmaz",
    "yas": 22,
    "tckn": "12345678901",
    "not_ortalamasi": 85.5
}

istenen_anahtarlar = ["isim", "tckn"]

yeni_sozluk = filtrele(ogrenci_bilgileri, istenen_anahtarlar)
print(yeni_sozluk)
