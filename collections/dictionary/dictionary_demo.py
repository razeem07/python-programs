

# create a dictionary product with key id,title,price,barand


product={"id":123,"title":"manager","price":300,"brand":"britania"}

print(product["brand"])

# update brand to "parla" and "price"

product["brand"]="parla"

product["price"]=250

print(product)

product["use_by_date"]="12/09/2025"

print(product)

product["offer"]=5

print(product)


# add offer as 10 if offer exist else add offer as 20 


if "offer" in product:

    product["offer"]=10

else:

    product["offer"]=20

print(product)


