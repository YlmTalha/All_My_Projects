import java.util.Scanner;
class hesapmakinesi{
	public static void main(String[] args){
		try (Scanner scan = new Scanner(System.in)) {
			int bakiye=1000;
			int islem;		

			System.out.println("1:Bakiyeyi görüntüle");
			System.out.println("2:Para cekme");
			System.out.println("3:Para yatirma");
			System.out.println("4:Sistemden cikis");
			
			islem = scan.nextInt();

			switch(islem){
			
				case 1:
					System.out.println("bakiyeniz" + bakiye + "Tl'dir");
			
				break;

				case 2:
					System.out.println("Ne kadar cekeceksiniz?");
					int miktar1 = scan.nextInt();

					bakiye -= miktar1;
					System.out.println("Toplam bakiye:" + bakiye);
				break;
				
				case 3:
					System.out.println("Ne kadar yatiracaksiniz");
					int miktar2 = scan.nextInt();

					bakiye += miktar2;
					System.out.println("Toplam bakiye" + bakiye);
				break;

				case 4:
					System.out.println("Sistemden cikiliyor...");

				break;
				
				default:
					System.out.println("Gecersiz islem");
				break;
			}
		}
	}
}
