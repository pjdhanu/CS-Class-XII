def bigone(x,y):
 if x%10>y%10:
  return(y)
 else:
  return(x)
a=int(input("Enter a Number\n"))
b=int(input("Enter a Number\n"))
print("The Number with Lowest Value at One's Place is : ",bigone(a,b))
