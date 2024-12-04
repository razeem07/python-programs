from json import load

f=open("C:\\Users\\hp\\OneDrive\\Desktop\\Pythonworks\\data_sets\\countries.json",encoding="utf-8")

data=load(f)

# print number of countries

# print(len(data))

# print all country names

all_country_name=[country.get("name")for country in data]

# print(all_country_name)

# print all regions

all_regions=[country.get("region")for country in data ]

# print(set(all_regions))

# print region count

region_count={region:all_regions.count(region)for region in all_regions}

# print(region_count)


max_region_count=max(region_count,key=lambda k:region_count.get(k))

# print(max_region_count,region_count.get(max_region_count))


# capitals of specific country [India]

# userinput= input("enter the name: ")

# country_capital=[country.get("capital")for country in data if country.get("name")== userinput]

# print(country_capital)


# countries with most number of borders

most_borders={country.get("name"):len(country.get("borders",[0]))for country in data }

# print(most_borders)

max_borders_count=max(data,key=lambda country :len(country.get("borders",[]))).get("name")

# print(max_borders_count)

# most populated country

most_populated_country=max(data,key=lambda country : country.get("population",0)).get("name")

# print(most_populated_country)


# border sharing countries

userinput=input("Enter the name: ")

aplfa_three_codes=[country.get ("borders") for country in data if country.get("name") == userinput][0]

for code in aplfa_three_codes:

    for country in data:

        if country.get("alpha3Code")==code:

            print(country.get("name"))
