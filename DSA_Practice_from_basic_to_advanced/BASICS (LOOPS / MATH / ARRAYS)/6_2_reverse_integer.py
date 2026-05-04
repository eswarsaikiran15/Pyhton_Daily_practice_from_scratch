def reverse(n):
    rev=0
    sign=-1 if n<0 else 1  #to handle negative numbers
    n=abs(n)  #to work with positive value of n

    while n>0:
        digit=n%10  #get the last digit
        rev=rev*10+digit  #append the digit to rev
        n//=10  #remove the last digit from n
    return sign * rev  #return the reversed number with the original sign

n= int(input("enter a number: "))
print("reversed number is:",reverse(n))

'''
enter a number: 12356
reversed number is: 65321
enter a number: -9875
reversed number is: -5789
'''