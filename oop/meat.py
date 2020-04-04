from food import Food
class Meat(Food):

    def __init__(self, name, kind):
        super().__init__(name, kind)

    def cook(self):
        print('Cooking {}'.format(self.name))


meat = Meat('chicken', 'non veg')
meat.cook()