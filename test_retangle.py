
import Retangle
import Point
rec=Retangle.Rectangle(Point.Point(0,0),Point.Point(1,10))



def test_width_for_rectangle():

    assert rec.get_width()==1

def test_hight_for_rectangle():

    assert rec.get_height()==10



def test_area_for_rectangle():

    assert rec.get_area()==10


# def test_rectangle_off_the_grid():
#     # with pytest raises... value error
#         Rectangle(bad points)