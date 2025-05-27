import random

def adam_asmaca():
    kelimeler = ["python", "programlama", "bilgisayar", "yazilim", "kodlama"]
    secilen_kelime = random.choice(kelimeler)
    gizli_kelime = ["_" for _ in secilen_kelime]
    yanlis_tahmin_sayisi = 0
    max_hak = 5
    
    adam_cizimi = [
        "\n  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========" ,
        "\n  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========" ,
        "\n  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========" ,
        "\n  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========" ,
        "\n  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========" ,
        "\n  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="
    ]
    
    print("\nAdam Asmaca Oyununa Hos Geldiniz!\n")
    
    while yanlis_tahmin_sayisi < max_hak and "_" in gizli_kelime:
        print(adam_cizimi[yanlis_tahmin_sayisi])
        print("\nKelime: " + " ".join(gizli_kelime))
        tahmin = input("Bir harf tahmin edin: ").lower()
        
        if len(tahmin) != 1 or not tahmin.isalpha():
            print("Lutfen sadece tek bir harf girin!\n")
            continue
        
        if tahmin in gizli_kelime:
            print("Bu harfi zaten buldunuz! Baska bir harf deneyin.\n")
            continue
        
        if tahmin in secilen_kelime:
            print("Dogru tahmin! Harf yerine yerlestirildi.\n")
            for index, harf in enumerate(secilen_kelime):
                if harf == tahmin:
                    gizli_kelime[index] = tahmin
        else:
            yanlis_tahmin_sayisi += 1
            print(f"Yanlis tahmin! Kalan hak: {max_hak - yanlis_tahmin_sayisi}\n")
        
    print(adam_cizimi[yanlis_tahmin_sayisi])
    if "_" not in gizli_kelime:
        print("\nTebrikler! Kelimeyi dogru tahmin ettiniz: " + "".join(gizli_kelime))
    else:
        print(f"\nMaalesef kaybettiniz! Dogru kelime: {secilen_kelime}\n")

adam_asmaca()
