import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        int m = scan.nextInt();

        if (n < 1 || n > 1000 || m < 1 || m > 1000) {
            System.out.println("n ve m değerleri 1 ile 1000 arasinda olmalidir.");
            return;
        }

        int RaporSayisi = 0;

        scan.nextLine();

        for (int i = 0; i < n; i++) {
            String Satir = scan.nextLine();
            if (GuvenliRapor(Satir, m)) {
                RaporSayisi++;
            }
        }

        System.out.println(RaporSayisi);
    }

    private static boolean GuvenliRapor(String Satir, int m) {
        String[] values = Satir.split(" ");
        if (values.length != m) {
            return false; 
        }

        boolean kontrol = true;
        boolean ArtanSayilar = true;
        boolean AzalanSayilar = true;

        int ilkdeger = Integer.parseInt(values[0]);
        if (ilkdeger < 0 || ilkdeger > 9) {
            return false;
        }

        for (int j = 1; j < m; j++) {
            int ikincideger = Integer.parseInt(values[j]);
            if (ikincideger < 0 || ikincideger > 9) {
                return false;
            }
            int fark = ikincideger - ilkdeger;

            if (Math.abs(fark) > 3) {
                kontrol = false;
            }

            if (fark < 0) {
                ArtanSayilar = false;
            }

            if (fark > 0) {
                AzalanSayilar = false;
            }
            ilkdeger = ikincideger;
        }

        if (!(ArtanSayilar || AzalanSayilar)) {
            kontrol = false;
        }

        return kontrol;
    }
}