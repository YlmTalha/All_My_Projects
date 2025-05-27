import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
    
        String input = scan.nextLine();
        char[] binaryArray = new char[input.length()];
        int binaryLength = 0;

        for (int currentIndex = 0; currentIndex < input.length();) {
            if (input.startsWith("ZERO", currentIndex)) {
                binaryArray[binaryLength++] = '0';
                currentIndex += 4;
            } else if (input.startsWith("ONE", currentIndex)) {
                binaryArray[binaryLength++] = '1';
                currentIndex += 3;
            } else {
                currentIndex++;
            }
        }
        

        char[] asciiArray = new char[binaryLength / 8];
        int asciiIndex = 0;

        for (int i = 0; i < binaryLength; i += 8 ) {
            if(i+8 <= binaryLength){
                StringBuilder byteStringBuilder = new StringBuilder();
                for (int j = 0; j < 8; j++) {
                    byteStringBuilder.append(binaryArray[i + j]);
                }
                int decimalValue = Integer.parseInt(byteStringBuilder.toString(), 2);
                asciiArray[asciiIndex++] = (char) decimalValue;
            }
        }
        
        String asciiMessage = new String(asciiArray);

        String finalMessage = asciiMessage
            .replace('4', 'A')
            .replace('@', 'A')
            .replace('8', 'B')
            .replace('3', 'E')
            .replace('6', 'G')
            .replace('9', 'G')
            .replace('1', 'I')
            .replace('!', 'I')
            .replace('0', 'O')
            .replace('2', 'Z')
            .replace('7', 'Z');

        System.out.println(finalMessage);
    }
}
