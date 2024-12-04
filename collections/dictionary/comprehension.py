#  dictionar comprehension

# arr=[10,20,30,40,2,3]

# result={num:num**3 for num in arr }

# print(result)


# arr=[10,20,30,40,2,3,7,8,9,10,30]

# frequenct_count={num:arr.count(num) for num in arr}

# print(frequenct_count)


# text="ABABBCCDDE"

# character_frequency={ch:text.count(ch) for ch in text}

# print(character_frequency)
# # non recursive element

# for k,v in character_frequency.items():

#     if v==1:

#         print(k)


words=["hello","hai","hello","this","is","this","is","hello"]

words_frequency={w:words.count(w)for w in words}

print(words_frequency)

recursive_words=[k for  k,v in words_frequency.items()if v>1]

# print(recursive_words)




