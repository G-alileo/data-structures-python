# This is a python program to perform a linear search
# loops through all the elements in an array, returns the target

# linear search function
def linear_search(array, target):
    for index in range (len(array)):
        if array[index] == target:
            return index
    return -1


# Taking user array input
user_array = input("Enter an array of numbers separated by spaces: ")
array = list(map(int, user_array.split()))

# Getting target value
target = int(input("Enter the Target value : "))

# Calling linear search function 
result = int(linear_search(array, target))

if result == -1:
    print(f" {target} not found")

else:
    print (f" {target} is at position {result+1}")


