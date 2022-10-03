public class p014_array {
  public static void main(String[] args) {
    //arrays of object/value
    String[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
    System.out.println(cars[0]);
    cars[0] = "Opel";
    System.out.println(cars[0]);
    System.out.println(cars.length);
    
    //multidimension array
    int[][] myNumbers = { {1, 2, 3, 4}, {5, 6, 7} };
    for (int i = 0; i < myNumbers.length; ++i) {
      for(int j = 0; j < myNumbers[i].length; ++j) {
        System.out.println(myNumbers[i][j]);
      }
    }
  }
}
