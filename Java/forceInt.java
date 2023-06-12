public class forceInt{

  public static void forceInt(int val){
    if (val>0){
      forceInt(val / 10);
      System.out.print(val % 10);
    } else {
      System.out.print("Forced integer: ");
    }
  }

  public static void main (String[] args){
    int x= 257496;
    System.out.println("Regular integer: "+x);
    forceInt(x);
  }
  
}