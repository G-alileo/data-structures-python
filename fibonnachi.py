# This is a program illustrating the fibinnachi sequence
# Eg 0,1,1,2,3,5,8,13,21

print ("\n \t\t This is the fibonnachi Sequence")

# Taking user input
size = int(input("Enter the range/size of the sequence: "))

# initializing variables and start value
a, b = 0, 1

# display default values
print(f"[{a}", b, sep=",", end="")

# Looping to print values
for i in range(size-2):
    c = a + b
    print (",", c, sep="", end="")
    a, b = b, c

print ("]", end="\n")

