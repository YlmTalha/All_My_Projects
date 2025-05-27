class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
        print(f"{self.name} adli calisan olusturuldu. Departman: {self.department}, Maas: {self.salary} TL")
    
    def give_raise(self, amount):
        if amount <= 0:
            print("Zam miktari pozitif olmali!")
        else:
            self.salary += amount
            print(f"{self.name} adli calisana {amount} TL zam yapildi. Yeni maas: {self.salary} TL")
    
    def display_info(self):
        print(f"Calisan Bilgileri -> Ad: {self.name}, Departman: {self.department}, Maas: {self.salary} TL")

def main():
    name = input("Calisanin adini giriniz: ")
    department = input("Calisanin departmanini giriniz: ")
    salary = float(input("Calisanin maasini giriniz: "))
    employee = Employee(name, department, salary)
    
    while True:
        print("\nLutfen bir islem seciniz:")
        print("1 - Maas Zam Yap")
        print("2 - Calisan Bilgilerini Goster")
        print("3 - Cikis")
        
        secim = input("Seciminizi yapiniz (1/2/3): ")
        
        if secim == "1":
            miktar = float(input("Yapilacak zam miktarini giriniz: "))
            employee.give_raise(miktar)
        elif secim == "2":
            employee.display_info()
        elif secim == "3":
            print("Cikis yapiliyor...")
            break
        else:
            print("Gecersiz secim, lutfen tekrar deneyin!")

if __name__ == "__main__":
    main()