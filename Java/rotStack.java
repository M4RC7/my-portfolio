public class rotStack{
  public static int rot = -1;

  public static class Rot{
    private int[] rotS;
    private int rotC;

    public Rot(){
      rotS = new int[256];
      rotC = -1;
    }

    public void verificaRot(){
      if (rotC < 0){
        System.out.print("Empty");
      }else{
        for (int i = 0; i <= rotC; i++){
          System.out.print(rotS[i]+" ");
        }
      }
      System.out.println();
    }

    public String empilhaRot(){
      rotS[++rotC]= ++rot;
      return ".r"+rot;
    }

    public String mantemRot(){
      return ".r"+rotS[rotC];
    }
    
    public String desempilhaRot(){
      return ".r"+rotS[rotC--];
    }
  }

  public static void main (String[] args){
    Rot aux0 = new Rot();
    aux0.verificaRot();
    System.out.println(aux0.empilhaRot());
    aux0.verificaRot();
    System.out.println(aux0.mantemRot());
    aux0.verificaRot();
    System.out.println(aux0.desempilhaRot());
    aux0.verificaRot();
    System.out.println(aux0.empilhaRot());
    aux0.verificaRot();
  }
}