from re import finditer
text="ababbabab"
matcher=finditer("ab",text)
for obj in matcher:
    print(obj.start(),obj.group())
