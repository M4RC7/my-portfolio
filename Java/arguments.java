/*
Messing around with the built-in Java args
Try running just "java arguments" then
"java arguments <something> <something>"
(as many somethings as you like between spaces)
*/

public class arguments{
  public static void main(String[] args){
    if (args.length>0){
      System.out.println("THESE ARE YOUR ARGUMENTS:");
      for (String arg : args){
        System.out.println(arg);
      }
    } else {
      System.out.println("YOUR ARGUMENT IS INVALID");
    }
  }
}