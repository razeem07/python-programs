# list comprehension

# [return iteration condition]

# map() 
# filter()
# reduce  max()  min()  sum() 




arr=[2,3,4,5,6,7,8]

# addition

add_5=[num+5 for num in arr]

print(add_5)

# squares

square_num=[num**2 for num in arr]

print(square_num)

# cuqbs

cube=[num**3 for num in arr]

print(cube)

# even number

even_num=[num for num in arr if num%2==0]

print(even_num)

# odd numbers
odd_num=[num for num in arr if num%2!=0]

print(odd_num)

# num greater than 5 

num_grt_five=[num for num in arr if num > 5]

print(num_grt_five)

# words starting with vowels

text=["apple","iphone"",orange","potatto"]
