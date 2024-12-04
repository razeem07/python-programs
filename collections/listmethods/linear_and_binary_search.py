# linear search


# arr=[2,4,6,3,8,7]
# #    0,1,2,3,4,5
# #    i

# serch_element=int(input("enter number "))

# is_present=False

# for i in range(0,len(arr)):

#     if serch_element==arr[i]:

#         is_present=True
#         break

# print(is_present)


# binary search

arr=[10,13,15,16,18,20,22,25]

#    step 1 sort() 

arr.sort()

serch_element=int(input("enter number "))

is_present=False

low=0
upp=len(arr)-1

while(low<=upp):

    mid=(low+upp)//2

    if serch_element==arr[mid]:

        is_present=True

        break

    elif serch_element<arr[mid]:

        upp=mid-1

    elif serch_element>arr[mid]:

        low=mid+1

print(is_present)









