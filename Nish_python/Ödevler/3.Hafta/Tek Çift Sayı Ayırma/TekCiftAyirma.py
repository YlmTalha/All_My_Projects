sayilar = []
tek_sayilar = []
cift_sayilar = []
for i in range(10):
#Burda try except kullanmamın sebebi sayı yerine başka birşey girildiğinde program kapanmasın diye.
    try:
        sayi = int(input(f"{i+1}. sayiyi girin: "))  # Kullanıcıdan sayı alın
        sayilar.append(sayi)  # Tüm sayıları sayilar listesine ekle

        if sayi % 2 == 0:
            cift_sayilar.append(sayi)  # Çift sayılar listesine ekle
        else:
            tek_sayilar.append(sayi)  # Tek sayılar listesine ekle
    except ValueError:
        print("Lütfen geçerli bir sayi girin!")
        continue

print("Tüm sayilar listesi:", sayilar)
print("Tek sayilar listesi:", tek_sayilar)
print("Çift sayilar listesi:", cift_sayilar)

birlesik_liste = tek_sayilar + cift_sayilar
birlesik_liste.sort()

print("Birlesik ve sirali liste:", birlesik_liste)