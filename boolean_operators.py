#this is a booean + if elif statement
is_computer_science_student = False                                                                                                             
is_chang_jung_student = True

if(is_chang_jung_student and is_computer_science_student):
    print("YOu are enrolled in my computer science class")
elif(is_computer_science_student or is_chang_jung_student):
    print("You may not be enrolled in my computer class")
elif(not is_computer_science_student and is_chang_jung_student):
    print("You are not in my computer science cla ss")



#and - both values must be true for the expression to be true
is_enrolled_computer_science = is_computer_science_student and is_chang_jung_student
print('the value of our AND statement',is_enrolled_computer_science)

#or - one of the values must be true for the expression to be true 
is_enrolled_chang_jung = is_computer_science_student or is_chang_jung_student
print('the value of our OR statement', is_enrolled_chang_jung)



A = True
B = True
C = A or B #expect this to be true if either A OR B is true

D = True
E = False
F = D and E #expect F to be false if both D and E are not true
print(C)
print(F)