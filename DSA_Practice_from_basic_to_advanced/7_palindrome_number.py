def palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    return str(x) == str(x)[::-1]

n = int(input("Enter a number: "))
if palindrome_number(n):
    print(f"{n} is a palindrome number.")
else:
    print(f"{n} is not a palindrome number.")