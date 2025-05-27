yas = int(input("Lutfen yasinizi girin: "))
sinav_notu = float(input("Lutfen sinav notunuzu girin: "))
odeme = float(input("Lutfen odeyeceginiz tutari girin (TL): "))

if yas < 18:
    print("Kayit reddedildi: Yasiniz 18'den kucuk, ehliyet kursuna kayit olamazsiniz.")
else:
    if sinav_notu >= 70 and odeme >= 15000:
        print("Kayit basarili! Ehliyet kursuna kayit oldunuz.")
    else:
        print("Kayit reddedildi: Sinav notunuz 70'ten dusuk veya odemeniz 15000 TL'den az.")