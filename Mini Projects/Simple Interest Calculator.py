print("Please enter the following information:")
#inputs
pa=int(input("Principal amount: ₹"))
rate=float(input("Rate of interest per annum (%): "))
time=float(input("Time (in years): "))

# calculations
si=(pa*rate*time)/100
amount=pa+si

# outputs
print(f"\nSimple interest is ₹{si}\nTotal amount after the given time period is ₹{amount}")