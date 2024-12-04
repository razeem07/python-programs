
arr=[1,2,2,1,2,3,4,3]

arr.sort()

com_num=[]

for i in range(0,len(arr)-1):
        
    j=i+1
   
    result=arr[j]-arr[i]

    if result==0:
        if arr[i] not in com_num:

            com_num.append(arr[i])

print(com_num)

