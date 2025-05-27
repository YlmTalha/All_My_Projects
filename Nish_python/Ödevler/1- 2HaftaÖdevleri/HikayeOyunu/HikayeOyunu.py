print("Buyulu bir ormanda kayboldunuz. Ne yapmak istersiniz?")
print("1: Magaraya gitmek")

print("2: Ormanda kalmak")

secim1 = input("Seciminizi yapin (1/2): ")

if secim1 == "1":
    print("Magaraya girdiniz ve bir ejderha ile karsilastiniz!")
    print("1: Ejderhaya yaklasmak")
    print("2: Saklanmak")
    
    secim2 = input("Seciminizi yapin (1/2): ")
    
    if secim2 == "1":
        print("Ejderha size bakiyor ve cesur olup olmadiginizi soruyor.")
    
        cesaret = input("Cesur musunuz? (evet/hayir): ")
    
        if cesaret.lower() == "evet":
            print("Ejderha cesaretinizi odullendirdi! Altin bir hazine kazandiniz.")
            print("Hazineyi alarak buyuk bir kasabaya gittiniz ve orada yeni bir hayat kurdunuz.")
            print("Ancak kasabada garip bir gizemle karsilastiniz: Her gece saat tam 12'de bir kiliseden tuhaf sesler geliyordu.")
    
            secim4 = input("Bu olayi arastirmak ister misiniz? (evet/hayir): ")
    
            if secim4.lower() == "evet":
                print("Kilisedeki sesleri takip ederek gizli bir bolmeye ulastiniz. Burada antik bir kitap buldunuz ve buyuk bir sirri kesfettiniz!")
    
            else:
                print("Gizemle ilgilenmeden sakin bir hayat yasamayi sectiniz. Hikayeniz burada sona eriyor.")
    
        else:
            print("Ejderha sizi magaradan disari atti. Sansinizi baska yerde denemelisiniz!")
    
    elif secim2 == "2":
        print("Saklandiniz, ancak ejderha sizi buldu ve korktugunuzu anladı. Maalesef basarisiz oldunuz.")
    
    else:
        print("Gecersiz secim. Ejderha sizi fark etti ve kacmaniza izin vermedi.")

elif secim1 == "2":
    print("Ormanda kalmayi sectiniz ve bir nehirle karsilastiniz.")
    print("1: Nehri yuzerek gecmek")
    print("2: Kopru aramak")

    secim3 = input("Seciminizi yapin (1/2): ")

    if secim3 == "1":
        print("Nehri yuzerek gecmeye calisiyorsunuz, ancak tehlikeli bir balik size saldirdi!")
        print("Baliktan kacip bir adaya sigindiniz. Adada bir sandik buldunuz. Sandigi acmak icin bir sifre gerekiyor.")

        sifre = input("Sandik sifresini tahmin edin (3 basamakli bir sayi): ")

        if sifre == "123":
            print("Sandigi actiniz ve icinde eski bir harita buldunuz. Harita sizi gizemli bir hazineye goturuyor!")
            print("Haritayi takip ederek unutulmus bir tapinaga ulastiniz. Tapinagin icinde sizi bekleyen yeni bir macera basliyor!")

        else:
            print("Yanlis sifre! Sandik acilmadi ve adada mahsur kaldiniz.")

    elif secim3 == "2":
        print("Bir kopru aradiniz ve sonunda guvenli bir sekilde nehri gectiniz.")
        print("Karsiya gectikten sonra harika bir sehre ulastiniz ve maceranizi basariyla tamamladiniz!")
        print("Ancak sehirde bir tufan basladi ve halk sizden yardim istedi. Bir kahraman olarak yeni bir yolculuga ciktiniz.")

    else:
        print("Gecersiz secim. Nehirde kayboldunuz.")

else:
    print("Gecersiz secim. Ormanda kaybolmaya devam ediyorsunuz.")