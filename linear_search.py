# This is a python program to perform a linear search
# loops through all the elements in an array, returns the target

# linear search function
def linear_search(array, target):
    for index in range (len(array)):
        if array[index] == target:
            return index
    return -1

array = [10, 20, 30, 40, 50]
target = int(input("Enter the Target value [10,20,30,40,50] : "))

result = int(linear_search(array, target))

if result == -1:
    print(f" {target} not found")

else:
    print (f" {target} is at position {result+1}")


