#Değişken Tanımlama Kuralları

# Geçerli değişken isimleri
deger = 10
deger_2 = 20
numara1 = 5

# Geçersiz değişken isimleri
''' 
1deger = 10   Başlangıç rakamla olamaz
if = 20       Anahtar kelime kullanılamaz
'''

#Değişken Türleri
x1 = 10       # int
y1 = 3.14     # float
z1 = "Python" # str
liste = [1, 2, 3]  # list
sozluk = {"ad": "Ahmet", "yas": 25}  # dict (sözlük)
sayilar = {1, 2, 3} # set (küme)
renkler = ("Kırmızı", "Yeşil", "Mavi") # tuple (değiştirilemez liste)
dogru_mu = True     # bool (mantıksal değer)
yanlis_mi = False   # bool (mantıksal değer)
bos_deger = None    # NoneType (boş değer)
z = 3 + 4j          # complex (karmaşık sayı)

#Bellek Yönetimi ve Performans
import sys 
""" 
Bunu kullanmamızın sebebi, bir nesnenin bellekte ne kadar yer kapladığını öğrenmek için 
"sys.getsizeof()" komutunu koda dahil etmektir.
"""

x2 = 10
y2 = "Python"
z2 = [1, 2, 3]
print(f"\nint bellek kullanımı: {sys.getsizeof(x2)} bytes")
print(f"str bellek kullanımı: {sys.getsizeof(y2)} bytes")
print(f"list bellek kullanımı: {sys.getsizeof(z2)} bytes \n")