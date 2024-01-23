
import Box
import Point
import cub

rec=cub.Cube(Point.Point(0,0),Point.Point(10,10))



def test_width_for_rectangle():

    assert rec.get_width()==10

def test_hight_for_rectangle():

    assert rec.get_height()==10


def test_area_for_rectangle():

    assert rec.get_area()==60

def test_volume_for_rectangle():

    assert rec.get_volume()==1000

