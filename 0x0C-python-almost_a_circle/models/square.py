#!/usr/bin/python3
"""Create a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """Define a Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        """public getter"""
        return self.width

    @size.setter
    def size(self, value):
        """public setter"""
        super(Square, Square).width.__set__(self, value)

    def update(self, *args, **kwargs):
        """public method that assigns attributes"""
        num_args = len(args)
        if args:
            if num_args >= 1:
                self.id = args[0]
            if num_args >= 2:
                self.size = args[1]
            if num_args >= 3:
                self.x = args[2]
            if num_args >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                self.y, self.size))

    def to_dictionary(self):
        """public method that returns the
        dictionary representation of a Square"""
        d = dict()
        d['id'] = self.id
        d['x'] = self.x
        d['size'] = self.size
        d['y'] = self.y
        return d
