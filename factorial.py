def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
print(factorial.__doc__)
print("The factorial of 0 is:", factorial(0))
print("The factorial of 1 is:", factorial(1))
print("The factorial of 2 is:", factorial(2))
print("The factorial of 3 is:", factorial(3))
print("The factorial of 4 is:", factorial(4))
print("The factorial of 5 is:", factorial(5))
print("The factorial of 6 is:", factorial(6))
print("The factorial of 7 is:", factorial(7))
print("The factorial of 8 is:", factorial(8))
print("The factorial of 9 is:", factorial(9))
print("The factorial of 10 is:", factorial(10))