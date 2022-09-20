#DICTIONARY OPERATIONS

# creating a dictionary
dict = {1:"one", 2:"two", 3:"three"}
print("The dictionary is - ")
print(dict)
print()

# inserting in a dictionary
dict[4] = "four"
print(dict)
print()

# updating a dictionary
dict.update({4:"FOUR"})
print(dict)
print()

# deleting from a dictionary
del dict[4]
print(dict)
print()



#DICTIONARY IMPLEMENTATION

# python script to check whether a given key already exists in a dictionary or not
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
    if x in d:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')
is_key_present(5)
is_key_present(9)

#Python script to merge two Python dictionaries.
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)