input_str = input("Enter a string: ")

for char in input_str:
    if input_str.count(char) == 1:
        print(f"Unique char is: {char}")
        break