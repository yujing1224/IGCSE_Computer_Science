#array
from array import array
#create a new array using built in array method
test_scores = array("i", [90,70,40,60,98,93])

#add another test scores to end of our array (append = add)
test_scores.append(100)
print(test_scores[0])

#literate over the array
for score in test_scores:
    print(score)

#get length of the array
length = len(test_scores)
print("length of the array(number of scores): ", length)