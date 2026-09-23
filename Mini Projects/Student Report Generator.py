print("Please enter the following information:")
# inputs
name=input("Name: ")
roll_no=input("Roll Number: ")

phy=int(input("Physics Mark: "))
chem=int(input("Chemistry Mark: "))
maths=int(input("Mathematics Mark: "))
hindi=int(input("Hindi Mark: "))
eng=int(input("English Mark: "))

# calculations
total=phy+chem+maths+hindi+eng
avg=total/5

# output
print("\n================================\n       STUDENT REPORT\n================================\n")
print(f"Name: {name}\nRoll Number: {roll_no}\n")
print(f"English: {eng}\nHindi: {hindi}")
print(f"Physics: {phy}\nChemistry: {chem}\nMathematics: {maths}\n")
print(f"Total: {total}\nAverage: {avg}\n================================")