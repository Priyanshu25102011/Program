string = input("Enter your own string: ")
string2 = ''
for i in string:
    string2 = i + string2
print("The Original String is: ", string)
print("The Reversed String is: ", string2)