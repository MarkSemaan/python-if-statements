
Age = int(input("Enter your age: "))


if (Age <= 8):
    print("The ticket price is 5$")
elif(8 < Age <= 12):
    print("The ticket price is 8$")
elif(13 <= Age <= 17):
    print("The ticket price is 10$")
else:
    print("The ticket price is 12$")