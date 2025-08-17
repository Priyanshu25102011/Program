# Program to check age validity and even/odd using exception handling

try:
   age = int(input("Enter your age: ")) # Try converting input to integer


# Check reasonable age range

   if age < 0 or age > 120:

    print("❌ Invalid age! Please enter a value between 0 and 120.")
   else:

    print(f"✅ You entered age: {age}")

# Check even or odd

    if age % 2 == 0:

      print("Your age is an EVEN number.")

    else:

      print("Your age is an ODD number.")
  
except ValueError:
  print("❌ Invalid input! Age must be a number.")
