
f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\data_sets\\words_2.txt","r")

words=[]

for line in f:

    line=line.rstrip("\n")

    all_words=line.split(" ")

    for w in all_words:

        words.append(w)

word_count={w:words.count(w) for w in words}

nested_wors_count=[[v,k]for k,v in word_count.items() ]

print(sorted(nested_wors_count,reverse=True))