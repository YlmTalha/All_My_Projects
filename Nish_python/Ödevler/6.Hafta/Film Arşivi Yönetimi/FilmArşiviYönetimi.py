def menu():
    print("\nFilm Arşivi")
    print("1. Film Ekle")
    print("2. Arşivi Listele")
    print("3. Film Sil")
    print("4. Çıkış")
    
film_arsivi = []

def film_ekle():
    ad = input("Filmin adını girin: ")
    yonetmen = input("Yönetmenin adını girin: ")
    yil = input("Filmin yayın yılını girin: ")
    film_arsivi.append({"Ad": ad, "Yönetmen": yonetmen, "Yıl": yil}) #.append listeye yeni eleman eklemek için kullandım.
    print(f"{ad} arşive eklendi.")

def arsivi_listele():
    if not film_arsivi:
        print("Arşivde kayıtlı film bulunmamaktadır.")
    else:
        print("\nFilm Arşivi:")
        for film in film_arsivi:
            print(f"Ad: {film['Ad']}, Yönetmen: {film['Yönetmen']}, Yıl: {film['Yıl']}")

def film_sil():
    ad = input("Silmek istediğiniz filmin adını girin: ")
    for film in film_arsivi:
        if film["Ad"] == ad:
            film_arsivi.remove(film)
            print(f"{ad} arşivden silindi.")
            return
    print("Böyle bir film arşivde bulunmamaktadır.")

def ana_program():
    while True:
        menu()
        secim = input("Seçiminizi yapın (1-4): ")
        
        if secim == "1":
            film_ekle()
        elif secim == "2":
            arsivi_listele()
        elif secim == "3":
            film_sil()
        elif secim == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen 1-4 arasında bir seçim yapın.")

ana_program()
