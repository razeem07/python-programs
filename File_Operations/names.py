
f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\data_sets\\names.txt","w")

names=("python","java","c#","javascript")


for n in names:

    f.write(n+("\n"))

f.close()