import os
file= input("File name? ")

if (file[-3:]==".cs"):
#  print(file[-3:])
#  print("This is a C# Source Code.")
  execu= file[:-3]+".exe"
#  print(execu)
  if(os.path.isfile(execu)):
    os.remove(execu)
  os.system("csc "+file)
  if(os.path.isfile(execu)):
    os.system(execu)
    os.remove(execu)
  else:
    print("Something went wrong.")

#elif (file[-5:]==".java"):
#  print(file[-5:])
#  print("This is a Java Source Code.")
#  execu= file[:-5]
#  print(execu)
#  if(os.path.isfile(execu)):
#    os.remove(execu)
#  os.system("javac "+file)
#  if(os.path.isfile(execu)):
#    os.system("java "+execu)
#    os.remove(execu)
#  else:
#    print("Something went wrong.")
  
else:
  print("This is another file type.")