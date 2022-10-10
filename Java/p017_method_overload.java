public class p017_method_overload {
  static int add(int x, int y) {
    return x + y;
  }
  
  static double add(double x, double y) {
    return x + y;
  }
  
  public static void main(String[] args) {
    int myNum1 = add(9, 6);
    double myNum2 = add(5.6, 7.94);
    System.out.println("int: " + myNum1);
    System.out.println("double: " + myNum2);
  }
}
