public class p006_strings.java{
  public static void main(String[] args){
    String txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    System.out.println("The string is: " + txt);
    System.out.println("Its length is: " + txt.length());
    System.out.println(txt.toLowerCase());
    System.out.println(txt.toUpperCase());
    
    /*
    indexOf()-> returns the index (the position) of the
    first occurrence of a specified text in a string
    (including whitespace)
    Position counting starts from zero:
    First position in a string is 0
    Second is 1, third is 2...
    */
    System.out.println(txt.indexOf("G"));
  }
}
