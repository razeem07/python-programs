
# BMI=weight_in_kg/(height_in_metre)**2

weight_in_kg=int(input("enter weight in kg"))

height_in_cm=int(input("enter height in cm"))

height_in_metre=height_in_cm/100

BMI=weight_in_kg/height_in_metre**2

BMI=round(BMI,1)

print(BMI) 

# print under weight if bmi <19

# print nirmal weight if bmi 19 to <25

# print overweight if bmi 25 to <30

# print obese if bmi >=30  



if BMI<19:                   # 0-18 range

    print("under weight")

elif BMI<24:                 # 19-24 range 

    print("normal weight")

elif BMI<30:                 # 25-29 range

    print("over weight")

elif BMI>=30:                # >30

    print("obese")
