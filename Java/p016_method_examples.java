public class p016_method_examples {
  static void checkNum(int x) {
    if (x < 18) {
      System.out.println("Below 20");
    } else {
      System.out.println("20 or greater");
    }
  }
  
  static int add(int x, int y) {
    return x + y;
  }

  public static void main(String[] args) {
    int a = add(17, 3);
    System.out.println(a);
    checkNum(a);
  }
}
