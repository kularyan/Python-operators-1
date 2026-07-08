# Ask the user for a number
num = float(input("Enter a number: "))

# Square root is number raised to power 0.5
if num >= 0:
    root = num ** 0.5
    print("Square root is:", root)
else:
    print("Sorry, cannot find square root of a negative number.")
    
