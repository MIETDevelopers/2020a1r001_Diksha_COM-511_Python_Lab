#BUILT IN FUNCTIONS

#Abs() : The abs() function returns the absolute value of the given number.
num1=-30.33
num2=20
print('Absolute value of -30.33 is : ', abs(num1))
print('Absolute value of 20 is : ', abs(num2))


#Len():The len() function returns the number of items (length) in an object.
languages=['Python', 'Java', 'Javascript']
length=len(languages)
print('Length of tuple is : ', length)
string='Physics'
length1=len(string)
print("Length of string is : ", length1)


#min() : The min() function returns the smallest item in an iterable.
numbers=[9,34,11,-4,27]
min_no=min(numbers)
print('The smallest number in ', numbers[0:4], ' is : ', min_no)


#Round() : It rounds the float point number from the decimal value to the closest multiple of 10.
print("Round off of 34.7 is= ", round(34.7))
print("Round off of 21.4 is= ", round(21.4))


#isalnum() : It returns True if all the characters are alphanumeric.
name="Python3"
print(name.isalnum())
