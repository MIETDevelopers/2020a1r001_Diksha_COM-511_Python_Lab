# Python programs to find the largest of the three numbers

# METHOD 1 (SIMPLE)
def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest

# Driver Code
x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))
z = int(input("Enter the third number : "))
print(maximum(x, y, z))



# METHOD 2 (LIST)
def maximum(a, b, c):
    list = [a, b, c]
    return max(list)

# Driver Code
x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))
z = int(input("Enter the third number : "))
print(maximum(x, y, z))



#METHOD 3 (USING MAX FUNCTION)
# Driver Code
x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))
z = int(input("Enter the third number : "))
print(max(x, y, z))