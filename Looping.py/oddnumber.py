
begin=int(input("enter number ")) #50
end=int(input("enter limit ")) #10 

if begin>end:

    begin,end=end,begin

i=begin

while(i<=end):

    if i%2!=0:

        print(i)

    i+=1 

    