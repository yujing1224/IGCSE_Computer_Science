#data validation - length check (admin password)

#1 - get name of the password
admin_password = input("enter your new password: ")
#2 - get the length
admin_password_length = len(admin_password)
#3 - validation
if(admin_password_length >= 6 or admin_password_length <= 12):
    print("password is updated")
else:
    print("password must be 6-12 characters") 



#check if user enters an empty string
# P.S : In Python and many other programming languages, 
#a single equal mark is used to assign a value to a variable, 
#whereas two consecutive equal -=marks is used to check whether 2 expressions give the same value
#(y==z) is True because we assign equal values to y and z
name = input("enter your name: ")
name_length = len(name)

if(name_length == 0):
    print("You cannot enter an empty name")
elif(name_length < 3):
    print("name must be nore than three letters")
elif(name_length > 25):
    print("name must be less than 25 characters")





pet_name = input("What is your new pet name? ")
pet_name_length = len(pet_name)
if(name_length < 2):
    print("your name is too short")
elif(name_length >= 20):
    print("your name is too long")
else:
    print("what a great name")


#validation task - write code that takes user input and validates its length
#ask the user for a resturant name
#validate that the name is greater than 5 letters and less than 25 letters
resturant_name = input('Name of the resturant: ')
resturant_name_length = len(resturant_name)
if(resturant_name_length > 0 and resturant_name_length < 5):
    print("your name is too short, please change a name")
elif(resturant_name_length == 0):
    print("blank detected, please enter a name")
elif(resturant_name_length > 25):
    print("your name is too long, please change a name")
else:
    print(resturant_name, "what a great name!!")












