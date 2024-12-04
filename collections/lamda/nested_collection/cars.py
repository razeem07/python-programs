cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},

    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},

    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt","dct"]},
    
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt","torque"]},
]

# print count of vehicles
# print(f"total vehicles=> {len(cars)}")


# print available colours of baleno

colours_baleno=[car.get("colors") for car in cars if car.get("name")=="baleno"]

# print(colours_baleno[0])

# print all brands

all_brands = {car.get('brand') for car in cars} 

# print(all_brands)

# print car names available in amt transmissions

amt_transmission=[car.get("name")for car in cars if "amt" in  car.get("transmissions")]

# print(set(amt_transmission))

# cars available in blue

blue_aval=[car.get("name")for car in cars if "blue" in car.get("colors")]

# print(set(blue_aval))


# print all transmissions types


all_transmissions=[t for car in cars for t in car.get("transmissions")]

# print(set(all_transmissions))


# print all colors 

all_colors={color for car in cars for color in car.get("colors")}

# print(all_colors)


# most popular color 

all_color=[color for car in cars for color in car.get("colors")]

# print(all_color)

color_count={color:all_color.count(color) for car in cars for color in car.get("colors")}

# print(color_count)

polular= max(color_count,key=lambda count:color_count.get(count))

# print(f"most popular color is {polular}")


# costly car

costly_car=max(cars,key=lambda d:d.get("price"))

# print(costly_car.get("name"))


# car with min cost 

affodable_car=min(cars,key=lambda d:d.get("price"))

# print(affodable_car.get("name"))


# sort cars wrt price

sorted_car=sorted(cars,key=lambda d:d.get("price"),reverse=True)

sorted_car_name={car.get("name"):[car.get("price"),car.get("brand")] for car in sorted_car}

print(sorted_car_name)











