public class forSomething{
  public static void main (String[] args){
    // for(int x=0, for(;;); x<10; x++){
    // for(int x=0, System.out.println("I'm in a for"); x<10; x++){
    // for(int x=0, for(;;), System.out.println("I'm in a for"); x<10; x++){
    // for(int x=0; x<10; x++){
    for(int x=0, y=0; x<10; x++, y=y+3){
      // System.out.println(x);
      System.out.println(x + "+" + y + "=" + (x + y));
    }
  }
}