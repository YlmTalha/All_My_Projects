yas = int(input("Yasinizi giriiniz: "))

print("1 Hareketsiz yaşam")
print("2 Orta düzey yaşam tarzi")
print("3 Hareketli yaşanti")

a = int(input("Aktivite seviyenizi seciniz: "))

if( 18 <= yas <= 30 ):
    if (a == 1):
        print("Günlük hafif yürüyüş")

    elif a==2:
        print("Haftada birkaç gün egzersiz yapmalisin ")
    
    elif a==3:
        print("Daha yoğun egzersiz ")
else:   
        print("aa")