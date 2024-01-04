#mylist = [i for i in range(10) if i % 2 == 0] ###also works
mylist = [i+1 for i in range(10)]
#my_new_list = [el for el in mylist if el % 2 == 0] ###also works
my_new_list = [el if el % 2 == 0 else 15 for el in mylist]
print(mylist)
print(my_new_list)