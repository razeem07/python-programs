from re import fullmatch

text="I have 3 cars,2 bike and 1-cycle"

pattern=""

matcher=fullmatch(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())
