class Solution {
    public static String whoLikesIt(String... names) {
        int size = names.length;
        
        if(size == 0)
          return "no one likes this";
        if(size == 1)
          return names[0] + " likes this";
        if(size == 2)
          return names[0] + " and " + names[1] + " like this";
        if(size == 3)
          return names[0] + ", " + names[1] + " and " + names[2] + " like this";
          
        size-=2;
        return names[0] + ", " + names[1] + " and " + size + " others like this";
    }
}