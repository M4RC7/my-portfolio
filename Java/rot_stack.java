public class rot_stack {
  public static int[][] rot = new int[3][256];
  public static int cont_rot = 0;
  
  public static void verificaRot(int i){
    for (int j = 0; j<rot[i].length; j++){
      if (rot[i][j]<1){
        System.out.println(i+", "+j+": "+rot[i][j]);
        break;
      }
      System.out.println(i+", "+j+": "+rot[i][j]);
    }
  }

  public static String empilhaRot(int i){
    int j;
    for (j = 0; j<rot[i].length; j++){
      if (rot[i][j]<1){
        break;
      }
    }
    rot[i][j]= ++cont_rot;
    return ".r"+cont_rot;
  }

  public static String mantemRot(int i){
    int j;
    for (j = 0; j<rot[i].length; j++){
      if (rot[i][j]<1){
        break;
      }
    }
    return ".r"+rot[i][--j];
  }

  public static String desempilhaRot(int i){
    int j, prov;
    for (j = 0; j<rot[i].length; j++){
      if (rot[i][j]<1){
        break;
      }
    }
    prov= rot[i][--j];
    rot[i][j]= 0;
    return ".r"+prov;
  }
  
  public static void main(String[] args) {
    verificaRot(0);
    //System.out.println(rot[0][0]); //int arrays are inited with 0
    System.out.println(empilhaRot(0));
    verificaRot(0);
    System.out.println(mantemRot(0));
    verificaRot(0);
    System.out.println(desempilhaRot(0));
    verificaRot(0);
    System.out.println(empilhaRot(0));
    verificaRot(0);
    System.out.println(desempilhaRot(0));
    verificaRot(0);
  }
}

