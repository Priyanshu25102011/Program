actual_cost = float(input("Enter the actual cost of the product: "))
sale_amonunt = float(input("Enter the sale amount of the product: "))

if (sale_amonunt > actual_cost):
    amount = sale_amonunt - actual_cost
    print("Total Profit = {0}".format(amount))

else:
    print("NO PROFIT!!!")
