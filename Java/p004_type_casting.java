
public class p004_type_casting {
  public static void main(String[] args) {
    int myInt = 9;
    double myDouble = myInt; // Automatic casting: int to double

    System.out.println(myInt);
    System.out.println(myDouble);
    
    double myDouble0 = 9.78d;
    int myInt0 = (int) myDouble0; // Explicit casting: double to int

    System.out.println(myDouble0);
    System.out.println(myInt0);
  }
}
