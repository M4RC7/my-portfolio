import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.lang.ProcessBuilder;

public class buildLink{
  public static void main (String[] args){
    try{
      ProcessBuilder processBuilder = new ProcessBuilder();

      //monta o pseudo-programa em assembly de NASM
      processBuilder.command("nasm",args[0],"-g","-w-zeroing","-f","elf64","-o",args[0]+".o");
      Process process = processBuilder.start();

      //linkedita o pseudo-programa montado
      processBuilder.command("ld",args[0]+".o","-o",args[0]+".exe");
      process = processBuilder.start();

      //executa o pseudo-programa linkeditado e escreve a saida na JVM
      processBuilder.command("./"+args[0]+".exe");
      process = processBuilder.start();

      BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));

      String line;
      while ((line = reader.readLine()) != null) {
        System.out.println(line);
      }

      int exitCode = process.waitFor();
      System.out.println("\nExited with error code : " + exitCode);

      //tratamento de eventuais erros de execucao, javac cobra isso
    }catch(ArrayIndexOutOfBoundsException x){
      System.out.println("I need a valid file name.");
      x.printStackTrace();
    }catch(IOException ex){
      System.out.println("I/O Error.");
      ex.printStackTrace();
    }catch(InterruptedException ax){
      System.out.println("Execution interrupted.");
      ax.printStackTrace();
    }
  }
}
