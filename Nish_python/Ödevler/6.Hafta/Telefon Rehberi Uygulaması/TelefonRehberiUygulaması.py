def menu():
    print("\nTelefon Rehberi")
    print("1. Kişi Ekle")
    print("2. Rehberi Listele")
    print("3. Kişi Sil")
    print("4. Çıkış")
    
telefon_rehberi = {}

def kisi_ekle():
    isim = input("Kişinin adını girin: ")
    telefon = input("Telefon numarasını girin: ")
    if isim in telefon_rehberi:
        print("Bu kişi zaten rehberde kayıtlı.")
    else:
        telefon_rehberi[isim] = telefon
        print(f"{isim} rehbere eklendi.")

def rehberi_listele():
    if not telefon_rehberi:
        print("Rehberde kayıtlı kişi bulunmamaktadır.")
    else:
        print("\nRehber Listesi:")
        for isim, telefon in telefon_rehberi.items():
            print(f"{isim}: {telefon}")

def kisi_sil():
    isim = input("Silmek istediğiniz kişinin adını girin: ")
    if isim in telefon_rehberi:
        del telefon_rehberi[isim]
        print(f"{isim} rehberden silindi.")
    else:
        print("Böyle bir kişi rehberde bulunmamaktadır.")

def ana_program():
    while True:
        menu()
        secim = input("Seçiminizi yapın (1-4): ")
        
        if secim == "1":
            kisi_ekle()
        elif secim == "2":
            rehberi_listele()
        elif secim == "3":
            kisi_sil()
        elif secim == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen 1-4 arasında bir seçim yapın.")

ana_program()
