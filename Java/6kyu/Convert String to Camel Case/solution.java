import java.lang.StringBuilder;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Solution{

  static String toCamelCase(String s){
    StringBuilder str = new StringBuilder();
    Matcher m = Pattern.compile("[-_]([a-z])").matcher(s);

    while(m.find()) {
      m.appendReplacement(str, m.group().toUpperCase());
    }

    m.appendTail(str);
    
    return str.toString().replaceAll("[-_]", "");
  }
}