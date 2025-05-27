Kilo = float(input("Kilonuzu giriniz: "))
İcilenSu = float(input("Günlük tükettiğiniz su miktarini giriniz: "))
Suİhtiyaci = Kilo*0.03

if (Suİhtiyaci<2):
    print("Daha fazla su tüketmelisin!!!")
elif (2 <= Suİhtiyaci <=3 ):
    print("Su ihtiyacini karşilamişsin, harika!")
elif (Suİhtiyaci>3):
    print("Dikkat et, fazla su içme!")