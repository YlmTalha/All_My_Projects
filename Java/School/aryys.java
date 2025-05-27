import java.util.ArrayList;
public class aryys {
    public static void main(String[]args){
        ArrayList<String> groups = new ArrayList<String>();

        int[] arr={10,20,30,40,50};

        groups.add("merhaba");
        groups.add("merhaba1");
        groups.add("merhaba2");
        groups.add("merhaba3");

        

        

        for(String s:groups){
            System.out.println("Eleman: " + s);
        }

        for(int i : arr){
            System.out.println("ELeman: " + i);
        }



    }
}
