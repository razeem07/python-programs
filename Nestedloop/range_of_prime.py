# read start,end

# print prime numbers from start to end

start=int(input("enter number "))
end=int(input("enter number "))

for num in range(start,end+1):

    is_prime=True

    for i in range(2,num):

        if num%i==0:

            is_prime=False

            break

    if is_prime==True:

      print(num)





#    not prime 


# start=int(input("enter number "))
# end=int(input("enter number "))

# for num in range(start,end+1):

#     is_prime=True

#     for i in range(2,num):

#         if num%i==0:

#             is_prime=False

#             break

#     if is_prime==False:

#       print(num)