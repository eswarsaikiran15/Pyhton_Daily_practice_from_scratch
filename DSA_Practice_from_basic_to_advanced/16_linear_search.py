arr=[1,2,34,5,6]
target=5
for i in range (len(arr)):
    if arr[i]==target:
        print("Element found at index:",i)
        break
    else:
        print("Element not found in the array.")
