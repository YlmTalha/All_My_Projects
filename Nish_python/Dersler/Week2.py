yil = int(input("doğum tarihini giriniz: "))
ad = input("isminizi giriniz: ")
cinsiyet = input("cinsiyetinizi giriniz: ")

yas = 2024 - yil

if cinsiyet == "erko" and yas >= 20:
    print("Askere git")
elif cinsiyet == "erko" and yas < 20:
    print("Askerlik yaşın gelmemiş")
else:
    print("Askerlik şart değil")    