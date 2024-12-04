from re import fullmatch

month_number=input("enter number :")

pattern="([1-9]|0[1-9]|1[0-2])"

matcher=fullmatch(pattern,month_number)

if matcher==None:

    print("invalid")

else:

    print("valid")
