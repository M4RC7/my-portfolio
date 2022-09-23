public class p002a_variable_combos{
  public static void main(String[] args){
    int myNum = 5;
    float myFloatNum = 5.99f;
    char myLetter = 'D';
    boolean myBool = true;
    String myText = "Hello";
    System.out.println("Hi "+myText);
    
    //text and variable
    String myName = "Hi and "+myText;
    System.out.println(myName);
    
    //adding variable to variable
    String myName2 = myText+myLetter;
    System.out.println(myName2);
    
    //math operator
    final int myNumFinal = 15;
    System.out.println(myNumFinal+myNum);
    
    //override
    System.out.println(myFloatNum+myNum);
  }
}
