def even_odd(n):
    even_count=0
    odd_count=0
    
    for num in arr:
        if num%2==0:
            even_count+=1  #increment even count if the number is even
        else:
            odd_count+=1
    return even_count,odd_count

arr=list(map(int,input("enter numbers separated by space:").split())) #taking input as a list of integers
even_count, odd_count = even_odd(arr)
print("Even count:", even_count)
print("Odd count:", odd_count)