
from json import load

f=open("data_sets/employee.json")

data=load(f)

for evm in data:

   print(evm)