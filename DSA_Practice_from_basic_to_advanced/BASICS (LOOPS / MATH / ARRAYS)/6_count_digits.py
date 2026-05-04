def count_digits(n):
    count=0
    n=abs(n)  #to handle negative numbers
    if n==0:
        return 1  #0 has 1 digit
    while n>0:
        count+=1
        n//=10  #integer division by 10 to remove the last digit
    return count

n=int(input("enter a number: "))
print("number of digits:",count_digits(n))


'''
output:enter a number: 12345
number of digits: 5
''' 