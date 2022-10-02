public class p013_break_continue {
  public static void main(String[] args) {
    //break bails the execution out of the loop
    for (int i = 0; i < 10; i++) {
      if (i == 4) {
        break;
      }
      System.out.println(i);
    }
    //continue skips current iteration of the loop
    for (int i = 0; i < 10; i++) {
      if (i == 4) {
        continue;
      }
      System.out.println(i);
    }
  }
}
