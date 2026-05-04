
# Check if an array is sorted in ascending or descending order without using built-in functions
def is_sorted_asc(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def is_sorted_desc(arr):
    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1]:
            return False
    return True


arr = list(map(int, input("Enter numbers: ").split()))

if is_sorted_asc(arr):
    print("Array is sorted in ascending order.")
elif is_sorted_desc(arr):
    print("Array is sorted in descending order.")
else:
    print("Array is not sorted.")






# using built-in functions to check if the array is sorted in ascending or descending order
def is_sorted_asc(arr):
    return arr == sorted(arr)

def is_sorted_desc(arr):
    return arr == sorted(arr, reverse=True)

arr = list(map(int, input("Enter numbers: ").split()))
if is_sorted_asc(arr):
    print("Array is sorted in ascending order.")
elif is_sorted_desc(arr):
    print("Array is sorted in descending order.")
else:
    print("Array is not sorted.")
