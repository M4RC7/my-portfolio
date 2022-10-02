name= "better"
name0= """better
   25"""
age= 25
print(f"Hello, {name}. You are {age}.")#a lot more handy than regular formatting
print(F"Hello, {name}. You are {age}.")#also works with capital 'F'
print(f"Check this out: {2*37}.")#evaluation at runtime allows this
print(f"{name.upper()}")#also supports functions
print(f"Check this out: {name}\n{age}.")#'\n' will work
print(f"{name}\t{age}.")#'\t' will work too
print(f"{name}\0\0\0\0{age}.")#'\0' will work too, but not so handy
print(f"{name}    {age}.")
print(f"{name}"f"{age}.")#always make sure to put that 'f'
print(f"{name}""{age}.")
print(f"{name}" \
      f"{age}....")#'\' actually does nothing, unless there's no line break -it's just a little something for those who rather it more organized
print(f"""{name}
   {age}.""")#and that's why you should be careful before using triple quotes to comment -they are actally used to design strings
print(name0)#here's the proof
#The f in f-strings may as well stand for "fast." f-strings are faster than both %-formatting and str.format() exactly for being evaluated at runtime rather than constant values.