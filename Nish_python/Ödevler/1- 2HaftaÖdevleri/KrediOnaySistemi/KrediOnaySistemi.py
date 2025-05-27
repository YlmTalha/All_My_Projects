yas = int(input("Lutfen yasinizi girin: "))
gelir = float(input("Lutfen aylik gelirinizin tutarini girin (TL): "))
kredi_notu = int(input("Lutfen kredi notunuzu girin: "))

if yas < 18:
    print("Kredi basvurusu reddedildi: Yasiniz 18'den kucuk, kredi basvurusu yapamazsiniz.")
else:
    if gelir < 5000:
        print("Kredi basvurusu reddedildi: Geliriniz 5000 TL'den dusuk.")
    else:
        # Kredi notu kontrolu
        if kredi_notu >= 600:
            print("Kredi onaylandi!")
        elif 500 <= kredi_notu < 600:
            print("Kredi degerlendirmeye alindi.")
        else:
            print("Kredi basvurusu reddedildi: Kredi notunuz 500'un altinda.")