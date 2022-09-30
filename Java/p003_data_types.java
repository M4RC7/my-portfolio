public class p003_data_types {
  public static void main(String[] args) {
    //byte: 1 byte, stores whole numbers from -128 to 127
    byte myByte = 128;
    System.out.println(myByte);  
    
    //short: 2 bytes, stores whole numbers from -32,768 to 32,767
    short myShort = 5000;
    System.out.println(myShort);
    
    //long: 8 bytes, stores whole numbers from -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
    long myLong = 15000000000L; //notice the 'l' at the end of the number
    System.out.println(myLong);
    
    //double: 8 bytes, stores fractional numbers. Sufficient for storing 15 decimal digits
    double myDouble = 12.34d; //the 'd' at the end of the number is not required for double
    System.out.println(myDouble);
    
    //A floating point number can also be a scientific number with an "e" to indicate the power of 10:
    float f1 = 35e3f;
    double d1 = 12E4d;
    System.out.println(f1);
    System.out.println(d1);
    
    /*
    Non-primitive data types are called reference types because they refer to objects.
    The main difference between primitive and non-primitive data types are:
    Primitive types are predefined (already defined) in Java. Non-primitive types are created by the programmer and is not defined by Java (except for String).
    Non-primitive types can be used to call methods to perform certain operations, while primitive types cannot.
    A primitive type has always a value, while non-primitive types can be null.
    A primitive type starts with a lowercase letter, while non-primitive types starts with an uppercase letter.
    The size of a primitive type depends on the data type, while non-primitive types have all the same size.
    Examples of non-primitive types are Strings, Arrays, Classes, Interface, etc.
    */
  }
}
