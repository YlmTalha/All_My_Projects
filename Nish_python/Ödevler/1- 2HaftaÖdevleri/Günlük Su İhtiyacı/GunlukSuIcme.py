kilo = float(input("Lütfen kilonuzu giriniz: "))

gunluk_su_ihtiyaci = kilo * 0.03

if gunluk_su_ihtiyaci < 2:
    tavsiye = "Daha fazla su içmelisiniz."
elif 2 <= gunluk_su_ihtiyaci <= 3:
    tavsiye = "Su ihtiyacinizi karşiliyorsunuz, böyle devam edin!"
else:
    tavsiye = "Fazla su içmemeye dikkat edin."

print(f"Günlük su ihtiyaciniz: {gunluk_su_ihtiyaci:.2f} litre.")
print(tavsiye)