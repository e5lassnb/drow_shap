from Retangle import *



class Cube(Rectangle):

    def __repr__(self):
        return (f'Cube({self.top_left}, {self.bottom_right})')

    # def __str__(self):
    #     return str('the  position for the cube is :'
    #                 "Top left: (" + str(self.top_left) +
    #                 ' Bottom right:  ' + str(self.bottom_right))
    #
    def get_volume(self):
        return self.get_height() * self.get_height() * self.get_height()

    def get_area(self):
        return (6 * self.get_width())


