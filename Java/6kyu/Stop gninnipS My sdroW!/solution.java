import java.lang.StringBuilder;
import java.util.Arrays;
import java.util.ArrayList;

public class SpinWords {

  public String spinWords(String sentence) {
    String[] words = sentence.split(" ");
    ArrayList a = new ArrayList<>();
    for(String word : words) {
      if(word.length() > 4) {
        StringBuilder str = new StringBuilder(word);
        word = str.reverse().toString();
      }
      a.add(word);
    }
    return String.join(" ", a);
  }
}