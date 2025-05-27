#İlk olarak kullanıcıdan 2 sayı alıyoruz.
sayi1 = int(input("Birinci sayiyi giriniz : "))
sayi2 = int(input("İkinci sayiyi giriniz : "))

# Matematiksel Operatörler
print(f"{sayi1} + {sayi2} =", sayi1 + sayi2)  # Toplama
print(f"{sayi1} - {sayi2} =", sayi1 - sayi2)  # Çıkarma
print(f"{sayi1} * {sayi2} =", sayi1 * sayi2)  # Çarpma
print(f"{sayi1} // {sayi2} =", sayi1 // sayi2)  # Tamsayı Bölmesi
print(f"{sayi1} % {sayi2} =", sayi1 % sayi2)  # Mod (Kalan)
print(f"{sayi1} ** {sayi2} =", sayi1 ** sayi2)  # Üs alma

# Karşılaştırma Operatörleri
print(f"{sayi1} == {sayi2}:", sayi1 == sayi2)  # Eşit mi?
print(f"{sayi1} != {sayi2}:", sayi1 != sayi2)  # Eşit değil mi?
print(f"{sayi1} < {sayi2}:", sayi1 < sayi2)    # Küçük mü?
print(f"{sayi1} > {sayi2}:", sayi1 > sayi2)    # Büyük mü?
print(f"{sayi1} <= {sayi2}:", sayi1 <= sayi2)  # Küçük veya eşit mi?
print(f"{sayi1} >= {sayi2}:", sayi1 >= sayi2)  # Büyük veya eşit mi?

# Karışık karşılaştırmalı operatörler.
print(f"({sayi1} + 5) > ({sayi2} * 2):", (sayi1 + 5) > (sayi2 * 2))
print(f"({sayi1} % 4) == ({sayi2} % 4):", (sayi1 % 4) == (sayi2 % 4))