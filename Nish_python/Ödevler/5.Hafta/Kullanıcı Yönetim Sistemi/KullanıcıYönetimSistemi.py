def ascii_toplam(isim):
    return sum(ord(char) for char in isim) 

def kullanici_yonetim_sistemi():
    kullanicilar = {}  

    while True:
        print("\n--- Kullanici Yonetim Sistemi ---")
        print("1. Kullanici Ekle")
        print("2. Kullanici Sil")
        print("3. Kullanicilari Listele")
        print("4. Cikis")
        
        secim = input("Seciminizi yapin (1-4): ")
        
        if secim == "1":
            isim = input("Kullanici ismi girin: ")
            id = ascii_toplam(isim)  # ID'yi kullanicinin ismindeki harflerin ASCII karsiligi olan sayilarla toplama işlemi yapıyoruz.
            
            if id in kullanicilar:
                print("Hata: Bu isimle ayni ID'ye sahip kullanici var!")
            else:
                kullanicilar[id] = isim
                print(f"Kullanici eklendi: {id} - {isim}")
        
        elif secim == "2":
            id = int(input("Silinecek kullanici ID girin: "))
            if id in kullanicilar:
                del kullanicilar[id]
                print(f"{id} ID'li kullanici silindi.")
            else:
                print("Hata: Bu ID sistemde bulunamadi!")
        
        elif secim == "3":
            if kullanicilar:
                print("\n--- Kullanici Listesi ---")
                for id, isim in kullanicilar.items():
                    print(f"{id}: {isim}")
            else:
                print("Henuz kullanici eklenmedi.")
        
        elif secim == "4":
            print("Cikis yapiliyor...")
            break
        
        else:
            print("Hatali giris! Lutfen 1-4 arasinda bir secim yapin.")

kullanici_yonetim_sistemi()