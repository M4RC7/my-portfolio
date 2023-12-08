namespace WandererGrounds {
  class Wanderer {
    private int pos_x, pos_y, beep;
    private int[,] grid;

    public Wanderer(int height, int width) {
      pos_x = pos_y = beep = 0;
      grid = new int[height,width];
    }

    public void Up(){
      if (pos_y > 0){
        pos_y--;
        System.Console.WriteLine("Moved to {"+pos_x+", "+pos_y+"}.");
      } else {
        System.Console.WriteLine("Can't move up!");
      }
    }
    public void Down(){
      if (pos_y < grid.GetLength(0)-1){
        pos_y++;
        System.Console.WriteLine("Moved to {"+pos_x+", "+pos_y+"}.");
      } else {
        System.Console.WriteLine("Can't move down!");
      }
    }
    public void Left(){
      if (pos_x > 0){
        pos_x--;
        System.Console.WriteLine("Moved to {"+pos_x+", "+pos_y+"}.");
      } else {
        System.Console.WriteLine("Can't move left!");
      }
    }
    public void Right(){
      if (pos_x < grid.GetLength(1)-1){
        pos_x++;
        System.Console.WriteLine("Moved to {"+pos_x+", "+pos_y+"}.");
      } else {
        System.Console.WriteLine("Can't move right!");
      }
    }

    public void PlaceBeep(int i, int j){
      grid[i,j]++;
    }

    public void PickBeep(){
      if (grid[pos_y, pos_x]>0){
        beep++;
        grid[pos_y, pos_x]--;
        System.Console.WriteLine("Beep picked. Now it has "+beep+" beeps.");
      } else {
        System.Console.WriteLine("No beep to pick!");
      }
    }
    public void DropBeep(){
      if (beep>0){
        beep--;
        grid[pos_y, pos_x]++;
        System.Console.WriteLine("Beep dropped. Now it has "+beep+" beeps.");
      } else {
        System.Console.WriteLine("No beep to drop!");
      }
    }

    public void ShowGrid(){
      for (int i = 0; i < grid.GetLength(0); i++){
        for (int j = 0; j < grid.GetLength(1); j++){
          if (i == pos_y && j == pos_x){
            System.Console.Write("["+grid[i,j]+"]");
          } else{
            System.Console.Write(" "+grid[i,j]+" ");
          }
        }
        System.Console.WriteLine();
      }
      //the following prints in stack, can't pretty print it
      /* foreach (int i in grid){
        System.Console.WriteLine(i);
      } */
    }

    public override string ToString() {
      return base.ToString() + " {\n"
           + "  position: {" + pos_x.ToString() + ", " + pos_y.ToString() + "}\n"
           + "  beep: " + beep.ToString() + "\n"
           + "}";
    }
  }

  class Test {
    static void Main(string[] args) {
      Wanderer wanderer = new Wanderer(2,5);
      wanderer.PlaceBeep(1,1);
      wanderer.Down();
      wanderer.Right();
      wanderer.PickBeep();
      wanderer.Left();
      wanderer.DropBeep();
      wanderer.DropBeep();
      wanderer.ShowGrid();
      System.Console.WriteLine(wanderer);
    }
  }
}