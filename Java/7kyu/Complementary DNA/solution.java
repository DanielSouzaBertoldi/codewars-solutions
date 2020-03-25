public class DnaStrand {
  public static String makeComplement(String dna) {
    StringBuilder str = new StringBuilder(dna);
    
    for(int i = 0; i < str.length(); i++) {
      if (str.charAt(i) == 'A') str.setCharAt(i, 'T');
      else if (str.charAt(i) == 'T') str.setCharAt(i, 'A');
      else if (str.charAt(i) == 'C') str.setCharAt(i, 'G');
      else str.setCharAt(i, 'C');
    }

    return str.toString();
  }
}