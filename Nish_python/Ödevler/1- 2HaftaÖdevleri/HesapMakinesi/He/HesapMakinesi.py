sayi1 = float(input("Birinci sayiyi giriniz: "))
sayi2 = float(input("Ikinci sayiyi giriniz: "))
islem = input("Yapilacak islemi seciniz (+, -, *, /): ")

if islem == "+":
    sonuc = sayi1 + sayi2
    print(f"Sonuc: {sonuc}")
elif islem == "-":
    sonuc = sayi1 - sayi2
    print(f"Sonuc: {sonuc}")
elif islem == "*":
    sonuc = sayi1 * sayi2
    print(f"Sonuc: {sonuc}")
elif islem == "/":
    if sayi2 != 0:
        sonuc = sayi1 / sayi2
        print(f"Sonuc: {sonuc}")
    else:
        print("Hata: Bir sayi sifira bölünemez.")
else:
    print("Hata: Gecersiz islem türü.")