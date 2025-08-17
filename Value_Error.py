try:
    number = int(input("Please enter a number: "))
    print("The number entered is:", number)
except ValueError as ex:
    print("Exception:", ex)