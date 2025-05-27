calisma_saati = float(input("Haftalik calisma saatinizi giriniz: "))

saatlik_ucret = 100
fazla_mesai_carpani = 1.5

if calisma_saati <= 40:
    toplam_ucret = calisma_saati * saatlik_ucret
else:
    normal_ucret = 40 * saatlik_ucret
    fazla_mesai_saati = calisma_saati - 40
    fazla_mesai_ucreti = fazla_mesai_saati * saatlik_ucret * fazla_mesai_carpani
    toplam_ucret = normal_ucret + fazla_mesai_ucreti

print(f"Toplam kazanciniz: {toplam_ucret} TL")