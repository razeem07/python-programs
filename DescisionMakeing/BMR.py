
# calculate BMR

weight=int(input("enter weight in kg: "))

height=int(input("enter height in cm: "))

age=int(input("enter age: "))

gender=input("entre gender: ").lower()

print(weight,height,age,gender)

# The Basal Metabolic Rate (BMR)=

# 10 *weight (kg) + 6.25 * height(cm) - 5 * age(y) + 5 for male

# 10 * weight (kg) + 6.25 * height(cm) - 5 * age(y) - 161 for female

if gender== "male":

    BMR= 10*weight + 6.25*height - 5*age + 5  

elif gender== "female":
    
    BMR= 10*weight + 6.25*height - 5*age - 161

else:

    print("***invalid gender")

print(BMR)

activity_level=int(input("""
select activity level
press 1 for sedentary
press 2 for lightly active
press 3 for moderatly active 
press 4 for very active 
press 5 for extra active"""))

if activity_level==1:

    calorie=BMR*1.2

elif activity_level==2:

    calorie=BMR*1.375

elif activity_level==3:

    calorie=BMR*1.55

elif activity_level==4:

    calorie=BMR*1.725

elif activity_level==5:

    calorie=BMR*1.9

else:

    print("select valid active level ")



print(f"total number of calories you need in order to maintain current weight {calorie}")


target_weight=int(input("ether weight to burn in kg"))

duration=int(input("enter duration in weeks "))

# 1 kg = 7700 calories

calorie_deficty=target_weight*7700

days=duration*7

daily_calorie_deficty=calorie_deficty/days

print(f"calorie burnde per day{daily_calorie_deficty}")