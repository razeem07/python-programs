# read two limits 
# sample input (1)
    # start=2
    # end=10

# sample outputs(1)
  # even
  # 2,4,6,8    

# sample input(2)
    # start=10
    # end=2

# samole output
    # even
    # 8,6,4,2


begin=int(input("enter number "))

end=int(input("enter end "))

# i++
# i--

reverse=True if begin>end else False

i=begin


while(i<=end if reverse==False else i>=end):

    if i%2==0:

      print(i)

    if reverse==False:
       i+=1

    else:
       
       i-=1
