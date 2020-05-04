def series(x,y):
 d=int((y-x)/3)
 for i in range(0,4):
  print(x+(i*d),end=" ")
a=int(input("Enter Starting Number\n"))
b=int(input("Enter End Number\n"))
print("Series is : ",end="")
series(a,b)
