user_string = input("Enter a string value: ")
reverse_string = ""

for char in user_string:
    reverse_string  = char + reverse_string

print(f"Reverse string of {user_string} is {reverse_string}")
