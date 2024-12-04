from re import finditer
text="abbbababbabaaaab"
pattern="a{2}"
#pattern="a{1,3}"  min=1,max=3
matcher=finditer(pattern,text)
for obj in matcher:
    print(obj.start(),obj.group())
