public class p009_ifelse{
  public static void main(String[] args){
    //just if
    if (20 < 18) {
      System.out.println("20 is lower than 18 lol");
    }
    
    //if and else
    int x = 20;
    if (x < 18) {
      System.out.println("Lower than 18");
    } else {
      System.out.println("18 or greater");
    }
    
    //if and else if and else
    if (x < 10) {
      System.out.println("Lower than 10");
    } else if (x < 20) {
      System.out.println("Lower than 20");
    } else {
      System.out.println("20 or greater");
    }
    
    //short hand if and else
    String out = (x < 18) ? "Lower than 18" : "18 or greater";
    System.out.println(out);
  }
}
