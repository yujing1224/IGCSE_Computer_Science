#initalize a list (linkedlist) []
from typing import NamedTuple


student_names = ["Mike", "Amy", "Charlie", "Marco", "David", "Leon", "Rain", "Angelina", "Yujing"]

#add a name to our list
student_names.append("Howard")
student_names.insert (0, "Mr.Amini") #insert at indext (0) first position

#delete a name
student_names.remove("Charlie")

#iterate over our list
for name in student_names:
    print(name)

#get the length of the list
length = len(student_names)
print(length)

#sort
student_names.sort()
for name in student_names:
    print(name)

#combine two lists
letters = ["a", "b", "c",]
numbers = [1, 2, 3]
combine_list = letters + numbers
print(combine_list)

#boolean list
is_students_homework_completed = [True, False, True]