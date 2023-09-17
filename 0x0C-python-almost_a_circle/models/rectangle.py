#!/usr/bin/python3
"""Create a class Rectangle that inherits from Base"""
Base = __import__('base').Base


class Rectangle(Base):
    """Define a class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter to set it"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter to set it"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """to retrieve x"""
        return self.__x

    @x.setter
    def x(self, value):
        """property setter to set it"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """to retrieve x"""
        return self.__y

    @y.setter
    def y(self, value):
        """property setter to set it"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """public method that returns the area
        value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """public method that prints in stdout the
        Rectangle instance with the character #"""

        z = 0
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            for k in range(self.__width):
                while (z in range(self.__x)):
                    z += 1
                    print(" ", end="")
                print("#", end="")
            z = 0
            print()

    def __str__(self):
        """Define __str__ method"""
        return("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
               self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """public method  that assigns an argument to each attribute"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
               self.x, self.y, self.width, self.height))

    def to_dictionary(self):
        """public method that returns the dictionary representation of a Rectangle"""
        d = dict()
        d['x'] = self.x
        d['y'] = self.y
        d['id'] = self.id
        d['height'] = self.height
        d['width'] = self.width
        return d
