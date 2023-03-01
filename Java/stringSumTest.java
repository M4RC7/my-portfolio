public class stringSumTest {
  public static void main (String[] args){
    String test= "test";
    int score= 0;
    for (int j = 0; j < test.length(); j++){
      int k= test.charAt(j);
      System.out.println(k);
      score += test.charAt(j);
    }
    System.out.println(score);
  }
}