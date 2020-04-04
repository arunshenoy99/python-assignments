from food import Food
class Fruit(Food):

    def __init__(self, name, kind):
        super().__init__(name, kind)

    def clean(self):
        print('Cleaning {}'.format(self.name))


fruit = Fruit('Apple', 'veg')
fruit.clean()