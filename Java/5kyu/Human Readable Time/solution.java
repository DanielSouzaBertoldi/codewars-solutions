import java.lang.Math;

public class HumanReadableTime {
  public static String makeReadable(int seconds) {
    int integer;
    double hours, minutes, sec;
    
    hours = seconds/3600.0;
    integer = seconds/3600;
    minutes = (hours - integer) * 60;
    integer = Integer.parseInt(String.valueOf(minutes).split("\\.")[0]);
    if(integer == 60)
      hours++;
    sec = Math.round((minutes - integer) * 60);
    if((int) sec == 60)
      minutes++;

    return String.format("%02d", (int) hours)+":" + String.format("%02d", (int) minutes)+":" + String.format("%02d", (int) sec);
  }
}