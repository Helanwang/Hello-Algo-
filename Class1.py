class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info_car(self, year):
        print(f"the car, {self.make}, is in made in {year}")


"""
self.year was NOT used in the display_info method 
bc year parameter is not an attribute of the Car class.

It just an parameter of the info_car method. 

If you use that method then pass in, otherwise is not part of the Car attributes. 
"""

little_car1 = Car("Audi", "A4")
little_car1.info_car(2024)

