medical_cause = input("Did you have medical cause Y or N:")
atten = int(input("Enter the ateendece of student: "))

if medical_cause == "Y":
    print("You are allowed")

else:
    if atten >= 75:
        print("You are allowed")
    else:
        print("You are not allowed")
