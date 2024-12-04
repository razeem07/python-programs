





# print(text.isalnum)


text="hello,world,python,java"

words=text.split(",")

# print(words)


text="\n we need to \n get going \n"

# remove \n

new_text=text.strip("\n")

# print(new_text)

# lstrip
# rstrip


text="hello world program"

# o => a 

new_text=text.replace("o","a",3)

# print(new_text)

text="python programming"
    # 012345678901234567
    # string_object[start:end:step]

# print(text[:6])

# print(text[7:])

# print(text[::])

# print(text[::2])

# print(text[::-1])

string="hello world"

rerversed_text=string[::-1]

# print(rerversed_text)


text="helloworld"
#     0123456789

# index od first o 

# text.repace()
# text.index("o") => 4 

# print(text.index("w"))


text="vaishnav@gmail.com"

# find index of @
# slice text from 0:index of slice


# print(text[0:text.index("@")])

text="hellopython"
# llehopython

o_index=text.index("o")

reversed_sub_str=text[o_index-1::-1]

balanced_sub_str=text[o_index:]

result=reversed_sub_str+balanced_sub_str

# print(result)













