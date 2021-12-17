#programs make decisions based on control logic (control flow)

student_grade = 93

if student_grade > 90:
    print("Your grade is A")
elif student_grade < 90 and student_grade > 80:
    print("Your grade is a B")
elif student_grade < 80 and student_grade>70:
    print("Your grade is a C")
else:
    print("Your grade is a D or F")




temperature = 20 

if temperature > 30:
    print("it's hot")
elif temperature > 10 and temperature < 30:
        print("it's warm")
elif temperature < 10: 
    print("it's cold")
else:
    print("bring an umbrella just in case")