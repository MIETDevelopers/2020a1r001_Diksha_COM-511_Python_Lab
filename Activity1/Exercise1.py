#1. Python program to calculate length of a String without using len() function
string=input("Enter string ")
length = 0
for i in string:
    length=length+1
print("length of the string is",length)    


#2. Python function to sum all the numbers in a list example
numbers=[2,4,6,8]
total=sum(numbers)
print("sum of all the numbers is:",total)     


#3. Finding largest number in a list using sort() method
a=[34,56,78,99,23]
a.sort()
print("largest number in a list is",a[-1])


#4. Finding largest number in a list using max() method
a=[1,5,3,9,67]
x=max(a)
print("largest number in a list",x)

#5. Write a Python program to print the even numbers from a given list 
a=[1,2,3,4,5,6,7,10,44,55,33,100]
for n in a:
   if n%2 == 0:
     print(n)