public class p002_variables{
  public static void main(String[] args){
    int myNum = 5;
    float myFloatNum = 5.99f;
    char myLetter = 'D';
    boolean myBool = true;
    String myText = "Hello";
    System.out.println(myNum);
    System.out.println(myFloatNum);
    System.out.println(myLetter);
    System.out.println(myBool);
    System.out.println(myText);
    
    //changing a value
    myNum = 20;
    System.out.println(myNum);
    
    //final variables cannot have their values changed
    final int myNumFinal = 15;
    //myNumFinal = 20; //yields error
    System.out.println(myNumFinal);
  }
}
