coffee_size = input("What size coffee would you like? (small, medium, large): ").lower()
extra_shot = True
order = ""

if extra_shot:
    order = coffee_size + " Coffee and an extra shot"
else:
    order = coffee_size + " Coffee"

print(f"Your order is: {order}")