
import Box
import Point
rec=Box.Box(Point.Point(0,0),Point.Point(10,10),4)



def test_width_for_rectangle():

    assert rec.get_width()==10

def test_hight_for_rectangle():

    assert rec.get_height()==10


def test_area_for_rectangle():

    assert rec.get_area()==360

def test_volume_for_rectangle():

    assert rec.get_volume()==400

