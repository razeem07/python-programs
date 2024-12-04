
# users=["rahul","rohit","kohli","rishab","sanju","pandya","siraj"]

# rahul_followers=["rohit","kohli","rishab","rahul"]

# follow_sugestion {"sanju","pandya","siraj"}

# rahul_followers_sugestion=set(users).difference(set(rahul_followers))

# print(rahul_followers_sugestion)



users=["rahul","rohit","kohli","rishab","sanju","pandya","siraj"]

rahul_followers=["rohit","kohli","rishab","rahul"]

sanju_friends=["sanju","rohit","kohli"]

mutal_friends=set(rahul_followers).intersection(set(sanju_friends))

print(mutal_friends)
