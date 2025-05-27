boy = float(input("Boyunuzu (metre cinsinden) girin: "))
kilo = float(input("Kilonuzu (kg cinsinden) girin: "))

bmi = kilo / (boy ** 2)

#metre cinsinden boyunuzu girmeye özen gösterin !(örnek:1.75)!
#.2f kullanmam çok uzun bir ondalık sayı göstermesin ve bunu yuvarlasın diye.

if bmi < 18.5:
    print(f"Vücut Kitle Endeksiniz: {bmi:.2f} - Zayif")
elif 18.5 <= bmi < 24.9:
    print(f"Vücut Kitle Endeksiniz: {bmi:.2f} - Normal")
elif 25 <= bmi < 29.9:
    print(f"Vücut Kitle Endeksiniz: {bmi:.2f} - Kilolu")
else:
    print(f"Vücut Kitle Endeksiniz: {bmi:.2f} - Obez")