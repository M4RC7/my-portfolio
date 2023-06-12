import java.io.BufferedWriter;
import java.io.FileWriter;   // Import the FileWriter class
import java.io.IOException;  // Import the IOException class to handle errors

public class WriteToFile {
  public static void main(String[] args) throws IOException {
    try {
      FileWriter myWriter = new FileWriter("filename.txt");
      BufferedWriter bw = new BufferedWriter(myWriter);
      bw.write("Files in Java might be tricky, but it is fun enough!\n");
      bw.write("Files in Java might be tricky, but it is fun once you get the hang!");
      bw.close();
      myWriter.close();
      System.out.println("Successfully wrote to the file.");
    } catch (IOException e) {
      System.out.println("An error occurred.");
      e.printStackTrace();
    }
  }
}
/* public class WriteToFile {
  public static void main(String[] args) throws IOException {
    FileWriter myWriter = new FileWriter("filename.txt");
    BufferedWriter bw = new BufferedWriter(myWriter);
    bw.write("Files in Java might be tricky, but it is fun enough!\n");
    bw.write("Files in Java might be tricky, but it is fun once you get the hang!");
    bw.close();
    myWriter.close();
    System.out.println("Successfully wrote to the file.");
  }
} */