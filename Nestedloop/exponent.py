# create a function exopnent with two parameter num1,n 


def expo(num,n=2):

    return num**n

# print(expo(6))


# create a function smart_sub with three parameter num1,num2,reverse ?

def smart_sum(num1,num2,reverse):

    return num2-num1 if reverse==True else num1-num2

# print(smart_sum(10,20,True))



# create a function random_numbers(start,end,step)
# print numbers from start to end 
# random_numbers(1,7,2) #1,3,5

def random_numbers(start,end,step=1):

    i=start

    while i <= end:

        print(i)

        i+=step


random_numbers(1,7,2)





