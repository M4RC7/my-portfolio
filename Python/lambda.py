#A lambda function is a small anonymous function which can take any number of arguments, but can only have one expression.
x = lambda a : a + 10
print(x(5))
x = lambda a, b : a * b
print(x(5, 6))
x = lambda a, b, c : a*2 + (b-4)/c
print(x(1, 2, 5))
#Why Use Lambda Functions? The power of lambda is better shown when you use them as an anonymous function inside another function. Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def myfunc(n):
  return lambda a : a * n
#Use that function definition to make a function that always doubles the number you send in:
mydoubler = myfunc(2)
#Or, use the same function definition to make a function that always triples the number you send in:
mytripler = myfunc(3)
#Or, use the same function definition to make both functions, in the same program:
print(mydoubler(11))
print(mytripler(11))