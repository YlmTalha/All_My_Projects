orijinal_liste = ["elma", "armut", "kiraz", "muz", "portakal"]

kopya_liste = orijinal_liste.copy()

kopya_liste.append("karpuz")
kopya_liste.remove("armut")
kopya_liste[1] = "çilek"

print("Orijinal liste:", orijinal_liste)
print("Kopya liste:", kopya_liste)