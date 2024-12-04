from re import findall

f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\regular_expression_files_works\\url.txt")

content=f.read()

pattern="https?://[\w\S./]+"

urls=findall(pattern,content)

for url in urls:

    print(url)