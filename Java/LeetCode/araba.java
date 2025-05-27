import java.util.*;
public class araba {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
    
            int[] arr;
            arr = new int[]{1, 5, 10};

            int b = arr.length;
            for (int i = 0; i < b; i++) {

                for (int j = 0; j <b; j++) {
                    if (arr[i] == 2 * arr[j]) {
                        System.err.println(1); 
                    }
                
                }
                
            }
            System.err.println(0);
    }
}
