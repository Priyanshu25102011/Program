def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"

    binary_result = ""
    
    max_bits = 0
    temp_val = decimal_num
    while temp_val > 0:
        temp_val //= 2
        max_bits += 1
    
    for i in range(max_bits - 1, -1, -1):
        power_of_2 = 1
        for _ in range(i):
            power_of_2 *= 2
        
        if decimal_num >= power_of_2:
            binary_result += "1"
            decimal_num -= power_of_2
        else:
            binary_result += "0"
            
    return binary_result.lstrip('0') or '0'

try:
    num = int(input("Enter a non-negative decimal number: "))
    if num < 0:
        print("Please enter a non-negative number.")
    else:
        binary_representation = decimal_to_binary(num)
        print(f"The binary representation of {num} is: {binary_representation}")
except ValueError:
    print("Invalid input. Please enter an integer.")