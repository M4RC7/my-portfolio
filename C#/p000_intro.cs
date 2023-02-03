using System;
namespace Test {
  class Program {
    static void Main(string[] args) {
      Console.WriteLine("Test C#");
      //Console.ReadKey(); //prevents screen from running and closing quickly when running straight from ".exe"
    }
  }
}
/*
@ How to access datapath: Computer-> Properties-> Advanced Config-> Environment Variables-> Path-> Folder where .Net Framework is installed, usually "C:\Windows\Microsoft.NET\Framework\v4.0.30319"
@ Compile with "csc <filename>". ".cs" extension. Execute by running generated executable.
@ w3schools.com <-don't forget who your true friends are
*/
