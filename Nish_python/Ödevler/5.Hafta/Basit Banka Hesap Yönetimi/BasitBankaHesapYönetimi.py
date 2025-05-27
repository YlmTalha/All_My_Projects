import random #Kullanmamin amaci rastgele hesap numarasi üretmek!!!

def banka_hesap_yonetim_sistemi():
    hesaplar = {}
    
    while True:
        print("\n--- Banka Hesap Yonetim Sistemi ---")
        print("1. Yeni Hesap Ac")
        print("2. Hesaplari Listele")
        print("3. Para Yatir")
        print("4. Para Cek")
        print("5. Cikis")
        
        secim = input("Seciminizi yapin (1-5): ")
        
        if secim == "1":
            isim = input("Hesap sahibinin ismini girin: ")
            sifre = input("Sifre belirleyin: ")
            hesap_no = random.randint(100000, 999999)
            while hesap_no in hesaplar:
                hesap_no = random.randint(100000, 999999)
            hesaplar[hesap_no] = {'isim': isim, 'sifre': sifre, 'bakiye': 0}
            print(f"Hesap acildi! Hesap No: {hesap_no}")
        
        elif secim == "2":
            if hesaplar:
                print("\n--- Hesap Listesi ---")
                for hesap_no, bilgi in hesaplar.items():
                    print(f"Hesap No: {hesap_no}, Sahip: {bilgi['isim']}, Bakiye: {bilgi['bakiye']} TL")
            else:
                print("Henuz hesap acilmadi.")
        
        elif secim == "3":
            hesap_no = int(input("Para yatirmak icin hesap numarasini girin: "))
            if hesap_no in hesaplar:
                sifre = input("Sifrenizi girin: ")
                if sifre == hesaplar[hesap_no]['sifre']:
                    miktar = float(input("Yatirilacak miktari girin: "))
                    if miktar > 0:
                        hesaplar[hesap_no]['bakiye'] += miktar
                        print(f"{miktar} TL yatirildi. Yeni bakiye: {hesaplar[hesap_no]['bakiye']} TL")
                    else:
                        print("Gecersiz miktar!")
                else:
                    print("Hata: Sifre yanlis!")
            else:
                print("Hata: Hesap bulunamadi!")
        
        elif secim == "4":
            hesap_no = int(input("Para cekmek icin hesap numarasini girin: "))
            if hesap_no in hesaplar:
                sifre = input("Sifrenizi girin: ")
                if sifre == hesaplar[hesap_no]['sifre']:
                    miktar = float(input("Cekilecek miktari girin: "))
                    if 0 < miktar <= hesaplar[hesap_no]['bakiye']:
                        hesaplar[hesap_no]['bakiye'] -= miktar
                        print(f"{miktar} TL cekildi. Yeni bakiye: {hesaplar[hesap_no]['bakiye']} TL")
                    else:
                        print("Gecersiz miktar veya yetersiz bakiye!")
                else:
                    print("Hata: Sifre yanlis!")
            else:
                print("Hata: Hesap bulunamadi!")
        
        elif secim == "5":
            print("Cikis yapiliyor...")
            break
        
        else:
            print("Hatali giris! Lutfen 1-5 arasinda bir secim yapin.")

banka_hesap_yonetim_sistemi()
