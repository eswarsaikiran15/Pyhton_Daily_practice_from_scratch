def reverse_an_array(arr):
    left, right = 0, len(arr) - 1 # initialize pointers used to reverse the array i have used two pointers approach to reverse the array in place
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # swap elements
        left += 1
        right -= 1
    return arr

arr = list(map(int, input("Enter numbers separated by space: ").split())) #taking input as a list of integers
reversed_arr = reverse_an_array(arr)    
print("Reversed array:", reversed_arr)
