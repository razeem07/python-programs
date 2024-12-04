
num=int(input("enter number: "))

y=num

digit_count=len(str(num))

total=0

while(num!=0):

    digit=num%10

    exponent=digit**digit_count

    total=total+exponent

    num=num//10


print("amstrong number" if total==y else "not amstrong number")

