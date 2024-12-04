from re import fullmatch
vech_reg=input("enter number")
pattern="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"
matcher=fullmatch(pattern,vech_reg)
if matcher==None:
    print("invalid")
else:
    print("valid")