class Bank:
    def __init__(self, isim, bakiye=5000):
        self.isim = isim
        self.bakiye = bakiye
        print(f"{self.isim} adli kullanici icin banka hesabi olusturuldu. Baslangic bakiyesi: {self.bakiye} TL")
        
    def add_money(self, amount):
        if amount <= 0:
            print("Pozitif bir miktar yatirmaniz gerekiyor!")
        else:
            self.bakiye += amount
            print(f"Hesabiniza {amount} TL yatirildi. Guncel bakiye: {self.bakiye} TL")

    def withdraw_money(self, amount):
        if amount <= 0:
            print("Pozitif bir miktar cekmeniz gerekiyor!")
        elif amount > self.bakiye:
            print("Yetersiz bakiye! Cekmek istediginiz miktar mevcut bakiyeden fazla.")
        else:
            self.bakiye -= amount
            print(f"Hesabinizdan {amount} TL cekildi. Kalan bakiye: {self.bakiye} TL")
    
    def get_current_balance(self):
        print(f"Guncel bakiyeniz: {self.bakiye} TL")

def main():
    isim = input("Lutfen adinizi giriniz: ")
    hesap = Bank(isim)
    
    while True:
        print("\nLutfen bir islem seciniz:")
        print("1 - Para Yatirma")
        print("2 - Para Cekme")
        print("3 - Bakiye Sorgulama")
        print("4 - Cikis")
        
        secim = input("Seciminizi yapiniz (1/2/3/4): ")
        
        if secim == "1":
            miktar = float(input("Yatirmak istediginiz miktari giriniz: "))
            hesap.add_money(miktar)
        elif secim == "2":
            miktar = float(input("Cekmek istediginiz miktari giriniz: "))
            hesap.withdraw_money(miktar)
        elif secim == "3":
            hesap.get_current_balance()
        elif secim == "4":
            print("Cikis yapiliyor...")
            break
        else:
            print("Gecersiz secim, lutfen tekrar deneyin!")

if __name__ == "__main__":
    main()