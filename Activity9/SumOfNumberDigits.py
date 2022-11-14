# Python code to demonstrate sum of number digits in List using loop + str()

# Initializing list
test_list = [12, 67, 98, 34]

# printing original list
print("The original list is : " + str(test_list))

# Sum of number digits in List using loop + str()
res = []
for i in test_list:
	sum = 0
	for digit in str(i):
		sum += int(digit)
	res.append(sum)

# printing result
print ("The sum of the List integers is : " + str(res))