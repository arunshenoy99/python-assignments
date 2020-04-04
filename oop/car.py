from vehicle import Vehicle
class Car(Vehicle):
    def brag(self):
        print('Look fast i am')


car1 = Car(10)
car1.drive()

print(car1)
#print(car1.__dict__ )

car2 = Car(200)
car2.drive()