import java.util.Scanner;

public class IstanbulkartHesaplama {

    public static void main(String[] args) {
        // Ücret bilgileri
        double yolculukUcreti = 9.76;
        double aktarmaUcreti = 4.28;
        double abonelikUcreti = 850.00;
        int abonelikSiniri = 120;

        // Kullanıcıdan girişleri al
        Scanner scanner = new Scanner(System.in);
        System.out.print("Günlük ortalama yolculuk sayısı: ");
        int gunlukYolculuk = scanner.nextInt();
        
        System.out.print("Günlük ortalama aktarma sayısı: ");
        int gunlukAktarma = scanner.nextInt();
        
        // Aylık yolculuk ve aktarma sayısını hesapla
        int aylikYolculuk = gunlukYolculuk * 30;
        int aylikAktarma = gunlukAktarma * 30;

        // Abonesiz maliyeti hesapla
        double abonesizMaliyet = (aylikYolculuk * yolculukUcreti) + (aylikAktarma * aktarmaUcreti);

        // Abonelikli maliyeti hesapla
        double abonelikliMaliyet = abonelikUcreti;
        if (aylikYolculuk > abonelikSiniri) {
            abonelikliMaliyet += (aylikYolculuk - abonelikSiniri) * yolculukUcreti;
        }
        abonelikliMaliyet += aylikAktarma * aktarmaUcreti;

        // Karşılaştırma yap ve sonucu yazdır
        if (abonelikliMaliyet < abonesizMaliyet) {
            System.out.printf("Abonelik almak daha avantajlı: %.2f TL\n", abonelikliMaliyet);
        } else {
            System.out.printf("Abonelik almamak daha avantajlı: %.2f TL\n", abonesizMaliyet);
        }
    }
}
