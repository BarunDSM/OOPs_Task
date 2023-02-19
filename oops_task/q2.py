from q1 import vehicle


class car(vehicle):
    def seating_capacity(self,capacity):
        print(self.name_of_vehicle," has a seating capacity of ",capacity,"person.")

car1=car("Honda",200,70)
car1.seating_capacity(5)