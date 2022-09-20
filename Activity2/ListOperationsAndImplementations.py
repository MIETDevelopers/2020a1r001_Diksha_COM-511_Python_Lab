#LIST OPERATIONS

list = [10,30,50,70,90]     # creation of list
print("List =",list)        #printing a list
list[0] = 20     #updating list[0] from 10 to 20
print("List =",list)
list.append(100)    #adds 100 to the last of list
print("List =",list) 
list.insert(3,40)   #adds 40 to the 3rd index of list
print("List =",list)
list.reverse()     #prints the reversed list
print("List =",list)
list.sort()     #prints the list in sorted order
print("List =",list)
list.count(40)    #counts how many 40 are present in list
print(list.count(40))
list.index(90)    #prints the index of 90
print(list.index(90))
list.pop(4)     #pop out the elemnet at 4th index
print(list.pop(4))
print("List =",list)
list.remove(50)    #removes the 50 from the list
print("List =",list)
print("Length of list =",len(list))   #prints the length of list
print(30 in list)     #prints true if 30 is present in list



#LIST IMPLEMENTATIONS

# program to find even numbers from a list
list = [23, 24, 5, 12, 4]
print("Even numbers in the list are...")
print()
for i in list:
    if i%2 == 0:
        print(i, end = " ")


#Interchange First and Last Element of a List
list = [100,80,60,40,20,0]
print("List =",list)
temp = list[0]   #by swapping method
list[0] = list[-1]
list[-1] = temp
print("Intechanged list =",list)

#second method
list[0], list[-1] = list[-1], list[0]
print("Intechanged list =",list)


#Program to Merge Two Lists
listA = [1,3,5,7,9]
listB = [2,4,6,8,10]
print("List A =",listA)
print("List B =",listB)
listC = listA + listB  #using + operator
print("LIST C =",listC)

#using extend method
listA.extend(listB)
print("List =",listA)