print("BMR Hesaplama Programina Hoş Geldiniz!")

# Kullanıcıdan bilgileri al
cinsiyet = input("Cinsiyetinizi girin (Erkek/Kadin): ").strip().lower()
yaş = int(input("Yaşinizi girin: "))
kilo = float(input("Kilonuzu girin: "))
boy = float(input("Boyunuzu (cm) girin: "))

# BMR hesaplama
if cinsiyet == "erkek":
    bmr = 88.362 + (13.397 * kilo) + (4.799 * boy) - (5.677 * yaş)
elif cinsiyet == "kadin":
    bmr = 447.593 + (9.247 * kilo) + (3.098 * boy) - (4.330 * yaş)
else:
    print("Hatali bir cinsiyet girdiniz. Lütfen 'Erkek' veya 'Kadin' olarak giriniz.")
    bmr = None

# Sonucu yazdır
if bmr is not None:
    print(f"\nHesaplanan BMR: {bmr:.2f} kalori/gün")
