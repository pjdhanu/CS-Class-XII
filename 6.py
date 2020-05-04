def nthroot(x,n):
 return x**(1/n)
a=int(input("Enter Main Number\n"))
b=int(input("Enter Root Number\n"))
print("Square Root of",a,"is : ",a**(1/2))
print(b,"th Root of",a,"is : ",nthroot(a,b))
