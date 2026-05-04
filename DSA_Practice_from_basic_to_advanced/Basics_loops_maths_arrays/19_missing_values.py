arr=[1,2,4,5,6,7,8,9]
n=9
expected=n*(n+1)//2
actual=sum(arr)
missing=expected-actual
print("Missing number is:",missing)