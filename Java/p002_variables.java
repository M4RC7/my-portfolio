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
    
    /*
    All variables must be identified with unique names called identifiers.
    Identifiers can be short names (like x and y) or more descriptive names (age, sum, totalVolume).
    It is recommended to use descriptive names in order to create understandable and maintainable code:
    -----
    // Good
    int minutesPerHour = 60;

    // OK, but not so easy to understand what m actually is
    int m = 60;
    ------
    The general rules for naming variables are:
    Names can contain letters, digits, underscores, and dollar signs;
    Must begin with a letter;
    Should start with a lowercase letter and it cannot contain whitespace;
    Can also begin with $ and _ (but we will not use it in this tutorial);
    Are case sensitive ("myVar" and "myvar" are different variables);
    Reserved words, such as int or boolean, cannot be used as names.
    */
  }
}
