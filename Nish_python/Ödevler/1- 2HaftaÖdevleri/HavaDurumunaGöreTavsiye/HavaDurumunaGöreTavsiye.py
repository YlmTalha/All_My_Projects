sicaklik = float(input("Hava sicakligini giriniz (°C): "))

if sicaklik < 10:
    print("Hava cok soguk! Kalin kiyafetler giyin.")
elif 10 <= sicaklik < 20:
    print("Hava serin. Bir ceket giymeniz iyi olur.")
elif 20 <= sicaklik < 30:
    print("Hava ilik. Hafif giysiler tercih edebilirsiniz.")
else:
    print("Hava sicak! Ince ve serin tutacak kiyafetler giyin.")
