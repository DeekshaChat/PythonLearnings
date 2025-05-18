pet = input("Enter your pet: ").lower()
pet_age = int(input("Enter your pet age: "))
                    
if pet == "dog":
    if pet_age < 2:
        print('Puppy food')
    else:
        print('Dog food')
elif pet == "cat":
    if pet_age <= 5:
        print('Kitten food')
    else:
        print('Senior cat food')