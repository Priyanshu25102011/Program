def calculate_due_amount(total_amount, amount_paid):
  return total_amount - amount_paid

total = int(input("Enter the total amount: "))
paid = int(input("Enter the amount paid: "))

due = calculate_due_amount(total, paid)

print("Total Amount: $",total)
print("Amount Paid:  $",paid)
print("-" * 25)
print("Due Amount:   $",due)