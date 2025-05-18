fruit = input("Enter a fruit: ").lower()
color = input("Enter a color: ").lower()

if fruit == "banana":
    if color == "green":
        print("Unripe")
    elif color == "yellow":
        print("Ripe")
    elif color == "brown":
        print("Overripe")
    else:
        print("Unknown color")