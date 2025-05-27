import java.util.*;

public class projedeneme {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        int m = scan.nextInt();

        int RaporSayisi = 0;

        for (int i = 0; i < n; i++) {
            if(GuvenliRapor(scan, m)){
                RaporSayisi++;
            }
        }

        System.out.println(RaporSayisi);
    }

    private static boolean GuvenliRapor(Scanner scan, int m){
        boolean kontrol = true;
        boolean artan = true;
        boolean azalan = true;
        
        int ilkdeger = scan.nextInt();

        for (int j = 1; j < m; j++) {
            int ikincideger = scan.nextInt(); 
            int fark = ikincideger - ilkdeger;
            
            if(Math.abs(fark)>3){
                kontrol=false;
            }
            
            if(fark<0){
                artan=false;
            }
            
            if(fark>0){
                azalan=false;
            }
            ilkdeger=ikincideger;
        }
        if(!(artan ||  azalan)){
            kontrol=false;
        }
        return kontrol;
    }
}

