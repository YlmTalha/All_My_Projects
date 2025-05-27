import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int n = scan.nextInt();
        scan.nextLine();

        if (n < 1 || n > 200000) {
            return;
        }

        String bumpers = scan.nextLine();

        if (bumpers.length() != n) {
            return;
        }

        for (int i = 0; i < bumpers.length(); i++) {
            char index = bumpers.charAt(i);
            if (index != '<' && index != '>') {
                return;
            }
        }

        int leftFallCount = 0;
        int rightFallCount = 0;

        for (int i = 0; i < n; i++) {
            if (bumpers.charAt(i) == '>') {
                break;
            }
            leftFallCount++;
        }

        for (int i = n - 1; i >= 0; i--) {
            if (bumpers.charAt(i) == '<') {
                break;
            }
            rightFallCount++;
        }

        System.out.println(leftFallCount + rightFallCount);

        scan.close();
    }
}