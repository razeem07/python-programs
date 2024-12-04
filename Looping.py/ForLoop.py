

# prgm to print number from 10 to 1 using for loop


# sequence=range(10,-1,-1)

# for num in sequence:
#     print(num)


# print all numbers from start to end

start=int(input("enter number "))

end=int(input("enter end "))

if start<end:

    for num in range(start,end+1,1):

       print(num)

else:

    for num in range(start,end-1,-1):

        print(num)

