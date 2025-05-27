from collections import Counter

def harf_sikligi(metin):
    return dict(Counter(metin))

metin = input("Bir metin giriniz: ")
siklik = harf_sikligi(metin)

print("Harf Sikligi:")
print(siklik)