def total_calc(bill_amount, tip_perce):
    total = bill_amount*( 1 + 0.01*tip_perce)
    total = round(total, 2)
    print(f"please pay: {total} $")
total_calc(150, 50)
