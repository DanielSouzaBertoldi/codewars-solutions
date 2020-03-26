import java.util.Map;
import java.util.LinkedHashMap;
import java.lang.StringBuilder;

public class TimeFormatter {
    
    public static String formatDuration(int seconds) {
      System.out.println(seconds);
      LinkedHashMap<String, Integer> results = new LinkedHashMap<String, Integer>();
      String replacement = "";
      StringBuilder timeResult = new StringBuilder();
  
      Map<String, Integer> times = Map.of(
        "years", 365 * 24 * 60 * 60,
        "days", 24 * 60 * 60,
        "hours", 60* 60,
        "minutes", 60,
        "seconds", 1
      );    
  
      if(seconds == 0)
        return "now";
  
      results.put("year", seconds / times.get("years"));
      results.put("day", (seconds - times.get("years")*results.get("year"))/times.get("days"));
      results.put("hour", (seconds - times.get("years")*results.get("year") - times.get("days")*results.get("day"))/times.get("hours"));
      results.put("minute", (seconds - times.get("years")*results.get("year") - times.get("days")*results.get("day") - times.get("hours")*results.get("hour")) / times.get("minutes"));
      results.put("second", seconds - times.get("years")*results.get("year") - times.get("days")*results.get("day") - times.get("hours")*results.get("hour") - times.get("minutes")*results.get("minute"));
  
      // Removing times with value 0
      results.values().removeIf(f -> f == 0);
  
      // Checks if the date should be plural
      results.forEach((k, v) -> {
        if(v > 1)
          k += "s";
        timeResult.append(v + " " + k + ", ");
      });
  
      // Replaces the two last ', ' ocurrences with '' and ' and ', respectively
      for(int i = 0; i < 2; i++){
        int lastOcurrence = timeResult.lastIndexOf(", ");
  
        if(lastOcurrence != -1) {
          if(i != 0)
            replacement = " and ";
  
          timeResult.replace(lastOcurrence, lastOcurrence+2, replacement);
        }
      }
  
      return timeResult.toString();
    }
}