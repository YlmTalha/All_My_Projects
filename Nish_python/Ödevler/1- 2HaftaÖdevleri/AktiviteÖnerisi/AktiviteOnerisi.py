yas = int(input("Lutfen yasinizi giriniz: "))

print("Aktivite seviyenizi seciniz:")
print("1 - Standart (Hareketsiz yasam tarzi)")
print("2 - Orta Duzey Aktivite")
print("3 - Yuksek Aktivite")
aktivite_seviyesi = int(input("Aktivite seviyesi (1, 2 veya 3): "))

if yas < 18:
    print("18 yas altindaki bireyler icin oneriler bu programa dahil edilmemistir.")
elif 18 <= yas <= 30:
    if aktivite_seviyesi == 1:
        print("Gunluk 30 dakikalik yuruyus onerilir.")
    elif aktivite_seviyesi == 2:
        print("Haftada birkac gun hafif egzersiz veya yoga yapabilirsiniz.")
    elif aktivite_seviyesi == 3:
        print("Duzenli spor yapmaya devam edin. Kardiyo ve kuvvet antrenmanlari tavsiye edilir.")
    else:
        print("Gecerli bir aktivite seviyesi secmediniz.")
elif yas > 30:
    if aktivite_seviyesi == 1:
        print("Gunde 20-30 dakikalik hafif yuruyus veya dusuk tempolu egzersiz onerilir.")
    elif aktivite_seviyesi == 2:
        print("Haftada 3-4 gun orta duzey egzersiz yapabilirsiniz. Ornegin yuzme veya bisiklet surme.")
    elif aktivite_seviyesi == 3:
        print("Daha yogun egzersizler veya spor salonu programlari onerilir. Ancak profesyonel bir rehberle calismaniz faydali olabilir.")
    else:
        print("Gecerli bir aktivite seviyesi secmediniz.")
else:
    print("Gecerli bir yas girmediniz.")