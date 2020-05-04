import random
def randnum(n):
 low=10**(n-1)
 high=10**n
 return random.randint(low,high)
a=int(input("Enter Length of the Random Number\n"))
print("Random Number of Length",a,"is",randnum(a))
