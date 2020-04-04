class Vehicle:
    #top_speed = 100   Class attribute here

    def __init__(self, starting_top_speed = 100):
        self.__top_speed = starting_top_speed     #Instance attribute here and __ indicates it is private

    def __repr__(self):
        return 'Top Speed: {}'.format(self.__top_speed)

    def drive(self):
        print('I am driving but certainly not faster than {}kmph'.format(self.__top_speed))