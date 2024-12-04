
# def student_info(45,43,44,operation="avg")
# def student_info(45,43,44,operation="total")


def student_info(*args,**kwargs):

    if kwargs.get("operation")=="avg":

        return sum(args)/len(args)

    if kwargs.get("operation")=="total":

        return sum(args)
    
# print(student_info(45,43,44,operation="avg"))



# def sort_numbers(1,2,3,4,15,11,reverse="True") desc

# def sort_numbers(1,2,3,4,15,11,reverse="False") asc




def sort_numbers(*args,**kwargs):

    if kwargs.get("reverse")=="True":

        return sorted(args,reverse=True)

    if kwargs.get("reverse")=="False":

        return sorted(args)

print(sort_numbers(1,2,3,4,15,11,reverse="True"))
