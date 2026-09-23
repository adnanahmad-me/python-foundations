# input
num=int(input("Please enter a number: "))

# operations
a_val=abs(num)
sq=num*num             # or num**2
cube=num**3            # or num*num*num
pos=num>0
neg=num<0

# output
print(f"Absolute value of {num} is {a_val}")
print(f"Square of {num} is {sq}.\nCube of {num} is {cube}")
print(f"{num} is a positive number: {pos}\n{num} is a negative number: {neg}")