# Print the first 5 numbers in the Fibonacci series:


# prev=0

# curt=1

# print(prev)

# print(curt)

# for i in range(1,5):

#     next=prev+curt

#     print(next)

#     prev=curt

#     curt=next




# check 51 is a fibonacci number

num=int(input("enter number "))

prev=0

curt=1

is_fibo=False

for i in range(1,num+1):

    next=prev+curt

    prev=curt

    curt=next

if next==num:

    is_fibo=True

print(next)









