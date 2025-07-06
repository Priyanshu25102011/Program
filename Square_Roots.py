import math

num = int(input("Enter a number to find its square root: "))

if num <= 0:
    print("Please enter a positive number.")
else:
    root_int = int(math.sqrt(num))

    if root_int * root_int == num:
        square_root = math.sqrt(num)
        print(f"The square root of {num} is: {square_root}")
    else:
        print(f"The number {num} is not a perfect square.")      