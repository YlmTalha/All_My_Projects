#1 Örtük Dönüşüm (Implicit Type Conversion)
sayi1 = 5     # int
sayi2 = 3.2   # float
sonuc = sayi1 + sayi2  # Python, int'i float'a dönüştürür, nedeni int le float toplandığında otomatik olarak floata çevirmesidir.
print("\n",sonuc)  # 8.2
print(type(sonuc), "\n")  # <class 'float'>

#2 Açık Dönüşüm (Explicit Type Conversion)
sayi = "166"  # string
sayi_int = int(sayi)  # string'i int'e dönüştürür
print(sayi_int, "\n")  # 166  

#3 float sayiyi int sayiya dönüştürürken oluşan veri kaybı örneği.
sayi = 5.73 # Ondalıklı kısmı kaybetmemize neden olur.
print(int(sayi), "\n")  # 5

#4 Hata Yönetimi
try:
    sayi = int("abc")  # Burda'da verilen string değeri int'e dönüştürmeye çalışılıyor. "abc" nin sayı değeri olmadığı için böyle bir işlem gerçekleşmeyecektir. 
except ValueError:
    print("Geçersiz girdi, sayıya dönüştürülemez!", "\n")

#5 String ve Sayılar Arasındaki Dönüşümler
sayi = "123.45"         # 4. örnekte açıklamış olduğum kısmı sayılar ile gerçekleştirdiğimizde gerçekleşmiş olduğunu görüyoruz.
print(int(float(sayi)), "\n")  # 123

#6 Booleen Dönüşümü
print(bool(0))  # False  bool(0) ifadesi False döndürür çünkü Python'da 0 değeri False olarak kabul edilir
print(bool(1))  # True   bool(1) ise True döndürür çünkü herhangi bir sıfırdan farklı sayı True olarak kabul edilir.
print(bool(2))  # True   bool(2) ise 0 dan farklı bir değer olduğu için tekrardan "True" döndürecektir.