user_score = int(input("Enter your score: "))

if user_score >100:
    print("Invalid score")
    exit()

if user_score >= 90:
    print('Grade: A')
elif user_score >= 80:
    print('Grade: B')
elif user_score >= 70:
    print('Grade: C')
elif user_score >= 60:
    print('Grade: D')
else:
    print('Grade: F')