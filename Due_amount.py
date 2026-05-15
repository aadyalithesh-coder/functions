def due_amount (paid_amount,price):
    return(paid_amount-price)

price=int(input("Enter price of items:"))
paid_amount=int(input("Enter paid amount:"))

print("Due amount = $",due_amount(paid_amount,price))
