print("Enter the marks obtained in 4 subjects:")

Maths = int(input("Marks in Maths: "))
English = int(input("Marks in English: "))
Hindi = int(input("Marks in Hindi: "))
Science = int(input("Marks in Science: "))

sum = Maths + English + Hindi + Science
print("The sum of all the marks is:", sum)
 
percantage = (sum / 400) * 100
print(end="Percentage Marks: ")
print(percantage)