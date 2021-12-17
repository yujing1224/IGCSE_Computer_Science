#what is a string?
message = "hello word"


#strings operations-

#return length of a string - len()
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_length = len(alphabet)
#examples
print(alphabet_length)
for letter in range(alphabet_length):
    print("this is printed same # times as the length alphabet")

#lowercase -> uppercase - upper()
uppercase_alphabet = alphabet.upper()
print(uppercase_alphabet)

#what is ASCII?
#convert character to it's ASCII code - ord()
english_a = "a"
ASCII_a = ord(english_a)
print(ASCII_a)
#convert ASCII to a_z character - chr()
ASCII_code_for_a = 97
a_z_letter = chr(97)
print(a_z_letter)

#add two strings together
string_one = "good morning"
string_two = "my neighbor"
combined = string_one + " " + string_two
print(combined)

#return the position of a specific letter - index()
alphabet = "abcdefghijklmnopqrstuvwxyz"
position_of_letter_d = alphabet.index("d")
print(position_of_letter_d +1)




# strings are objects in python
#using the dot operator(.) we can access an object's function (methods)

message = "this is my message"
uppercase_message = message.upper()

#len function isn't a part of the string object it's more "general"
#that's why it's not called using the dot operator messange.len()
length = len(message)

