number_val = int(input("Enter a number of which you wants to find factorial: "))
factorial = 1

while  number_val > 0:
    factorial *= number_val
    number_val -= 1

print(f"Factorial is: {factorial}")

