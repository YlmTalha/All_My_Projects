fiyatlar = {
    1: 43.31,  # Dizel
    2: 43.02,  # Benzin
    3: 26.03   # LPG
}

print("Yakit türünü seçiniz:\n1 - Dizel\n2 - Benzin\n3 - LPG")
yakit_turu = int(input("Yakit türü (1, 2 veya 3): "))

if yakit_turu in fiyatlar:
    yakit_miktari = float(input("Almak istediğiniz yakit miktari (litre): "))
    bakiye = float(input("Bakiyenizi giriniz (TL): "))

    toplam_tutar = fiyatlar[yakit_turu] * yakit_miktari

    if bakiye >= toplam_tutar:
        kalan_bakiye = bakiye - toplam_tutar
        print(f"Yakit aliminiz başarili! Toplam tutar: {toplam_tutar:.2f} TL.")
        print(f"Kalan bakiyeniz: {kalan_bakiye:.2f} TL.")
    else:
        eksik_tutar = toplam_tutar - bakiye
        print(f"Bakiyeniz yetersiz! {eksik_tutar:.2f} TL eksik bakiyeniz var.")
else:
    print("Geçerli bir yakit türü seçmediniz. Lütfen 1, 2 veya 3'ü seçiniz.")
