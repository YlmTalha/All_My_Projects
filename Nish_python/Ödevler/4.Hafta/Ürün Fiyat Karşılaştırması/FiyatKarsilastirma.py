urun_fiyatlari = {}
n = int(input("Kaç mağaza bilgisi girmek istiyorsunuz? "))

for _ in range(n):
    magaza = input("Mağaza adi: ")
    fiyat = float(input(f"{magaza} mağazasindaki fiyat: "))
    urun_fiyatlari[magaza] = fiyat

en_ucuz_magaza = min(urun_fiyatlari, key=urun_fiyatlari.get)
en_ucuz_fiyat = urun_fiyatlari[en_ucuz_magaza]

print("\nMağaza ve Fiyatlar:")
for magaza, fiyat in urun_fiyatlari.items():
    print(f"{magaza}: {fiyat:.2f} TL")

print(f"\nEn ucuz mağaza: {en_ucuz_magaza} ({en_ucuz_fiyat:.2f} TL)")