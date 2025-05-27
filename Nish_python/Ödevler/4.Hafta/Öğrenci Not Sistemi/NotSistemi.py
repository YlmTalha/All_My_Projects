def harf_notu_belirle(notlar):
    if notlar >= 90:
        return 'A'
    elif 80 <= notlar < 90:
        return 'B'
    elif 70 <= notlar < 80:
        return 'C'
    elif 60 <= notlar < 70:
        return 'D'
    else:
        return 'F'

ogrenciler = {}
n = int(input("Kaç öğrenci girmek istiyorsunuz? "))

for _ in range(n):
    isim = input("Öğrenci ismi: ")
    notu = float(input(f"{isim} adli öğrencinin notu: "))
    ogrenciler[isim] = notu

harf_notlari = {isim: harf_notu_belirle(notu) for isim, notu in ogrenciler.items()}

print("Öğrencilerin harf notlari:")
for isim, harf in harf_notlari.items():
    print(f"{isim}: {harf}")