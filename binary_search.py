def binary_search(arr,target):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

values = [5, 10, 20, 30, 45, 60, 75]
target = int(input("Enter a number to search : "))

result = binary_search(values, target)

if result != -1:
    print(f"{target} found at position {result + 1}")
else:
    print(f"{target} not found")

