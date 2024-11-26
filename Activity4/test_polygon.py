""" This program tests different scenarios involing the Polygon class. This includes tests for initialization, getter and setter methods, 
and equality and inequality comparisons between Polygon instances."""

import pytest
from polygon import Polygon

def test_polygon_initialization():
    """Tests the initialization of a Polygon object, including its name and sides."""

    polygon = Polygon("Triangle", [3, 3, 3])
    assert polygon.get_name() == "Triangle"  # Tests to see if the Polygon is correctly named.
    assert polygon.get_sides() == [3, 3, 3]  # Tests to see if the polygon is associated with three equal sides.

def test_get_name():
    """Tests the get_name method of the Polygon class to retrieve the name of the polygon."""

    polygon = Polygon("Square", [4, 4, 4, 4])
    assert polygon.get_name() == "Square"

def test_set_name():
    """Tests the set_name method of the Polygon class."""

    polygon = Polygon("Square", [4, 4, 4, 4])
    polygon.set_name("Rectangle")
    assert polygon.get_name() == "Rectangle"

def test_get_sides():
    """Tests the get_sides method of the Polygon class to get the sides."""

    polygon = Polygon("Pentagon", [5, 5, 5, 5, 5])
    assert polygon.get_sides() == [5, 5, 5, 5, 5]

def test_set_sides():
    """Tests the set_sides method of the Polygon class."""

    polygon = Polygon("Pentagon", [5, 5, 5, 5, 5])
    polygon.set_sides([6, 6, 6, 6, 6])
    assert polygon.get_sides() == [6, 6, 6, 6, 6]

def test_polygon_equality():
    """Tests equality between different Polygon objects based on their name and sides."""

    polygon1 = Polygon("Hendecagon", [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11])
    polygon2 = Polygon("Hendecagon", [11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11])
    polygon3 = Polygon("Icosagon", [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20])

    assert polygon1 == polygon2
    assert polygon1 != polygon3

def test_polygon_inequality():
    """Tests inequality between Polygon objects based on their name and sides."""

    polygon1 = Polygon("Square", [4, 4, 4, 4])
    polygon2 = Polygon("Square", [4, 4, 4, 4])
    polygon3 = Polygon("Nonagon", [9, 9, 9, 9, 9, 9, 9, 9, 9])
    polygon4 = Polygon("Square", [6, 6, 6, 6])

    assert polygon1 != polygon3
    assert polygon1 != polygon4
    assert not (polygon1 != polygon2)

def test_polygon_str():
    """Tests the string representation of the Polygon object."""

    polygon = Polygon("Square", [4, 4, 4, 4])
    assert str(polygon) == "Square with sides: [4, 4, 4, 4]"

def test_circumference_calculation():
    """Tests the calculation of the circumference of the Polygon."""

    hexagon = Polygon("Hexagon", [5,5,5,5,5,5])
    assert hexagon.calculate_circumference() == pytest.approx(30)