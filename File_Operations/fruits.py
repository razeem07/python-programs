

f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\data_sets\\fruits.txt","r")

fruits=[]

for line in f:
    fruits.append(line.rstrip("\n"))

print(fruits)
