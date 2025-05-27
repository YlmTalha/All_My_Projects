import java.util.Scanner;
public class ters {
    private static Scanner scanner;
    public static void main(String[] args) {
        scanner = new Scanner(System.in);
        
        System.out.println("4 basamakli sayi giriniz: " );
        int sayi = scanner.nextInt();
        
        int birlerbas = (sayi%10);
        int onlarbas =  (sayi/10) %10; 
        int yuzlerbas= (sayi/100)%10;
        int binlerbas= (sayi/1000);

        int terssayi = (birlerbas*1000) + (yuzlerbas*10) + (onlarbas*100)+binlerbas;
        System.err.println(terssayi);
    }
}
