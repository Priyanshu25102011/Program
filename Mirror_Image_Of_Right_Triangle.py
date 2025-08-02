print("Right-Angled Triangle (Mirror Image) Pattern of (*)")
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n - 1 - i):
        print(" ", end=" ") 
    for k in range(i + 1):
        print("*", end=" ")
    print()