""" This program implements a Polygon class using the Test-Driven Development (TDD) process. 
It utilizes attributes, constructors, getters, and setters to define the Polygon class and its behavior."""

class Polygon:

    def __init__(self, name, sides):
        """Initializes a Polygon with a name and sides."""

        self.__name = name
        self.__sides = sides

    def get_name(self):
        """Returns the name of the Polygon."""

        return self.__name
    
    def set_name(self, newName):
        """Sets a new name for the Polygon."""

        self.__name = newName
    
    def get_sides(self):
        """Returns the sides of the Polygon."""

        return self.__sides
    
    def set_sides(self, newSides):
        """Sets new sides for the Polygon."""

        self.__sides = newSides

    def __eq__(self, other):
        """Checks if two Polygons are equal."""

        return self.__name == other.__name and self.__sides == other.__sides
    
    def __ne__(self, other):
        """Checks if two Polygons are not equal."""

        return self.__name != other.__name or self.__sides != other.__sides
    
    def __str__(self):
        """Returns a string representation of the Polygon."""

        return f"{self.__name} with sides: {self.__sides}"

    def calculate_circumference(self):
        """Calculates the circumference of the Polygon."""
        return sum(self.__sides)

def main():    
    hexagon = Polygon("Hexagon", [5, 5, 5, 5, 5, 5])
    print(f"{hexagon} Circumference: {hexagon.calculate_circumference()}")
    
    square = Polygon("Square", [4, 4, 4, 4])
    print(f"{square} Circumference: {square.calculate_circumference()}")

    triangle = Polygon("Triangle", [3,3,3])
    print(f"{triangle} Circumference: {triangle.calculate_circumference()}")



if __name__ == '__main__':
    main()
