vize1 = float(input("Lutfen Vize1 notunu girin: "))
vize2 = float(input("Lutfen Vize2 notunu girin: "))
final = float(input("Lutfen Final notunu girin: "))

ortalama = (vize1 * 0.30) + (vize2 * 0.30) + (final * 0.40)

if ortalama >= 85:
    harf_notu = "AA (Gecti)"
elif ortalama >= 75:
    harf_notu = "BA (Gecti)"
elif ortalama >= 65:
    harf_notu = "BB (Gecti)"
elif ortalama >= 50:
    harf_notu = "CC (Gecti)"
else:
    harf_notu = "FF (Kaldi)"

print(f"\nOrtalamaniz: {ortalama:.2f}")
print(f"Harf Notunuz: {harf_notu}")
