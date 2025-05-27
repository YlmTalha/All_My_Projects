public class Stringmetod {
    public static void main(String[] args) {
        String s1="Mustafa";
        String s3="Mustafa";
        String s2=new String("Mustafa");

        System.out.println(s1.length());

        System.out.println(s2.charAt(0));

        System.out.println(s2.startsWith("Mu"));
        System.out.println(s2.endsWith("an")); 


        if(s1.equals(s3)){
            System.out.println("Eşit");
        }




    }
}
