try:
    age = int(input("Enter your age: "))
except ValueError as error:
    print("please enter a number only")
    print(error)
    print(type(error))
else:
    print("no exceptions were thrown, execute this")