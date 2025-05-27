film1 = input("1. favori filminizi girin: ")
film2 = input("2. favori filminizi girin: ")
film3 = input("3. favori filminizi girin: ")
film4 = input("4. favori filminizi girin: ")
film5 = input("5. favori filminizi girin: ")

filmler = [film1, film2, film3, film4, film5]

filmler.sort()

print("\nAlfabetik siraya gore siralanmis filmler:")
for index, film in enumerate(filmler):
    print(f"{index + 1}. {film}")

degisim_index = int(input("\nHangi filmi degistirmek istersiniz? ")) - 1
if 0 <= degisim_index < len(filmler):
    yeni_film = input("Yeni film adini girin: ")
    filmler[degisim_index] = yeni_film
else:
    print("Gecersiz sira numarasi!")

filmler.sort()

print("\nGuncellenmis ve alfabetik siraya gore siralanmis filmler:")
#"enumerate" kullanmamın sebebi index ile filmi birlikte daha kısa kodda yazmak. 
for index, film in enumerate(filmler):
    print(f"{index + 1}. {film}")