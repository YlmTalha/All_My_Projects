def donusum_hesaplayici():
    while True:
        print("Donusturmek istediginiz birimi secin:")
        print("1: Metre -> Kilometre")
        print("2: Kilometre -> Metre")
        print("3: Kilogram -> Gram")
        print("4: Gram -> Kilogram")
        print("5: Celsius -> Fahrenheit")
        print("6: Fahrenheit -> Celsius")
        print("7: Cikis")
        
        secim = input("Seciminizi yapin (1/2/3/4/5/6/7): ")
        
        if secim == "7":
            print("Cikis yapiliyor...")
            break
        
        deger = float(input("Donusturmek istediginiz degeri girin: "))
        
        if secim == "1":
            sonuc = deger / 1000
            print(f"{deger} metre = {sonuc} kilometre")
        elif secim == "2":
            sonuc = deger * 1000
            print(f"{deger} kilometre = {sonuc} metre")
        elif secim == "3":
            sonuc = deger * 1000
            print(f"{deger} kilogram = {sonuc} gram")
        elif secim == "4":
            sonuc = deger / 1000
            print(f"{deger} gram = {sonuc} kilogram")
        elif secim == "5":
            sonuc = (deger * 9/5) + 32
            print(f"{deger} Celsius = {sonuc} Fahrenheit")
        elif secim == "6":
            sonuc = (deger - 32) * 5/9
            print(f"{deger} Fahrenheit = {sonuc} Celsius")
        else:
            print("Gecersiz secim, lutfen tekrar deneyin.")
        
        print("\n")

donusum_hesaplayici()
