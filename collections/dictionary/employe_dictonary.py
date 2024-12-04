
# create a dictionary employee with keys eid,name,salary,department,experience

# employee={"E-id":123,
#           "name":"vaishnav",
#           "salary":30000,
#           "department":"Hr",
#           "experience":6 }

# print(employee["salary"])

# # add contact as "23456"

# employee["contact"]=23456

# print(employee)

# """if employee experience > 5 update salary as current_salary+10000 
# else current_salary+5000"""

# if employee["experience"]>5:

#     employee["salary"]+=10000

# else:

#     employee["salary"]+=5000

# print(employee)

# if employee["experience"]>5:

#     employee["roll"]="SDE"

# else:
#     employee["roll"]= "JDE"

# print(employee)



# create a dictionary employee with keys id,name,salary,department,age



# get()
# pop()
# keys()
# values()
# items()


employee={"id":123,"name":"vaishnav","salary":30000,"department":"Hr","age":32 }

print(employee.get("salary"))  #get(key)


# invalid key return 

# pop(key) remove

employee.pop("salary")

print(employee)


# return all key  => keys()

for k in employee.keys():

    print(k)


# fetch all values  => values()

for v in employee.values():

    print(v)


# fetch key and values => items()

for k,v in employee.items():

    print(k,v)


# get()
# pop()
# keys()
# values()
# items()


