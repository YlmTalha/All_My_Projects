class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []
        print(f"{self.name} adli ogrenci olusturuldu. Ogrenci Numarasi: {self.student_id}")
    
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
            print(f"{self.name} adli ogrenciye {grade} notu eklendi.")
        else:
            print("Gecersiz not! Not 0 ile 100 arasinda olmalidir.")
    
    def calculate_average(self):
        if not self.grades:
            print("Hic not girilmemis.")
            return 0
        average = sum(self.grades) / len(self.grades)  #"sum" total değer, "len" ise eleman sayisini gösterir
        print(f"{self.name} adli ogrencinin not ortalamasi: {average:.2f}")
        return average
    
    def display_info(self):
        print(f"Ogrenci Bilgileri -> Ad: {self.name}, Numarasi: {self.student_id}, Notlari: {self.grades}")

def main():
    name = input("Ogrencinin adini giriniz: ")
    student_id = input("Ogrencinin numarasini giriniz: ")
    student = Student(name, student_id)
    
    while True:
        print("\nLutfen bir islem seciniz:")
        print("1 - Not Ekle")
        print("2 - Not Ortalamasini Hesapla")
        print("3 - Ogrenci Bilgilerini Goster")
        print("4 - Cikis")
        
        secim = input("Seciminizi yapiniz (1/2/3/4): ")
        
        if secim == "1":
            grade = float(input("Eklemek istediginiz notu giriniz: "))
            student.add_grade(grade)
        elif secim == "2":
            student.calculate_average()
        elif secim == "3":
            student.display_info()
        elif secim == "4":
            print("Cikis yapiliyor...")
            break
        else:
            print("Gecersiz secim, lutfen tekrar deneyin!")

if __name__ == "__main__":
    main()