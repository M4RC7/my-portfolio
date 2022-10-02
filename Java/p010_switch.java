public class p010_switch {
  public static void main(String[] args) {
    int day = 4;
    switch (day) {
      defualt:
        System.out.println("No case");
        break; //without the break, next case will be executed
      case 1:
        System.out.println("Case 1");
        break;
      case 2:
        System.out.println("Case 2");
        break;
      case 3:
        System.out.println("Case 3");
        break;
      case 4:
        System.out.println("Case 4");
        break;
      case 5:
        System.out.println("Case 5");
        break;
      case 6:
        System.out.println("Case 6");
        break;
      case 7:
        System.out.println("Sunda7");
        break; //last case doesn't need break
    }
  }
}
