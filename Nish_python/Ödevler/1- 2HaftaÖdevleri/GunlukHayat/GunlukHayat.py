# Aktivite 1: Susuzluk durumu
susuzluk = input("Susuzluk seviyenizi girin (düşük, orta, yüksek): ").strip().lower()

if susuzluk == "yüksek":
    print("Hemen su içmelisin!")
elif susuzluk == "orta":
    print("Bir bardak su içmek faydali olabilir.")
else:
    print("Şimdilik su içmene gerek yok.")

# Aktivite 2: Yemek yeme durumu
aclik = input("Açlik seviyenizi girin (düşük, orta, yüksek): ").strip().lower()

if aclik == "yüksek":
    print("Yemek yemelisin!")
elif aclik == "orta":
    print("Bir ara öğün iyi olabilir.")
else:
    print("Yemek yemene gerek yok, biraz bekleyebilirsin.")

# Aktivite 3: Uyuma isteği, Egzersiz yapma isteği veya Sosyal etkinlik tercihi
aktivite = input("Hangi aktiviteyi yapmak istersiniz? (uyuma, egzersiz, sosyal): ").strip().lower()

if aktivite == "uyuma":
    print("Biraz dinlenmelisin!")
elif aktivite == "egzersiz":
    print("Egzersiz yaparak vücudunu canlandirabilirsin!")
elif aktivite == "sosyal":
    print("Arkadaşlarinla vakit geçirmek iyi bir fikir!")
else:
    print("Geçerli bir aktivite seçmedin.")