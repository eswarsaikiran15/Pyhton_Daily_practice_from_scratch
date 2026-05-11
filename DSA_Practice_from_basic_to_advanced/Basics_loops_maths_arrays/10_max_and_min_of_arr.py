# using built-in functions to find maximum and minimum of an array
'''
def max_and_min_of_arr(arr):
    return max(arr), min(arr)

arr=list(map(int, input("Enter numbers separated by space: ").split())) #taking input as a list of integers
maximum, minimum = max_and_min_of_arr(arr)
print("Maximum:", maximum)
print("Minimum:", minimum)
'''
'''
output:Enter numbers separated by space: 1 56 8 79 115
Maximum: 115
Minimum: 1
'''





#option 2: without using built-in functions
def max_and_min_of_arr(arr):
    if not arr:
        return True,True  #returning True for both max and min if the array is empty
    max_val=arr[0]  #initialize max and min with the first element of the array
    min_val=arr[0]
    for num in arr:
        if max_val<num:
            max_val=num  #update max if current number is greater
        if min_val>num:
            min_val=num  #update min if current number is smaller
    return max_val, min_val

arr=list(map(int,input("enter numbers separated by a space:").split())) #taking input as a list of integers
maximum, minimum = max_and_min_of_arr(arr)
print("Maximum:", maximum)
print("Minimum:", minimum)
