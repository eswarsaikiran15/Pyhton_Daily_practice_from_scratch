arr=list(map(int,input("enter numbers separated by space:").split())) #taking input as a list of integers
def even(n):
    for num in arr:
        if num%2==0:
            print(num,end=" ")  #print even numbers in the array
def odd(n):
    for num in arr:
        if num%2!=0:
            print(num,end=" ")  #print odd numbers in the array
print("Even numbers in the array:")
even(arr)   
print("\nOdd numbers in the array:")
odd(arr)