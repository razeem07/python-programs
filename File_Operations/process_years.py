yesrs_path="C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\data_sets\\years.txt"

centuary_path="C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\data_sets\\centuary_yr.txt"

leap_yr_path="C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\data_sets\\leap_yr.txt"

f_read=open(yesrs_path,"r")

f_centuary=open(centuary_path,"w")

f_leap_yr=open(leap_yr_path,"w")

for year in f_read:

    year=int(year)

    if year%100==0:

        f_centuary.write(str(year)+"\n")

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

        f_leap_yr.write(str(year)+"\n")


f_read.close()
f_centuary.close()
f_leap_yr.close()
