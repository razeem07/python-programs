from re import finditer

f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\regular_expression_files_works\\social_post.txt")

for line in f:

    word=line.rstrip("\n")

    pattern="#\w+"

    matcher=finditer(pattern,word)

    for obj in matcher:

        print(obj.group())