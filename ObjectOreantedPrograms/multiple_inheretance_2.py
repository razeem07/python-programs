
# Cusine(cusine_name)
# MealType(name)
# Dish(dish_name) display_dish_info()

# indian,break_fast,gheeroast,
# italian,
# break_fast
# pasta

# inheritance
# Polymorphism
    # methodoverloading
    # methodoverriding


class Cusine:

    def __init__(self,cusine_name):

        self.cusine_name=cusine_name

    def display_cusine_info(self):

        print(self.cusine_name)