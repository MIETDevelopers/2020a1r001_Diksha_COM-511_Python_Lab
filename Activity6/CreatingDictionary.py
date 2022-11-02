#Creating dictionary using For Loop

students = dict()
n = int(input("Enter number of students :"))
for i in range(n):
        sname = input("Enter names of student :")
        marks= []
        for j in range(5):
           mark = float(input("Enter marks :"))
           marks.append(mark)
        students[sname] = marks
print("Dictionary of student created :")
print(students)