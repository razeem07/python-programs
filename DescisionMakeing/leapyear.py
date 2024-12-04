# create a python program to print a year is leapyear or not


year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year %100 == 0 and year % 400 == 0):
   
   print("leap year") 

else:
   
   print("non leapyear")
