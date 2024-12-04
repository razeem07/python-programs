
# copy()
# index("object")
# insert()
# pop()
# append()
# sort()


# class list:

# def  append(self):

colors=["red","green","blue"]


# colour.append() #insert new object end of the list 

# colors.append("yellow")

# print(colors)


# def  pop(self): or pop(self,index)

colors=["red","green","blue"]
# #         0      1       2

# colour.pop()  # remove the last object from the list and returns it 

# colors.pop(1) 

# print(colors)


# def insert(self,index)

# colors.insert(0,"purple")

# print(colors)


praveen_fvt_colour=["blue","yellow","black","white"]

abishek_fvt_colour=praveen_fvt_colour.copy()

abishek_fvt_colour.pop()

# print("ab",abishek_fvt_colour)

# print("pr",praveen_fvt_colour)



# copy()
# index("object")
# insert()
# pop()
# append()
# extend()
# reverse()


# def sort(self)

lst=[2,4,6,3,5,8,7]

# lst.sort()  #assending order

lst.sort(reverse=True)    #desending order

# print(lst)




# extend()

fruits=["apple","orange","mango"]

products=["onion","potato","brinjal"]

products.extend(fruits)

fruits.reverse()

print(fruits)