ay_numarasi = int(input("Lütfen bir ay numarasi girin (1-12): "))

if 1 <= ay_numarasi <= 12:
    if ay_numarasi in [12, 1, 2]:
        print("Kiş Mevsimi")
    elif ay_numarasi in [3, 4, 5]:
        print("İlkbahar Mevsimi")
    elif ay_numarasi in [6, 7, 8]:
        print("Yaz Mevsimi")
    elif ay_numarasi in [9, 10, 11]:
        print("Sonbahar Mevsimi")
else:
    print("Geçersiz ay numarasi. Lütfen 1 ile 12 arasinda bir sayi girin.")
