#!/usr/bin/python3
"""Unittest for rectangle"""
import unittest
import io
import sys
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """test for Square class"""

    def test_square_size(self):
        """test without args"""
        with self.assertRaises(TypeError):
            Square.size()

        """test getter"""
        s1 = Square(2)
        self.assertEqual(s1.size, 2)

        """test setter"""
        s1 = Square(2)
        s1.size = 7
        self.assertEqual(s1.size, 7)

        """test setter with 0"""
        s1 = Square(2)
        with self.assertRaises(ValueError):
            s1.size = 0

        """test setter with negative value"""
        s1 = Square(2)
        with self.assertRaises(ValueError):
            s1.size = -5

        """test setter with wrong type: float"""
        s1 = Square(2)
        with self.assertRaises(TypeError):
            s1.size = 4.5

        """test setter with wrong type: string"""
        s1 = Square(2)
        with self.assertRaises(TypeError):
            s1.size = "python"

        """test setter with wrong type: list"""
        s1 = Square(2)
        with self.assertRaises(TypeError):
            s1.size = [4]

        """test setter with wrong type: tuple"""
        s1 = Square(2)
        with self.assertRaises(TypeError):
            s1.size = (4, )

        """test setter with wrong type: dictionary"""
        s1 = Square(2)
        with self.assertRaises(TypeError):
            s1.size = {4}

        """test str"""
        def test_square_str(self):
            """test normal str"""
            s1 = Square(2, 1, 3, 6)
            self.assertEqual("[Square] (6) 1/3 - 2", str(s1))

            """test less informations"""
            s2 = Square(2, 1)
            self.assertEqual("[Square] (24) 1/0 - 2", str(s2))
            s3 = Square(3, 1, 6)
            self.assertEqual("[Square] (25) 1/6 - 3", str(s3))
            s4 = Square(3)
            self.assertEqual("[Square] (26) 0/0 - 3", str(s4))

            """test wrong informations"""
            with self.assertRaises(ValueError):
                Square(-2)
            with self.assertRaises(ValueError):
                Square(0)
            with self.assertRaises(TypeError):
                Square(3.2)
            with self.assertRaises(TypeError):
                Square({1, 2})
            with self.assertRaises(TypeError):
                Square([1, 2])
            with self.assertRaises(TypeError):
                Square((1, 2))
            with self.assertRaises(TypeError):
                Square(float('inf'))


class TestToDict(unittest.TestCase):
    """unittest for to_dictionary method"""

    def test_to_dict(self):
        """test for normal square"""

        s1 = Square(10, 2, 1, 5)
        self.assertEqual(s1.to_dictionary(), {
                         'id': 5, 'x': 2, 'size': 10, 'y': 1})
        s1 = Square(10, 2, 1, 8)
        self.assertEqual(s1.to_dictionary(), {
                         'id': 8, 'x': 2, 'size': 10, 'y': 1})

        """"test for value error"""
        with self.assertRaises(ValueError):
            s2 = Square(-2, 3, 12)
            s2.to_dictionary()
        with self.assertRaises(ValueError):
            s3 = Square(2, -3, 12)
            s3.to_dictionary()

        """test for type error"""
        with self.assertRaises(TypeError):
            s7 = Square()
            s7.to_dictionary()
        with self.assertRaises(TypeError):
            s8 = Square(2.3, 3, 12)
            s8.to_dictionary()
        with self.assertRaises(TypeError):
            s9 = Square(2, 3.2, 12)
            s9.to_dictionary()
        with self.assertRaises(TypeError):
            s10 = Square(2, (3, 2, 3), 12)
            s10.to_dictionary()
        with self.assertRaises(TypeError):
            s11 = Square((2, 8, 9), 3, 12)
            s11.to_dictionary()
        with self.assertRaises(TypeError):
            s12 = Square(2, 3, (2, 8, 7))
            s12.to_dictionary()
        with self.assertRaises(TypeError):
            s13 = Square((), 3, 12)
            s13.to_dictionary()
        with self.assertRaises(TypeError):
            s14 = Square(2, (), 12)
            s14.to_dictionary()
        with self.assertRaises(TypeError):
            s15 = Square(2, 3, ())
            s15.to_dictionary()
        with self.assertRaises(TypeError):
            s16 = Square(float('inf'), 3, 12)
            s16.to_dictionary()
        with self.assertRaises(TypeError):
            s17 = Square(2, float('inf'), 12)
            s17.to_dictionary()
        with self.assertRaises(TypeError):
            s18 = Square(2, 12, float('inf'))
            s18.to_dictionary()


class TestSquareArgs(unittest.TestCase):
    """unittest for update args"""

    def test_update_args(self):
        """test without parameter"""
        s = Square(4, 2, 3, 1)
        s.update()
        self.assertEqual("[Square] (1) 2/3 - 4", str(s))

        """Test with one parameter"""
        s = Square(4, 2, 3, 1)
        s.update(5)
        self.assertEqual("[Square] (5) 2/3 - 4", str(s))

        """Test with two parameters"""
        s = Square(4, 2, 3, 1)
        s.update(5, 6)
        self.assertEqual("[Square] (5) 2/3 - 6", str(s))

        """Test with three parameters"""
        s = Square(4, 2, 3, 1)
        s.update(5, 6, 7)
        self.assertEqual("[Square] (5) 7/3 - 6", str(s))

        """Test with four parameters"""
        s = Square(4, 2, 3, 1)
        s.update(5, 6, 7, 8)
        self.assertEqual("[Square] (5) 7/8 - 6", str(s))

        """Test with multiple use of update() method"""
        s = Square(4, 2, 3, 1)
        s.update(5, 6, 7, 8)
        s.update(1, 2, 3, 4)
        self.assertEqual("[Square] (1) 3/4 - 2", str(s))

        """Test with None"""
        s = Square(4, 2, 3, 1)
        s.update(None)
        self.assertEqual("[Square] (None) 2/3 - 4", str(s))

        """Test with size is none"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(1, None)

        """Test with x coordinate is none"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(2, 6, None)

        """Test with y coordinate is none"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s.update(2, 6, 1, None)

        """Test size parameter with non integer"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(3600, "4")

        """Test size parameter with zero"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(3600, 0)

        """Test size with negative value"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(3600, -4)

        """Test x coordinate with non integer"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(3600, 6, "2")


class TestUpdateKwargs(unittest.TestCase):
    """test of update with kwargs"""

    def test_update_kwargs(self):
        """Test update(id=value)"""
        s = Square(4, 2, 3, 1)
        s.update(id=3600)
        self.assertEqual("[Square] (3600) 2/3 - 4", str(s))

        """Test update(size=value)"""
        s = Square(4, 2, 3, 1)
        s.update(size=8)
        self.assertEqual("[Square] (1) 2/3 - 8", str(s))

        """Test update(id, size, x, y)"""
        s = Square(4, 2, 3, 1)
        s.update(y=8, size=16, id=3600, x=4)
        self.assertEqual("[Square] (3600) 4/8 - 16", str(s))

        """Test update(size=None)"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size=None)

        """Test size parameter with non integer"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(size="4")

        """Test size parameter with zero"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(size=0)

        """Test x parameter with non integer"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s.update(x="2")

        """Test y parameter with negative value"""
        s = Square(4, 2, 3, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s.update(y=-3)


if __name__ == '__main__':
    unittest.main()
