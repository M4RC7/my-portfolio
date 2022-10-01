public class p005_operators{
  public static void main(String[] args){
    int sum1 = 100 + 50;
    int sum2 = sum1 + 250;
    int sum3 = sum2 + sum2;
    System.out.println(sum1);
    System.out.println(sum2);
    System.out.println(sum3);
    
    //Assignment
    sum3+= sum2;
    System.out.println(sum3);
    System.out.println(sum1 > sum3);
    
    //Extra: Increment/Decrement
    int x = 1;
    //Increments/Decrements after printing
    System.out.println(x++);
    System.out.println(x--);
    System.out.println(x);
    //Increments/Decrements before printing
    System.out.println(++x);
    System.out.println(--x);
    
    /*
    List of operators:
    +	Addition
    -	Subtraction
    *	Multiplication
    /	Division
    %	Modulus:	Returns the division remainder
    ++ Increment	Increases the value of a variable by 1
    -- Decrement	Decreases the value of a variable by 1
    &	AND operation
    |	OR operation
    ^	XOR operation
    >> Shift Right
    << Shift Left
    == Equal to-> x == y	
    != Not equal-> x != y	
    > Greater than-> x > y	
    <	Less than-> x < y	
    >= Greater than or equal to-> x >= y	
    <= Less than or equal to-> x <= y
    && Logical and: Returns true if both statements are true-> x < 5 &&  x < 10	
    || Logical or: Returns true if one of the statements is true-> x < 5 || x < 4	
    ! Logical not: Reverse the result, returns false if the result is true-> !(x < 5 && x < 10)
    */
  }
}
