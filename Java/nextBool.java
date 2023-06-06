import java.util.InputMismatchException;
import java.util.Scanner; // import the Scanner class 

class nextBool {
  public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);
    boolean userName = false;
    
    // Enter username and press Enter
    System.out.print("Enter a string: ");
    try{
      userName = myObj.nextBoolean(); //Exception is thrown here
    }catch(InputMismatchException e){
      System.out.println("Not a boolean.");
    }

    System.out.println("Logical value: " + userName);   
  }
}
