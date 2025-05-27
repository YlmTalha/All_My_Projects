import java.util.Scanner;
public class diskriminant{
    private static Scanner scanner;
    public static void main(String[] args) {
       scanner = new Scanner(System.in);
       System.out.println("a sayisini giriniz :");
       double a = scanner.nextInt();
       System.out.println("b sayisini giriniz :");
       double b = scanner.nextInt();
       System.out.println("c sayisini giriniz :");
       double c = scanner.nextInt();
      

       System.out.println("girdiğiniz sayilar :" + a + " " + b + " " + c );

        double dskr = b*b-4*a*c;    

        if(dskr > 0){
            double x1 = (-b + Math.sqrt(dskr))/(2*a);
            double x2 = (-b - Math.sqrt(dskr))/(2*a); 
            System.out.println("2 farkli kok vardir x1 : " + x1);
            System.out.println("2 farkli kok vardir x2 : " + x2);
        }

        else if (dskr == 0){

            double x = -b/(2*a);
            System.out.println("çakışık kök vardir x : " + x);
        }
        else {
            System.out.println("Gerçek kök yok, karmaşık kökler mevcut.");
        }


    }
}