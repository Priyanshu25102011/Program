Amount = int(input("Enter the Amount to Withdraw: "))

note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = (Amount%100%50)//10

print("Number of 100 notes: ", note_1)
print("Number of 50 notes: ", note_2)
print("Number of 10 notes: ", note_3)