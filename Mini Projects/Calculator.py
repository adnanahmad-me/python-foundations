'''
Enter two numbers and program will calculate 
several arithmetic operations between the two.
'''
print("      Calculator App\n")

# inputs
# print("Please enter two numbers a and b:")
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

# outputs
print(f"\nResults:\n{a} + {b} = {a+b}\n{a} - {b} = {a-b}\n{a} x {b} = {a*b}")
print(f"{a} ÷ {b} = {a/b}\n{a} ^ {b} = {a**b}\n{a} mod {b} = {a%b}")