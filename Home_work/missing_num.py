

arr=[1,3,4,5]

# n=1
# for i in range(0,len(arr)):

#     if n==arr[i]:

#         n=n+1
    
#     else:
#         break
# print(n)

# 0r

arr.sort()

for i in range(0,len(arr)-1):
        
    j=i+1
   

    result=arr[j]-arr[i]

    if result!=1:

     print(arr[i]+1, "is missing")

     break








# sample question 2 

# arr3=[1,2,3,5]


