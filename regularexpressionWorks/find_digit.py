
from re import finditer

text="I have 3 cars, 2 bike and 1 cycle"

# pattern="[a-zA-Z]" 
                              
# pattern "[abc]        => either "a" or "b" or "c"

# pattern "ab"          => chk for "ab" pair in the given text

# pattern "[a-z]"       => chk for all lowercase  alphabets 

# pattern "[a-zA-Z]      => chk for all  alphabets

# pattern "[a-zA-Z0-9]" => chk for all  alphanumeric

# pattern="[0-9]"       => chk for digits

# pattern = "[^ak]"    #  => exclude "a" & "k"

# print all lowercase alphabets exclude a,k

pattern="[^akA-Z0-9/-]" 



matcher=finditer(pattern,text)                    

for obj in matcher:                                

    print(obj.start(),obj.group())