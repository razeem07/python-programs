from re import finditer

text="I have 3 cars,2 bike and 1-cycle"

pattern="\w"

#pattern="\d"(digits)

#pattern="\D"(exclude digit)

#pattern="\W"(special character)

# pattern ="\w" (alphanumeric)

#pattern="\s"(space)

#pattern="\S"(exclude space)

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())
