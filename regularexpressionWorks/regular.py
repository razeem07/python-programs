from re import finditer

text="atcatratcamontoatget"

pattern="at"

matcher=finditer(pattern,text)

for obj in matcher:

    print(obj.start(),obj.group())


    