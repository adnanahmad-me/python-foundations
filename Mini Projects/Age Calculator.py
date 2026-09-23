print("Please enter the following information:")
# inputs
name = input("Name: ")
b_year = int(input("Birth year: "))
c_year = int(input("Current year: "))

# calculations
age = c_year-b_year

# outputs
print(f"Hello {name}, you are approximately {age} years old.")