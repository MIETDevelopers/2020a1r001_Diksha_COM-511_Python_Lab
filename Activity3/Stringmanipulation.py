#STRING MANIPULATION

#A) Count the number of alphabets in the given string

#Method 1 : Using isalpha() + len()
test_str = 'python is easy to code'
#printing original string
print("The original string is :" +str(test_str))
#isalpha() to computation of Alphabets
res = len([l for l in test_str if l.isalpha()])
print("Count of Alphabets :" +str(res))

#Method 2 : Using ascii_uppercase() + ascii_lowercase() + len()
import string
test_str = 'python is easy to code'
#printing original string
print("The original string is :" +str(test_str))
#ascii_lowercase and ascii_uppercase
res = len([l for l in test_str if l in string.ascii_uppercase or l in string.ascii_lowercase])
print("Count of Alphabets :" +str(res))


#B) To extract characters in the given,range from the given string 

#Method 1: Using join()+list comprehension
test_list=["python","is","easy","to","code"]
#printing original string
print("The original string is :" +str(test_list))
strt, end = 11, 18
res = ''.join([sub for sub in test_list])[strt : end]
print("Range characters :"+str(res))


#C) Check if the string is alphanumeric or not

#Method 1: String isalnum()
string ="abc 123"
print(string, "is alphanumeric?",string.isalnum())
string ="abc_123"
print(string, "is alphanumeric?",string.isalnum())
string ="000"
print(string, "is alphanumeric?",string.isalnum())
string ="aaaa"
print(string, "isalphanumeric?",string.isalnum())

#Method 2:Isalnum() in if...else statement
password ="user123456"
if password.isalnum():
    print("Password is alphanumeric")
else:
    print("Password is not alphanumeric")    