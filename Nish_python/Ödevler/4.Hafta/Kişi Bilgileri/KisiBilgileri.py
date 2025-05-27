from datetime import datetime

# Kişi bilgilerini içeren sözlük
kisi = {
    "ad": input("Ad: "),
    "yas": int(input("Yaş: ")),
    "meslek": input("Meslek: "),
    "dogum_yili": None
}

# Güncel yılı al
su_an = datetime.now()
yil = su_an.year

# Doğum yılını hesapla
kisi["dogum_yili"] = yil - kisi["yas"]

# Sonuçları yazdır
print("\nKişi Bilgileri:")
print(f"Ad: {kisi['ad']}")
print(f"Meslek: {kisi['meslek']}")
print(f"Yaş: {kisi['yas']}")
print(f"Doğum Yili: {kisi['dogum_yili']}")
