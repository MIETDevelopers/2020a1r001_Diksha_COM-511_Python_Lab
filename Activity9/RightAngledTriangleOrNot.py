# Python program to find whether the triangle is right angled or not
# Also find it's area 

import math

a=int(input("Enter side length 1 = "))
b=int(input("Enter side length 2 = "))
c=int(input("Enter side length 3 = "))

if (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b) :
    print("It is a right angled triangle")
else:
    print("Not a right angled triangle")

s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area is = ", area)



