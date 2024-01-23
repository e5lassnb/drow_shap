import Point
from Retangle import *
from Point import Point


class Box(Rectangle):

    def __init__(self, top_left:Point,bottom_right:Point, length:int):
        super().__init__(top_left,bottom_right)
        self.length=length

    def __repr__(self):
        return (f'Box({self.top_left}, {self.bottom_right},{self.length})')

    # def __rper__(self):
    #     return ('the  position for the Box is :'
    #                 "Top left: (" + str(self.top_left) +
    #                 ' Bottom right:  ' + str(self.bottom_right))
    #



    def get_volume(self):
        return self.get_height()*self.length*self.get_width()


    def get_area(self):
        return (2*self.length*self.get_width()+ 2*self.length *self.get_height()+2*self.get_width()*self.get_height())
