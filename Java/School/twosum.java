
class Solution {
    public static void main(String[] args) {
        String mail = "talha@hotmail.com";

        int atindex = mail.indexOf('@');       // '@' sembolünün indeksini bulur.
        int dotindex = mail.indexOf('.');      // İlk '.' sembolünün indeksini bulur.
        int dotsindex = mail.lastIndexOf('.'); // Son '.' sembolünün indeksini bulur.

        // Kullanıcı adı kısmı
        String username = mail.substring(0,atindex); // "talha"

        // Domain kısmı (örneğin, "hotmail")
        String domain = mail.substring(atindex + 1, dotindex);
        
        // Üst düzey domain kısmı (örneğin, "com")
        String topLevelDomain = mail.substring(dotsindex+1);

        // Çıktıları yazdır
        System.out.println("Kullanıcı Adı: " + username);
        System.out.println("Domain: " + domain);
        System.out.println("Üst Düzey Domain: " + topLevelDomain);
    }
}
