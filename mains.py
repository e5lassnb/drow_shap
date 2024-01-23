
from Retangle import *
point1=Point(-1,-1)
point2=Point(100,-30)
shape1=Rectangle(Point(3,3),Point(100,100))

def move_shape(shape,point1,point2):
    top_left_new=(shape.top_left.x+point1.x,shape.top_left.y+point1.y)
    botom_reight_new=(shape.bottom_right.x+point2.x,shape.bottom_right.y+point2.y)
    print(repr(shape))

    # return (top_left_new,botom_reight_new)




(move_shape(shape1,point1,point2))