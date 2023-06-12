public class str_vect {
  public static void main(String[] args) {
    String[] auxExp = new String [255];
    auxExp[0] = "Hello World!";
    auxExp[1] = "Hkllo World!";
    auxExp[0] = auxExp[1]+auxExp[0];
    for (int i = 0; i<auxExp.length; i++){
      if (auxExp[i]==null){
        break;
      }else{
        System.out.println(i+": "+auxExp[i]);
      }
    }
  }
}
