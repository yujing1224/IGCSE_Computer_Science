#what do we want to return - Boolean (True, exists) or index or value itself (?)
#return the index 
#What is the space and time complexity of this algorithm 
#O(log n) time complexity

#Gather requirements -
#1. the target is a value in our list, but we are using list indices to calculate where we look

#Givens
sorted_list = [1, 4, 6, 9, 11, 14, 15, 16, 18, 19, 20]
target = 15

#our function -algorithm
def binary_search(sorted_list, target):
    #setup of the algorithm - getting the pointers (indicies) to move around
    left_idx = 0
    right_idx = len(sorted_list) - 1

    while(left_idx <= right_idx):
        middle_idx = int((left_idx + right_idx) / 2) #cast interger - make 5.0 to 5 w/ int () fn

        if(sorted_list[middle_idx] == target):
            return middle_idx
        elif(target < sorted_list[middle_idx]):
            right_idx = middle_idx - 1
        else:
            left_idx = middle_idx + 1
    
    return -1 #if the value isn't in the list, return -1 

result = binary_search(sorted_list, target)
print('the target number is at list index:', result)

