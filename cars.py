class  Car:
    
    def __init__(self,make,model,year,color,price=None,mileage=None):
        self.make = make 
        self.model = model
        self.year = year
        self.color = color

        if price is not None:
            self.price = price
        
        if mileage is not None:
           self.mileage = mileage


    def drive(self):
        print("The car is driving!")

    def stop(self):
        print("The car is stopped!")


"""
    make =  str("Honda")
    model = str("Civic")
    year = int(2023)
    color = str("Black")
    price = int(22,000)
"""
    