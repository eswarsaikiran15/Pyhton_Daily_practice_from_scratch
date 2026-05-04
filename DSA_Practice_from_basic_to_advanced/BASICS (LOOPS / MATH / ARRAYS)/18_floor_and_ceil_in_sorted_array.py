arr = [10, 20, 30, 40]
x = 25

floor_val = None
ceil_val = None

low, high = 0, len(arr) - 1

while low <= high:
    mid = (low + high) // 2
    
    if arr[mid] == x:
        floor_val = ceil_val = arr[mid]
        break
    elif arr[mid] < x:
        floor_val = arr[mid]
        low = mid + 1
    else:
        ceil_val = arr[mid]
        high = mid - 1

print("Floor:", floor_val)
print("Ceil:", ceil_val)
