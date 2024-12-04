words_path="C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\data_sets\\words.txt"

palendrom_path="C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\data_sets\\palendrom.txt"

f_read=open(words_path,"r")

f_write=open(palendrom_path,"w")

for line in f_read:

    word=line.rstrip("\n")

    reversed_word=word[::-1]

    if word==reversed_word:

        f_write.write(word+"\n")

f_read.close()
f_write.close()