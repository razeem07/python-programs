# def add_num(*args):

#     return sum(args)


# print(add_num(10,20))

# print(add_num(20,20,40))

# print(add_num(10,30,50))



# create a function thatb accept any numbers of arguments and return second largest number?


# def second_max_num(*args):

#     sorted_num=sorted(args,reverse=True)

#     return sorted_num[1]

# print(second_max_num(10,12,11,14,16))


# (**kwargs)


# def display_mob_data(**kwargs):

#    print(kwargs.get("name"))

# display_mob_data(name="redmi",price=2800,display="amoled")




# calculator (10,20,30,operation="+")


def calculator(*args,**kwargs):

    if kwargs.get("operation")=="+":

        return sum(args)
    
    if kwargs.get("operation")=="*":

        result=1
        for num in args:

            result=result*num
        return result
    
print(calculator(10,20,30,operation="+"))


