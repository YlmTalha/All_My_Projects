def metin_analizi(metin):
    kelimeler = metin.split()
    kelime_sayisi = len(kelimeler)
    
    harfler = []
    for karakter in metin:
        if karakter.isalpha():
            harfler.append(karakter)

    harf_sayisi = len(harfler)

    harf_adedi = {}
    for harf in harfler:
        if harf in harf_adedi:
            harf_adedi[harf] += 1
        else:
            harf_adedi[harf] = 1
    
    print(f"Toplam Kelime Sayisi: {kelime_sayisi}")
    print(f"Toplam Harf Sayisi: {harf_sayisi}")
    print("Harf Adedi:")
    for harf in sorted(harf_adedi.keys()):
        print(f"{harf}: {harf_adedi[harf]}")

metin = input("Bir metin giriniz: ")
metin_analizi(metin)
