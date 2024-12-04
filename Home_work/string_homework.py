

# sample 1
text1="PQRS"
text2="ABCD"

# merge to strings
# output "PAQBRCSD"

result=""

for i in range(0,len(text1)):

    result+=text1[i]+text2[i]

print(result)


# or
# def merge_strings(text1,text2):
    
#     result = ""
    
    
#     min_len = min(len(text1), len(text2))
    
    
#     for i in range(min_len):
        
#         result += text1[i] + text2[i]
    
    
#     if len(text1) > len(text2):
#         result += text1[min_len:]
#     elif len(text2) > len(text1):
#         result += text2[min_len:]
    
#     return result


# merged_string = merge_strings(text1, text2)

# print(merged_string)


# sample 2 
text1="PQRST"
text2="ABC"

# output :"PAQBRCST"

smallest_text=text1 if text1<text2 else text2

largest_text=text1 if text1>text2 else text2

result=""

for i in range(0,len(smallest_text)):

    result+=text1[i]+text2[i]

balance_text=largest_text[len(smallest_text):]

result+=balance_text

print(result)



