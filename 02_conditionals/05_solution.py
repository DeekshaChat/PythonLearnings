weather = input("Enter the weather from the options - sunny, rainy or snowy: ").lower()

if weather == "sunny":
    print("Go for walk")
elif weather == "rainy":
    print("Read a book")
elif weather == "snowy":
    print("Build a snowman")
else:
    print("Watch tv")