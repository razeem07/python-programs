
# # lst=[]
# # tp=()


st=set()

st={10,20,30}

# print(st)


# duplicate
st={10,20,30,30,20,10}

# print(st)


colours={"red","green","blue"}


colours.add("yellow")

# print(colours)

arr=[10,30,20,20,10,30,60] #remove duplicate

# fetch numbers from arr

st=set()

for num in arr:

    # add num to set

    st.add(num)

# print(st)


st1={10,20,30,40,50}

st2={10,20,60,70,80}

intersection_set=st1.intersection(st2)

# print(intersection_set)

union_set=st1.union(st2)

# print(union_set)

difference_set=st1.difference(st2)

# print(difference_set)


str={10,20,30,40,50}

str.remove(50)

# print(str)


# st1={1,2,3}
# st2={1,2,3,4,5}

# print(st1.issubset(st2))
# print(st2.issuperset(st1))

st3={1,2,3,10,20}
st4={1,2,3,4,5}

# syymetric_difference=st1.symmetric_difference(st2)

# print(syymetric_difference)   #AUBM - A^B

st3.update(st4)

print(st3)