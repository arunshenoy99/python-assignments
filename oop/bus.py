from vehicle import Vehicle

class Bus(Vehicle):
    
    def __init__(self, starting_top_speed):
        super().__init__(starting_top_speed)

    def add_group(self):
        print('Passengers added')

bus1 = Bus(20)
bus1.drive()
bus1.add_group()