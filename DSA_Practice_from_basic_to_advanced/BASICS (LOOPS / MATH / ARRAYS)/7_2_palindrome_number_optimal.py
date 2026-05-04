def palindrome_number(x: int) -> bool:
    if x < 0:
        return False

    original = x
    rev = 0

    while x > 0:
        digit = x % 10
        rev = rev * 10 + digit
        x //= 10

    return original == rev

x=int(input("Enter a number: "))
if palindrome_number(x):
    print(f"{x} is a palindrome number.")   
else:    
    print(f"{x} is not a palindrome number.")

