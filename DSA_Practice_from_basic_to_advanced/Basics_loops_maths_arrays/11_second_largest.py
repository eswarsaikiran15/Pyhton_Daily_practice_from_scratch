def second_largest(arr):
    if len(arr) < 2:
        return None  #return None if there are less than 2 elements in the array
    
    first_largest = second_largest = float('-inf')  #initialize first and second largest to negative infinity
    for num in arr:
        if num>first_largest:
            second_largest=first_largest  #update second largest before updating first largest
            first_largest=num  #update first largest
        elif (num < first_largest) and (num > second_largest):  #check if the current number is between first largest and second largest
            second_largest=num  #update second largest  
    return second_largest

arr=list(map(int, input("Enter numbers separated by space: ").split())) #taking input as a list of integers
result = second_largest(arr)        
print("Second largest number is:", result)