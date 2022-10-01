public class p006a_concatenation{
  public static void main(String[] args){
    String firstName = "John";
    String lastName = "Doe";
    System.out.println(firstName + " " + lastName);
    System.out.println(firstName.concat(lastName));
    
    //Addition vs. Concatenation
    int x = 10;
    int y = 20;
    int z = x + y;
    System.out.println(z);
    
    String a = "10";
    String b = "20";
    String c = a + b;
    System.out.println(c);
    
    String d = a + y;
    System.out.println(d);
    
    /*
    Special Characters:
    \' ' Single quote
    \" " Double quote
    \\ \ Backslash
    \n	New Line	
    \r	Carriage Return	
    \t	Tab	
    \b	Backspace	
    \f	Form Feed
    */
  }
}
