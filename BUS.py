class Vehicle:
    def __init__(self, name, max_speed, mileage, time):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.time = time
        
class Bus(Vehicle):
    def fare(self):
        return self.mileage * self.time * 100

School_bus = Bus("School Volvo",180,12,2)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage, "Time:", School_bus.time,"hours") 
print("Total Bus fare is:", School_bus.fare())