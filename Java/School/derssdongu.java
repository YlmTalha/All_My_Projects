import java.util.Scanner;

public class derssdongu {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
    
        int n = 1;
        // Bir String dizisi oluşturuyoruz
        String[] isimler = new String[n];
        int i=0;
        isimler[i] = scan.nextLine();

            int p =0;

            while( p >= 0 || p ==3 ){
                System.out.print(isimler[0].charAt(p));
                p++;
            }
            
        
        
    }
}