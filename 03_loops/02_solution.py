num = int(input("Enter a number: "))
sum_of_even =0

for i in range(1, num+1):
    if i %2 == 0:
        sum_of_even += i

print("Sum of even number upto {} is {}".format(num, sum_of_even))