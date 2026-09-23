# inputs
print("Please enter the following information:")
name=input("Item name: ")
price=float(input(f"Unit price of {name}: "))
qty=int(input("Quantity: "))

# operations
total=price*qty

# output
print(f"Total amount you have to pay is ₹{total}.")