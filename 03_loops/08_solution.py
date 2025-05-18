num = int(input("Enter a number: "))
if_prime = True

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            if_prime = False
            break
    if if_prime: print("Prime number")
else: 
    print("Not a valid input for prime number")
