public class p011_while {
  public static void main(String[] args) {
    //while condition is true
    int i = 0;
    while (i < 3) {
      System.out.println(i++);
    }
    
    //do it once, then while condition is true
    int i = 0;
    do {
      System.out.println(i++);
    }
    while (i < 3);
    //always make sure the variable used in the condition increases/decreases towards making the condition false, otherwise you'll never leave the loop!
    /*
    while(true){
      System.out.println("Press Ctrl+C to exit.");
    }
    */
  }
}
