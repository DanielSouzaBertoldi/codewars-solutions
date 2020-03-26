import java.util.HashMap;
import java.util.Map;

public class FindOdd {
  public static int findIt(int[] a) {
    HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>();
    
    for(int i = 0; i < a.length; i++) {
      int num = a[i];
      
      if(hash.containsKey(num))
        hash.put(num, hash.get(num)+1);
      else
        hash.put(num, 1);
    }
    
    for(Map.Entry<Integer, Integer> map : hash.entrySet()) {
      if(map.getValue() % 2 == 1)
        return map.getKey();
    }
    
    return 0;
  }
}