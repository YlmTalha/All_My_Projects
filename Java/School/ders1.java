import java.util.Scanner;
class ders1{
	public static void main(String[] args){
		try (Scanner scan = new Scanner(System.in)) {
			int sayi = scan.nextInt();
			int toplam = 0;
			do{
				toplam += sayi%10;
				sayi = sayi/10;
				System.out.println("Toplam=" + toplam + "sayi= " +sayi);
			
			}
			while(sayi > 0);
			System.out.println("Toplam = " + toplam);
		}

	}
}
