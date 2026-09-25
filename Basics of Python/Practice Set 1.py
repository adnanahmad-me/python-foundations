# 1. Program to find remainder when a number is divided by z.

print("Please enter the following information:")

dividend=float(input("The number you want to divide: "))
divisor=float(input("The number you divide by: "))

remainder=dividend%divisor

print(f"The Remainder is {remainder} when {dividend} is divided by {divisor}.")


# 2. Python program to display a user entered name followed by Good Afternoon using input() function

name = input("Name: ")
print(f'Good Afternoon, {name.title()}.')  # ---> newer method
# print('Good Afternoon, {}.'.format(name.title())) # ---> older method


# 3. Program to detect double space in a string.

string=input("String: ")
print(string.find("  "))

# 4. Replace the double space from above problem with single spaces.

print(string.replace("  "," "))


# 5. Program to format the following letter using escape sequence characters.
#    letter = "Dear Adnan, this python course is nice. Thanks!"

letter = "Dear Adnan,\n\tThis python course is nice.\nThanks!"
print(letter)