def sum_of_array(arr: list) -> int:
    total = 0
    for num in arr:
        total += num
    return total

arr=list(map(int, input("Enter numbers separated by space: ").split())) #taking input as a list of integers
print("Sum of the array:", sum_of_array(arr))


