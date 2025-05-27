import java.util.*;

public class StudentID_Assignment1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Verilerin boyutlarını oku
        int n = scanner.nextInt(); // Rapor sayısı
        int m = scanner.nextInt(); // Her bir rapordaki sayıların uzunluğu

        int guvenliRaporSayisi = 0;

        // Her bir raporu işle
        for (int i = 0; i < n; i++) {
            if (isReportSafe(scanner, m)) {
                guvenliRaporSayisi++;
            }
        }

        // Güvenli raporların sayısını yazdır
        System.out.println(guvenliRaporSayisi);
    }

    private static boolean isReportSafe(Scanner scanner, int m) {
        boolean guvenli = true;
        boolean artan = true;
        boolean azalan = true;

        int onceki = scanner.nextInt();

        for (int j = 1; j < m; j++) {
            int simdiki = scanner.nextInt();
            int fark = simdiki - onceki;

            if (Math.abs(fark) > 3) {
                guvenli = false; // Fark izin verilen aralığı aşıyor
            }

            if (fark < 0) {
                artan = false; // Tamamen artan değil
            }

            if (fark > 0) {
                azalan = false; // Tamamen azalan değil
            }

            onceki = simdiki;
        }

        if (!(artan || azalan)) {
            guvenli = false;
        }

        return guvenli;
    }
}
