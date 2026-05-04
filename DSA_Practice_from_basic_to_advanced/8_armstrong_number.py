def armstrong_number(n: int) -> bool:
    num_str = str(n)
    num_digits = len(num_str)
    armstrong_sum = 0

    for digit in num_str:
        value = int(digit) ** num_digits
        armstrong_sum += value

    return armstrong_sum == n


n = int(input("Enter a number: "))

if armstrong_number(n):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
