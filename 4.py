import random
def rannum(x,y):
 for i in range(0,3):
  print(random.randint(x,y),end=" ")
a=int(input("Enter Starting Limit\n"))
b=int(input("Enter End Limit\n"))
print("3 Random Numbers between",a,"and",b,"is :",end=" ")
rannum(a,b)
