string = input("Enter your own string: ")
string2 = ''
while string:
    string2 = string[0] + string2
    string = string[1:]
print("The Reversed String is: ", string2)