#variabes-

#a) write a boolean to represent whether you pass the test
pass_test = True

#b) write an interger variable to represent your score
score = 100

#c) write a floating point variable to repersent the class average on the exam
class_average = 5.22

#d) write a string varaible to represnt something you'd say to your friend in the morning
chats_with_friend = "Wow! You weren't late for school!"



#interations - for loop

#a) write a for loop that prints "I am a polite and kind person" x10
for i in range(10):
    print("I am a polite and kind person", i)

#while loop
counter = 0
while(counter < 10):
    print("I know computer science", counter)
    counter = counter + 1

working = True
while(working == True):
    print("working")
    working = False
#In Python and many other programming languages, a single equal mark is used to assign a value to a variable, whereas two consecutive equal marks is used to check whether 2 expressions give the same value+=



#control flow - write a simple if-elif statement to describe this
#a) if student has a grade of 90-100 print "you rock"
#b) elif student has a grade of 90-80 print "you are great"
#c) elif student has a grade of 70-80 print "not bad, keep working"
#d) else if student has a grade of less than 70 print "you can always do more and become more, growth mindset"

student_grade = 12
if student_grade > 90 and student_grade <= 100:
    print("you rock")
elif student_grade > 80 and student_grade < 90:
    print ("you are great")
elif student_grade > 70 and student_grade <80:
    print("not bad, keep working")
else:
    print("you can always do more and become more, growth mindset")



#arithemic operations 
#write code to complete the following arithmetic operations
#print the results on the screen

1 + 5 
99999 - 9494
38484 * 999
24 / 2
90 % 10

happy = 1
sad = 5
feelings = happy + sad
print("feelings:", feelings)
a = 99999 
b = 9494
c = a-b
print("99999-9494=",c)
d = 38484
e = 999
f = d * e
print("38484 * 999=",f)
g = 24
h = 2
i = g/h
print("24/2=", i)
m = 90
n = 10
o = 90%10
print("90%10=", o)

students = 21
student_money = 15.5
class_total = students * student_money
print(class_total)



#string operations
alphabet = "abcdefghijklmnopqrstuvwxyz"

#find how many characters are in it - len
alphabet_length = len(alphabet)
print(alphabet_length)

#write code to find the index (position) of the letter"t" - find
position = alphabet.find("t")
print(position)

#get and store user input - input
#write code to ask for the users name
name = input("Enter your name: ")

#output the user input on the screen
print("Good morning", name)