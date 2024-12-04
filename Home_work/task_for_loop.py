# 1. **Print numbers from 1 to 10:**
#    - Input: None
#    - Output: 1 2 3 4 5 6 7 8 9 10

# Print numbers from 1 to 10
for number in range(1, 11):
    print(number)

# -----------------------------------

# 2. **Print the first 5 multiples of 3:**
#    - Input: None
#    - Output: 3 6 9 12 15

for i in range(1, 6):
    print(3 * i)

# -----------------------------------

# 3. **Print the sum of numbers from 1 to 5:**
#    - Input: None
#    - Output: 15

total_sum = 0
for i in range(1, 6):
    total_sum += i

# print("The sum of numbers from 1 to 5 is:", total_sum)


# ------------------------------

# 4. **Print the first 5 natural numbers in reverse order:**
#    - Input: None
#    - Output: 5 4 3 2 1


for i in range(5, 0, -1):
    print(i, end=' ')


# ----------------------------

# 5. **Print the squares of numbers from 1 to 5:**
#    - Input: None
#    - Output: 1 4 9 16 25
   
for i in range(1, 6):
    print(i * i, end=' ')

# -----------------------------------

# 6. **Print the factorial of 5:**
#    - Input: None
#    - Output: 120

factorial = 1
for i in range(1, 6):
    factorial *= i
print(factorial)

# ---------------------------------------

# 7. **Print the first 5 even numbers:**
#    - Input: None
#    - Output: 2 4 6 8 10

for i in range(1, 6):
    print(2 * i, end=' ')

# -----------------------------------------

# 8. **Print the first 5 odd numbers:**
#    - Input: None
#    - Output: 1 3 5 7 9

for i in range(5):
    print(2 * i + 1)

# --------------------------------------------

# 9. **Print each character of the string 'Python':**
#    - Input: 'Python'
#    - Output: P y t h o n

string = "Python"
for char in string:
    print(char)

# -----------------------------------------

# 10. **Print numbers from 10 to 1:**
#     - Input: None
#     - Output: 10 9 8 7 6 5 4 3 2 1

for i in range(10, 0, -1):
    print(i )


# -------------------------------------------

# 11. **Print the first 5 numbers in the Fibonacci series:**
#     - Input: None
#     - Output: 0 1 1 2 3

a = 0
b = 1
for i in range(5):
    print(a)
    a, b = b, a + b

# ------------------------------------------------

# 12. **Print the table of 5:**
#     - Input: None
#     - Output: 5 10 15 20 25 30 35 40 45 50

number = 5

for i in range(1, 11):
    print(number * i, end=' ')
    
# ----------------------------------------------

# 13. **Print the sum of all even numbers from 1 to 10:**
#     - Input: None
#     - Output: 30

sum_even = 0

for number in range(1, 11):
    if number % 2 == 0:
        sum_even += number
print(sum_even)

# ---------------------------------------------

# 14. **Print the sum of all odd numbers from 1 to 10:**
#     - Input: None
#     - Output: 25

sum_odd = 0

for number in range(1, 11):
    if number % 2 != 0:
        sum_odd += number
print(sum_odd)

# ---------------------------------------

# 15. **Print the reverse of the string 'hello':**
#     - Input: 'hello'
#     - Output: olleh

text = 'hello'


reversed_string = text[::-1]

print(reversed_string)
