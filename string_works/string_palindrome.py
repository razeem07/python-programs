

# text=input("enter text")

# reversed_string=text[::-1]

# print("palindrome" if text==reversed_string else "not plaindrome")


text="malayalam"
#intex012345678
# len 123456789

lengeth=len(text)-1 

reversed_str=""

for i in range(lengeth,-1,-1):

    reversed_str+=text[i]

print(reversed_str)