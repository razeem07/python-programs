
# full pyramid 


for row in range(1,8):

    for sp in  range(1,8-row):

        print(" ",end="")

    for col in range(1,row+1):

        print("* ",end="")

    print()
    

# inverted full pyranid



for row in range(7,0,-1):

    for sp in range(7-row):

        print(" ", end="")

    for col in range(row):

        print("* ", end="")

    print()