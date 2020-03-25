import java.lang.Math;

public class NthSeries {
  public static String seriesSum(int n) {
    int base = 1;
    double sum = 0;
    
    for(int i = 0; i < n; i++) {
      sum = sum + 1.0/base;
      base += 3;
    }

    return String.format("%.2f", sum);
  }
}