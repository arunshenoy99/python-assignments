class Food:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
    
    def describe(self):
        print('The name of the food is {} and the kind is {}'.format(self.name, self.kind))

    def __repr__(self):
        return str(self.__dict__)

food = Food('dosa', 'veg')
print(food)