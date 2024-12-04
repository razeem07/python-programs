

# create a function 


# sum

def sum(num1,num2):

    result=num1+num2

    print(result)

sum(100,300)

# cube

def cube(num):

    result=num**4

    print(result)

cube(4)


# create a function last_digit_max with two param num1,num2

def last_digit_max(num1,num2):

    num1_last_digit=num1%10
    num2_last_digit=num2%10

    print(num1 if num1_last_digit>num1_last_digit else num2)

print(last_digit_max(123,371))





