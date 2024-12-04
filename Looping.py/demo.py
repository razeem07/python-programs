# Input two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Determine the greater number
greater = a if a > b else b

# Find the LCM
while True:
    if greater % a == 0 and greater % b == 0:
        lcm = greater
        break
    greater += 1

# Print the LCM
print("The LCM of", a, "and", b, "is", lcm)


# HCF


# Input: Two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Initialize the HCF variable
hcf = 1

# Find the smaller of the two numbers
smaller = min(num1, num2)

# Loop from 1 to the smaller number (inclusive)
for i in range(1, smaller + 1):
    # If both numbers are divisible by i, update HCF
    if (num1 % i == 0) and (num2 % i == 0):
        hcf = i

# Output the HCF
print(f"The HCF of {num1} and {num2} is: {hcf}")
