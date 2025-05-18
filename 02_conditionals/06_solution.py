distance = int(input("Enter the distance in km: "))

if distance < 3:
    print("Walk")
elif distance <= 15:
    print("Bike")
else:
    print("Car")