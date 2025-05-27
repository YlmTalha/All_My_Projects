# Kullanıcıya listeyi gösterip işlem yaptırma
dizi1 = ["elma", "armut", "kiraz"]
dizi2 = ["muz", "portakal", "karpuz"]
birlesik_dizi = dizi1 + dizi2
print("Mevcut liste:", birlesik_dizi)

print("1) Tüm listeyi silmek.")
print("2) Tek bir eleman silmek icin.")
islem = input("Lütfen seçininizi yapiniz: ")


if islem == '1':
    birlesik_dizi.clear()
    print("Tüm liste silindi.")
    
elif islem == '2':
    index = int(input(f"Silmek istediğiniz elemanin index numarasini girin (0-5): "))

    if 0 <= index < len(birlesik_dizi):
        silinen = birlesik_dizi.pop(index)
        print(f"'{silinen}' elemani silindi.")

    else:
        print("Geçersiz index numarasi!")

else:
    print("Geçersiz seçim!")

print("Güncellenmiş liste:", birlesik_dizi)