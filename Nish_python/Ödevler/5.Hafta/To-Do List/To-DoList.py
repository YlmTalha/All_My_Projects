mevcut_id = 1  
def gorev_yonetim_sistemi():
    gorevler = {}

    while True:
        print("\n--- To-Do List ---")
        print("1. Yeni Gorev Ekle")
        print("2. Tum Gorevleri Listele")
        print("3. Gorevi Tamamla")
        print("4. Tamamlanan Gorevleri Goster")
        print("5. Cikis Yap")
        
        secim = input("Seciminizi yapin (1-5): ")
        
        if secim == "1":
            global mevcut_id
            ad = input("Gorev adini girin: ")
            gorevler[mevcut_id] = {'ad': ad, 'tamamlandi': False}
            print(f"Gorev eklendi: {mevcut_id} - {ad}")
            mevcut_id += 1  
        
        elif secim == "2":
            if gorevler:
                print("\n--- Tum Gorevler ---")
                for id, bilgi in gorevler.items():
                    durum = "Tamamlandi" if bilgi['tamamlandi'] else "Devam Ediyor"
                    print(f"{id}: {bilgi['ad']} - {durum}")
            else:
                print("Henuz gorev eklenmedi.")
        
        elif secim == "3":
            id = int(input("Tamamlanacak gorev ID'sini girin: "))
            if id in gorevler:
                gorevler[id]['tamamlandi'] = True
                print(f"{id} ID'li gorev tamamlandi.")
            else:
                print("Hata: Bu ID sistemde bulunamadi!")
        
        elif secim == "4":
            tamamlanan_gorevler = {id: gorev for id, gorev in gorevler.items() if gorev['tamamlandi']}
            if tamamlanan_gorevler:
                print("\n--- Tamamlanan Gorevler ---")
                for id, bilgi in tamamlanan_gorevler.items():
                    print(f"{id}: {bilgi['ad']}")
            else:
                print("Henuz hicbir gorev tamamlanmadi.")
        
        elif secim == "5":
            print("Cikis yapiliyor...")
            break
        
        else:
            print("Hatali giris! Lutfen 1-5 arasinda bir secim yapin.")

gorev_yonetim_sistemi()
