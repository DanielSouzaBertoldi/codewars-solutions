import java.util.Arrays;

public class isogram {
    public static boolean  isIsogram(String str) {
        str = str.toLowerCase();
        
        char[] letters = str.toCharArray();
        Arrays.sort(letters);
        for(int i = 0; i < str.length()-1; i++) {
          if(letters[i] == letters[i+1])
            return false;
        }
        return true;
    } 
}