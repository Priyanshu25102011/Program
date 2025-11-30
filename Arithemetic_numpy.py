import numpy as np

# First array (3x3)

a = np.arange(9, dtype=np.float64).reshape(3, 3)

print("First array:")

print(a)

print("\n")

# Second array (1x3)

b = np.array([10, 10, 10], dtype=np.float64)

print("Second array:")

print(b)

print("\n")

# Addition

print("Add the two arrays:")

print(np.add(a, b))

print("\n")

# Subtraction

print("Subtract the two arrays:")

print(np.subtract(a, b))

print("\n")

# Multiplication

print("Multiply the two arrays:")

print(np.multiply(a, b))

print("\n")

# Division

print("Divide the two arrays:")

print(np.divide(a, b))

print("\n")

