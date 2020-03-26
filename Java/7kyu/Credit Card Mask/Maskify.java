public class Maskify {
    public static String maskify(String str) {
        if(str.length() < 5)
          return str;
        
        StringBuilder mask = new StringBuilder();
        for(int i = 0; i < str.length()-4; i++)
          mask.append("#");
        
        for(int i = str.length()-4; i < str.length(); i++)
          mask.append(str.charAt(i));
          
        return mask.toString();
    }
}