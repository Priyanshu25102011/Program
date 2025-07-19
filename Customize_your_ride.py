print("select your ride")
print("1. Bike")
print("2. Car")

choice = int(input("Enter your choice: "))

if (choice == 1):
    print("Which type of bike")
    print("1. Scooter")
    print("2. Scooty")

    choice2 = int(input("Enter your choice: "))
    if (choice2 == 1):
        print("You have selected Scooter")

    else:
        print("You have selected Scooty")

elif (choice == 2):
    print("Which type of car")
    print("1. Sedan")
    print("2. SUV")

    choice3 = int(input("Enter your choice: "))
    if (choice3 == 1):
        print("You have selected Sedan")

    else:
        print("You have selected SUV")