#DATATYPES

#NUMBERS
# Integers, floating point and complex numbers fall under Python numbers category
#The class of a particular variable could be found using type() function

#integer
a=5
print(a, "is of type ", type(a))
#float
b=2.0
print(b, "is of type ", type(b))
#complex
c=1+2j
print(c, "is complex no.  ", isinstance(1+2j, complex))


#LISTS
list=[5,10,15,20,25,30,35,40]
print(type(list))
#printing the element at index 2 of the list
print("list[2]=", list[2])
#printing the elements from index 0 to 2 of the list
print("list[0:3]=", list[0:3])
#printing the elements from 5 to the end of the list
print("list[5:]=", list[5:])
#printing the element at last index
print("list[-1] = ", list[-1])


#TUPLES
tuple=(5, 'program', 1+3j)
print(type(tuple))
#printing the element at index 1 of the tuple
print("Tuple[1]=", tuple[1])
#printing the elements from index 0 to 2 of the tuple
print("Tuple[0:3}=", tuple[0:3])
#printing the elements starting from index 1 
print("Tuple[1:] = ", tuple[1:])
#printing the element at last index of the tuple
print("Tuple[-1] = ", tuple[-1])


#STRINGS
s='This is a string'
print("String =",s)
print(type(s))
#multiline string
s='''A multiline string
     here'''
print("String =",s)


#SETS
set = {5,2,3,1,4}
print("Set = ", set )
print(type(set))
set1={1,2,2,3,3,3} #set of repeating values
print(set1)     #output set has only distinct values


#DICTIONARY
d={1:'python', 'key':2}
print(type(d))
#prints the value where key=1
print("d[1] : ", d[1])
print("d['key'] : ", d['key'])


#CONVERSATIONS BETWEEN DATATYPES
print(float(5))  # Conversation from int to float
print(int(5.6))  # Conversation from float to int
print(int(-10.98))
print(float('25'))  # Conversation from string to float
print(int('35'))  # Conversation from string to int
print(str(43))  # Conversation from int to string
print(list('hello'))  # Conversation from string to list
print(tuple([22, 44, 32, 54, 'hello']))  # Conversation from list to tuple
print(set('73662727'))  # Conversation from tuple to set
print(dict([[2, 3], [4, 5]]))  # Conversation from list to dictionary

