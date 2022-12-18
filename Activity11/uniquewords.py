#Write a program that inputs a text file. The program should print all of the unique words in the file in alphabetical order

#creating a text file - myfile
f = open(r"C:\Users\DIKSHA\Documents\myfile1.txt","w")
#writing into the file
text = f.write("This is an apple.\nApple is good for health.\nAn apple a day, keeps the doctor away.")
#closing the file
f.close()
#opening the file in read mode
f = open(r"C:\Users\DIKSHA\Documents\myfile1.txt","r")
#reading the contents of file
text = f.read()
print(text)
#converting all the text into lower case
text = text.lower()
#converting the string into list
alphabet = text.split()
#removes all the punctuation
alphabet1 = [alphabet1.strip('.,!;()[]') for alphabet1 in alphabet]
#removes all the apostrophes and white spaces
alphabet1 = [alphabet1.replace("'s", '') for alphabet1 in alphabet]
#creating an empty list
l = []
#iterating over the list
for alphabet1 in alphabet1:
    #using if and membership operator to check the unique words
    if alphabet1 not in l:
        l.append(alphabet1) #appending the list
l.sort() #sorting the list
print(l) #printing the list