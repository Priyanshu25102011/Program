units = int(input("Enter the number of units consumed: "))
if (units < 50):
    amount = units * 2.60
    surcharge = 25

elif (units <= 100):
    amount = 130 + (units - 50) * 3.25
    surcharge = 35

elif (units <= 150):
    amount = 130 + 162.5 + (units - 100) * 5.26
    surcharge = 45

total = amount + surcharge
print("\n Electricity Bill = %.2f" % total)