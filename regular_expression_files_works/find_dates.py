
# from re import finditer
from re import findall

f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\regular_expression_files_works\\dates.txt")

# for line in f:

#     word=line.rstrip("\n")

#     pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

#     matcher=finditer(pattern,word)

#     for obj in matcher:

#         print(obj.group())


content=f.read()

pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

all_dates=findall(pattern,content)

for date in all_dates:

    print(date)

# fundementals (variables,operators,datatype)
# decisionmaking (if....else,if...elif....else)
# 
