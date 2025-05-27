
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String start = scan.next();
        String target = scan.next();
        
        boolean result = canChange(start, target);
        
    }
    public static boolean canChange(String start, String target) {
        // Uzunluklar eşit mi kontrol ediliyor
        int i1 = start.length();
        int i2 = target.length();
        
        // Eğer karakter setleri eşleşmiyorsa dönüşüm mümkün değil
        if (!start.replace("_", "").equals(target.replace("_", ""))) {
            return false;
        }
        
        // 'L' ve 'R' karakterlerinin ilk ve son görünümlerini bulma
        int l1 = start.indexOf("L");
        int r1 = start.indexOf("R");
        int r11 = start.lastIndexOf("R");
        int l11 = start.lastIndexOf("L");

        int l2 = target.indexOf("L");
        int r2 = target.indexOf("R");
        int r22 = target.lastIndexOf("R");
        int l22 = target.lastIndexOf("L");
        
        // Eğer 'L' ve 'R' yoksa dönüşüm direkt mümkün
        if (l1 == -1 && r1 == -1) {
            return true;
        }
        
        // Hareket kısıtlamalarını kontrol et
        if (l11 > r11 || l22 > l11 || l1 < l2 || r1 > r2 || l1 > r2 || r1 < l2) {
            return false;
        }

        return true;
        System.out.println(return);
    }
}
