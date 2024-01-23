# from Point
from Point import Point


class Rectangle:
    def __init__(self, top_left: Point, bottom_right: Point):
        # check if points are off the grid
        # raise value exception
        if top_left.x<0 or top_left.y<0:
            raise ValueError('it is a negative value.')
        if bottom_right.x>2240 or bottom_right.y>1080:
            raise ValueError('out of the limit.')

        self.top_left = top_left
        self.bottom_right = bottom_right

    def __repr__(self):
        return (f'Rectangle({self.top_left}, {self.bottom_right})')

    # def __str__(self):
    #     return str('the  position for the Rectangle is :'
    #                 "Top left: ("+str(self.top_left) +
    #                 ' Bottom right:  '+str(self.bottom_right))


    def get_width(self):
        return self.bottom_right.x-self.top_left.x

    def get_height(self):
        return self.bottom_right.y-self.top_left.y


    def get_area(self):
        return self.get_height()*self.get_width()




