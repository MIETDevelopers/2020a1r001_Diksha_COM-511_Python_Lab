def linearSearch(array, n, x):
    for i in range(0, n):
        if(array[i]==x):
            return i
    return -1

array=[3,7,6,98,32,12]
x=98
n=len(array)
index=linearSearch(array, n, x)

if(index==-1):
    print("Element not found")
else:
    print("Element found at index: ", index)

