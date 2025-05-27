orijinal_liste = ["elma", "armut", "kiraz", "muz", "portakal"]

paylasilan_liste = orijinal_liste

paylasilan_liste.append("karpuz")  
paylasilan_liste.remove("armut") 
paylasilan_liste[1] = "çilek"  

print("Orijinal liste:", orijinal_liste)
print("Paylaşilan liste:", paylasilan_liste)