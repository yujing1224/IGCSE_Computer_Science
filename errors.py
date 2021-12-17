#user input error - this throw an exeception if a string is given by user
age = int(input("Enter your age: "))

#try-catch block
try :
    age = int(input("Enter your age:"))
except ValueError as error:
    print("Please enter a number only")
    print(error)
    print(type (error))
else:
    print('No exceptions were thrown, execute this:')



#zero division error 
try :
    age = int(input("Enter your age:"))
    calculation  = 10/age
except (ValueError,ZeroDivisionError) :
    age = int(input("Please enter a vaild:"))
else:
    print('No exceptions were thrown, execute this:')
    




