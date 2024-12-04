from re import fullmatch
user_input=input("enter variablr name")
#strt with an alphabet(lower,upper)
#any num of alphabet,digit,_
pattern="[a-zA-Z][a-zA-Z0-9_]*"
matcher=fullmatch(pattern,user_input)
if matcher==None:
    print("invalid")
else:
    print("valid")