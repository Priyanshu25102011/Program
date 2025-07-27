string = input("Please enter a word: ")
char = input("Please enter a character to count: ")
i = 0
count = 0
while (i < len(string)):
    if (string[i] == char):
        count = count + 1
    i = i + 1
print("The Total number of Times", char, "has Occured is =", count)