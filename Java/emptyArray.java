public class Main {
  public static void main(String[] args) {
    char[] plank = new char[4];
    plank[2] = 'h';
    for (int i = 0; i < plank.length; i++) {
      System.out.println(plank[i]);
    }
  }
}
/*
 * Java, when you request new type for an array, initializes positions in array with a default empty value to prevent trash printing
 */