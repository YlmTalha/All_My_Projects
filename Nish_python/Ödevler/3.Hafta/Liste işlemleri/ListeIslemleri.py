# Iki diziyi birleştirme
dizi1 = ["elma", "armut", "kiraz"]
dizi2 = ["muz", "portakal", "karpuz"]
birlesik_dizi = dizi1 + dizi2
print("Birlesik dizi:", birlesik_dizi)

# Sonuna eleman ekleme
birlesik_dizi.append("ananas")
print("Sonuna ekleme:", birlesik_dizi)

# Normal eleman ekleme (belirli bir yere)
birlesik_dizi.insert(2, "çilek")
print("Belirli yere ekleme:", birlesik_dizi)

# Index numarasına göre eleman değiştirme
birlesik_dizi[1] = "erik"
print("Index numarasina göre değiştirme:", birlesik_dizi)

# Index aralığına göre eleman değiştirme
birlesik_dizi[3:5] = ["kivi", "nar"]
print("Index araliğina göre değiştirme:", birlesik_dizi)

# Alfabetik sıralama
birlesik_dizi.sort()
print("Alfabetik siralama:", birlesik_dizi)

# Tersine göre alfabetik sıralama
birlesik_dizi.sort(reverse=True)
print("Tersine göre alfabetik siralama:", birlesik_dizi)

# Direkt tersine sıralama
birlesik_dizi.reverse()
print("Direkt tersine siralama:", birlesik_dizi)

# Eleman adına göre silme
birlesik_dizi.remove("kivi")
print("Eleman adina göre silme:", birlesik_dizi)

# Son elemana göre silme
birlesik_dizi.pop()
print("Son elemana göre silme:", birlesik_dizi)