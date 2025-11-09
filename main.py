from cars import Car

car_1 = Car("Honda","Civic",2023,"Black",22000,30000)
car_2 = Car("Toyota","Camery",2024,"Gray", 29000,35000)
car_3 = Car("Tesla","Cybertruck",2025,"Silver",83000,50000)
car_4 = Car("Ford","Explorer",2023,"Blue",52000,40000)
car_5 = Car("Chevrolet"," Corvette",2025,"Red",74000,30000)

car_6 = Car("Chevrolet"," Corvette",2020,"Black")




print("The first car we have here is a " + car_1.color + " " + car_1.make + " " + car_1.get_model() + " for $" + str(car_1.price))
print("The second car we have here is a " + car_2.color + " " + car_2.make + " " + car_2.get_model() + " for $" + str(car_2.price))

print("The 6th car we have here is a " + car_6.color + " " + car_6.make + " " + car_6.get_model() ) 

# + " for $" + str(car_6.price))
