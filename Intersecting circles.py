from manim import *
import math

def circle_intersection(x0,y0,r0,x1,y1,r1):
    r = (x0**2 - x1**2) + (y0**2 - y1**2)
    intersection_point_x0 = 0
    intersection_point_y0 = 0
    intersection_point_x1 = 0
    intersection_point_y1 = 0

    # y = 2x(x0-x1) - ((r0^2 - r1^2) - (x0^2 - x1^2) - (y0^2 - y1^2)) / 2(y0 - y1)

    return (intersection_point_x0, intersection_point_y0), (intersection_point_x1, intersection_point_y1)

def test_circle_intersection():
    sqrt3 = math.sqrt(3)
    x0 = 0
    y0 = 0
    r0 = 1
    x1 = -(sqrt3 / 2)
    y1 = -0.5
    r1 = sqrt3 / 2

    expected_x0 = 0.15095350
    expected_y0 = 0.98854086
    expected_x1 = 0.93157825
    expected_y1 = -0.3635408

    epsilon = 0.0001

    (intersection_point_x0, intersection_point_y0), (intersection_point_x1, intersection_point_y1) = circle_intersection(x0,y0,r0,x1,y1,r1)

    assert abs(expected_x0 - intersection_point_x0) < epsilon
    assert abs(expected_y0 - intersection_point_y0) < epsilon
    assert abs(expected_x1 - intersection_point_x1) < epsilon
    assert abs(expected_y1 - intersection_point_y1) < epsilon

test_circle_intersection()