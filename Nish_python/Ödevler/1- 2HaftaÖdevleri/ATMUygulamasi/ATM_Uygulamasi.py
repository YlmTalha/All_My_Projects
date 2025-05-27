print("\nHos geldiniz! Lutfen baslangic bakiyenizi girin.")

while True:
    try:
        bakiye = float(input("Baslangic bakiyesi: "))
        if bakiye > 0:
            break
        else:
            print("Gecersiz bakiyeler. Lutfen pozitif bir deger girin.")
    except ValueError:
        print("Lutfen gecerli bir sayi girin.")
while True:
    print("\nYapmak istediginiz islemi secin:")
    print("1: Para Yatirma")
    print("2: Para Cekme")
    print("3: Bakiye Goruntuleme")
    print("4: Cikis")
    secim = input("Seciminizi yapin (1/2/3/4): ")
    if secim == "1":
        try:
            miktar = float(input("Yatirmak istediginiz tutar: "))
            if miktar > 0:
                bakiye += miktar
                print(f"\n{miktar} TL yatirildi. Guncel bakiyeniz: {bakiye} TL")
            else:
                print("Gecersiz tutar. Lutfen pozitif bir miktar girin.")
        except ValueError:
            print("Lutfen gecerli bir sayi girin.")
    elif secim == "2":
        try:
            miktar = float(input("Cekmek istediginiz tutar: "))
            if miktar > 0:
                if miktar <= bakiye:
                    bakiye -= miktar
                    print(f"\n{miktar} TL cekildi. Guncel bakiyeniz: {bakiye} TL")
                else:
                    print("Yetersiz bakiye!")
            else:
                print("Gecersiz tutar. Lutfen pozitif bir miktar girin.")
        except ValueError:
            print("Lutfen gecerli bir sayi girin.")
    elif secim == "3":
        print(f"\nMevcut bakiyeniz: {bakiye} TL")
    elif secim == "4":
        print("\nCikis yapiliyor...")
        break
    else:
        print("\nGecersiz secim. Lutfen tekrar deneyin.")