import math as M
a=int(input("enter a no a is:"))
b=int(input("enter a no b is:"))
c=int(input("enter a no c is:"))
s=(a+b+c)/2
ar=(s*(s-a)*(s-b)*(s-c))/2
area=M.sqrt(ar)
print("area of triangle is:",area)