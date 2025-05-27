mevcut_id = 1  
def kutuphane_yonetim_sistemi():
    kitaplar = {}  

    while True:
        print("\n--- Kutuphane Yonetim Sistemi ---")
        print("1. Yeni Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitaplari Listele")
        print("4. Cikis")
        
        secim = input("Seciminizi yapin (1-4): ")
        
        if secim == "1":
            global mevcut_id
            isim = input("Kitap ismi girin: ")
            kitaplar[mevcut_id] = isim
            print(f"Kitap eklendi: {mevcut_id} - {isim}")
            mevcut_id += 1  
        
        elif secim == "2":
            id = int(input("Silinecek kitap ID girin: "))
            if id in kitaplar:
                del kitaplar[id]
                print(f"{id} ID'li kitap silindi.")
            else:
                print("Hata: Bu ID sistemde bulunamadi!")
        
        elif secim == "3":
            if kitaplar:
                print("\n--- Kitap Listesi ---")
                for id, isim in kitaplar.items():
                    print(f"{id}: {isim}")
            else:
                print("Henuz kitap eklenmedi.")
        
        elif secim == "4":
            print("Cikis yapiliyor...")
            break
        
        else:
            print("Hatali giris! Lutfen 1-4 arasinda bir secim yapin.")
            
kutuphane_yonetim_sistemi()
