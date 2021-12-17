#character (letter) list
letter_grades = ["A", "A-", "A", "B", "B", "C", "C-", "A-", "B+"]
letter_grades.append("B")
letter_grades.append("A")
letter_grades.append("A")


#count number of people with grade A
number_of_A_grades = letter_grades.count("A")
print("number of grades A:", number_of_A_grades)

#integer list
numbers = [0, 0, 1, 1, 2, 3, 4, 0, 0, 1, 1, 0, 0, 1, 0, 0]
zero_frequency = numbers.count(0)
print("number of zeros", zero_frequency)

#sort list
numbers.sort()

#priunt each item in list (iteration)
for number in numbers:
    print(number)

#boolean list
has_completed_homework = [True, True, False, True, False, False, True]
number_of_completed_homeworks = has_completed_homework.count(True)
print("Number of people who did homework", number_of_completed_homeworks)

