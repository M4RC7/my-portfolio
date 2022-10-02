size= 8
links= [""]
links*= size

def write():
  try:
    p= int(input("Write in position?"))
  except ValueError:
    p= -1
  if p<0 or p>=size:
    print("Not a valid position")
  else:
    name= input("Content?")
    links[p]= name
    print("\""+name+"\" was written in position "+str(p))

def erase():
  try:
    p= int(input("Erase from position?"))
  except ValueError:
    p= -1
  if p<0 or p>=size:
    print("Not a valid position")
  else:
    links[p]= ""
    print("Link in position "+str(p)+" erased.")

def load():
  try:
    f= open("links.txt", "r")
    i= 0
    while i<size:
      links[i]= f.readline().strip() #"the end-of-line \n read by "readline()" is also being included -it's removed with "strip()""
      i+=1
   #f.close()
    print("Content loaded from file links.txt")
  except FileNotFoundError:
    open("links.txt", "x")
    print("File links.txt is missing -just created")

def save():
  f= open("links.txt", "w")
#  i= 0
  for x in links:
    f.write(x)
    f.write("\n")
#    i+=1
  f.close()
  print("Content saved in file links.txt")

def show():
  i= 0
  for x in links:
    print(str(i)+": "+x)
    i+=1

def option(opt):
  if opt=="0":
    print("Terminating execution")
  elif opt=="1":
    write()
  elif opt=="2":
    erase()
  elif opt=="3":
    show()
  elif opt=="4":
    load()
  elif opt=="5":
    save()
  else:
    print("Invalid option")

opt0= ""
while opt0!="0":
  opt0= input("What next?")
  option(opt0)