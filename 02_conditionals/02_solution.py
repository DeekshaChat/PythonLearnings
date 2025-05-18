user_age = int(input("Enter your age: "))
day_of_week = input('Enter the day of the week: ').lower()
price = 0

if user_age < 18:
    price = 8
else:
    price = 12

if(day_of_week == "wednesday"):
    price = price - 2

print(f"Your ticket price is: ${price}")