yas = int(input("Lutfen yasinizi girin: "))
spor_gecmisi = input("Daha once spor yaptiniz mi? (Evet/Hayir): ").lower()
odeme = float(input("Lutfen odeyeceginiz tutari girin (TL): "))

if yas < 18 or yas > 50:
    print("Uyelik reddedildi: Yasiniz 18 ile 50 arasinda olmalidir.")
else:
    if spor_gecmisi == "evet" and odeme > 1000:
        print("Uyeliginiz onaylandi. Hos geldiniz!")
    else:
        print("Uyelik reddedildi: Spor gecmisi olumlu olmali ve odeme tutariniz 1000 TL'den fazla olmalidir.")