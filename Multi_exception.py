try:
    num1, num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1/num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by zero is an error")

except SyntaxError:
    print("Comma is missing. Enter numbers seperated by commas like this 1,2")

except:
    print("wrong input")

else:
    print("NO exceptions")
    
finally:
    print("This will execute no matter what")