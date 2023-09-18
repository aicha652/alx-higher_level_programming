#!/usr/bin/python3
"""Unittest for rectangle"""
import unittest
import io
import sys
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test for Rectangle class"""

    def test_rectangle_id(self):
        """Test of id"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        r2 = Rectangle(10, 2, 0, 0, -9)
        r3 = Rectangle(65, 7, 8, 6, 5)
        r4 = Rectangle(65, 7, 8, 6, 0)

        self.assertEqual(r1.id, 12)
        self.assertEqual(r2.id, -9)
        self.assertEqual(r3.id, 5)
        self.assertEqual(r4.id, 0)

    def test_width(self):
        """Test of width"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(4, 2, 3, 6)
        r3 = Rectangle(8, 2, 3, 6, 9)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.width, 4)
        self.assertEqual(r3.width, 8)

        with self.assertRaises(ValueError):
            Rectangle(-10, 2, 3, -9, -18)
        with self.assertRaises(ValueError):
            Rectangle(0, 2, 3, -9, -18)
        with self.assertRaises(TypeError):
            Rectangle(10.2, 2, 3, -9, -18)
        with self.assertRaises(TypeError):
            Rectangle("10", 2, 3, -9, -18)
        with self.assertRaises(TypeError):
            Rectangle({}, 2, 3, -9, -18)
        with self.assertRaises(TypeError):
            Rectangle([], 2, 3, -9, -18)
        with self.assertRaises(TypeError):
            Rectangle((6, ), 2, 3, -9, -18)
        with self.assertRaises(TypeError):
            Rectangle("a", 2, 3, -9, -18)
        with self.assertRaises(TypeError):
            Rectangle(None, 2, 3, -9, -18)
        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 2, 3, -9, -18)

    def test_height(self):
        """Test of height"""
        r1 = Rectangle(10, 4)
        r2 = Rectangle(4, 6, 3, 6)
        r3 = Rectangle(8, 8, 3, 6, 9)

        self.assertEqual(r1.height, 4)
        self.assertEqual(r2.height, 6)
        self.assertEqual(r3.height, 8)

        with self.assertRaises(ValueError):
            Rectangle(10, -2, 3, -9, -18)
        with self.assertRaises(ValueError):
            Rectangle(10, 0, 3, -9, -18)
        with self.assertRaises(TypeError):
            Rectangle(10, 2.3, 3, -9, -18)
        with self.assertRaises(TypeError):
            Rectangle(10, "2", 3, -9, -18)
        with self.assertRaises(TypeError):
            Rectangle(10, {}, 3, -9, -18)
        with self.assertRaises(TypeError):
            Rectangle(10, [], 3, -9, -18)
        with self.assertRaises(TypeError):
            Rectangle(10, (2, ), 3, -9, -18)
        with self.assertRaises(TypeError):
            Rectangle(10, "n", 3, -9, -18)
        with self.assertRaises(TypeError):
            Rectangle(10, None, 3, -9, -18)
        with self.assertRaises(TypeError):
            Rectangle(10, float('inf'), 3, -9, -18)

    def test_x(self):
        """Test of x"""
        r1 = Rectangle(10, 4, 7, 9)
        r2 = Rectangle(4, 6, 3, 6)
        r3 = Rectangle(8, 8, 0, 6, 9)

        self.assertEqual(r1.x, 7)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r3.x, 0)

        with self.assertRaises(ValueError):
            Rectangle(10, 2, -5, 9, -18)
        with self.assertRaises(ValueError):
            Rectangle(10, 0, -3, 9, -18)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3.5, 9, -18)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "3", 9, -18)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, {3}, 9, -18)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, [3], 9, -18)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, (3, ), 9, -18)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "P", 9, -18)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, None, 9, -18)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, float('inf'), 9, -18)

    def test_y(self):
        """Test of x"""
        r1 = Rectangle(10, 4, 7, 9)
        r2 = Rectangle(4, 6, 3, 6)
        r3 = Rectangle(8, 8, 0, 0, 9)

        self.assertEqual(r1.y, 9)
        self.assertEqual(r2.y, 6)
        self.assertEqual(r3.y, 0)

        with self.assertRaises(ValueError):
            Rectangle(10, 2, 5, -9, -18)
        with self.assertRaises(ValueError):
            Rectangle(10, 0, 3, -1, -18)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3, 9.8, -18)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3, "9", -18)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3, {9, 6}, -18)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3, [9], -18)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3, (9, 7), -18)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3, "H", -18)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3, None, -18)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3, float('inf'), -18)

    def test_area(self):
        """Test of area"""
        r1 = Rectangle(10, 4)
        r2 = Rectangle(4, 6, 3, 6)
        r3 = Rectangle(8, 8, 0, 0, 9)

        self.assertEqual(r1.area(), 40)
        self.assertEqual(r2.area(), 24)
        self.assertEqual(r3.area(), 64)

        with self.assertRaises(ValueError):
            r4 = Rectangle(-10, 4)
            r4.area()
        with self.assertRaises(ValueError):
            r5 = Rectangle(0, 4)
            r5.area()
        with self.assertRaises(ValueError):
            r6 = Rectangle(10, -4, 6, 8, 5)
            r6.area()
        with self.assertRaises(ValueError):
            r7 = Rectangle(10, 0, 6, 8, 5)
            r7.area()
        with self.assertRaises(TypeError):
            r8 = Rectangle(10.2, 2, 3, -9, -18)
            r8.area()
        with self.assertRaises(TypeError):
            r9 = Rectangle("10", 2, 3, -9, -18)
            r9.area()
        with self.assertRaises(TypeError):
            r10 = Rectangle({}, 2, 3, -9, -18)
            r10.area()
        with self.assertRaises(TypeError):
            r11 = Rectangle([], 2, 3, -9, -18)
            r11.area()
        with self.assertRaises(TypeError):
            r12 = Rectangle((6, ), 2, 3, -9, -18)
            r12.area()
        with self.assertRaises(TypeError):
            r13 = Rectangle("a", 2, 3, -9, -18)
            r13.area()
        with self.assertRaises(TypeError):
            r14 = Rectangle(None, 2, 3, -9, -18)
            r14.area()
        with self.assertRaises(TypeError):
            r15 = Rectangle(float('inf'), 2, 3, -9, -18)
            r15.area()
        with self.assertRaises(TypeError):
            r16 = Rectangle(10, 2.3, 3, -9, -18)
            r16.area()
        with self.assertRaises(TypeError):
            r17 = Rectangle(10, "2", 3, -9, -18)
            r17.area()
        with self.assertRaises(TypeError):
            r18 = Rectangle(10, {}, 3, -9, -18)
            r18.area()
        with self.assertRaises(TypeError):
            r19 = Rectangle(10, [], 3, -9, -18)
            r19.area()
        with self.assertRaises(TypeError):
            r20 = Rectangle(10, (2, ), 3, -9, -18)
            r20.area()
        with self.assertRaises(TypeError):
            r21 = Rectangle(10, "n", 3, -9, -18)
            r21.area()
        with self.assertRaises(TypeError):
            r22 = Rectangle(10, None, 3, -9, -18)
            r22.area()
        with self.assertRaises(TypeError):
            r23 = Rectangle(10, float('inf'), 3, -9, -18)
            r23.area()

    def test_str(self):
        """Test of str method"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        r2 = Rectangle(5, 5, 1, 4, 0)

        self.assertEqual(r1.__str__(), '[Rectangle] (12) 2/1 - 4/6')
        self.assertEqual(r2.__str__(), '[Rectangle] (0) 1/4 - 5/5')


class TestDict(unittest.TestCase):
    """Test of to_dictionary method"""

    def test_to_dict(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 2)
        r2_dictionary = r2.to_dictionary()

        self.assertEqual(r1_dictionary, {'x': 1,
                         'y': 9, 'id': 1, 'height': 2, 'width': 10})
        self.assertEqual(r2_dictionary, {'height': 2,
                         'id': 2, 'width': 1, 'x': 0, 'y': 0})


class TestUpdate(unittest.TestCase):
    """Test of update method"""
    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10, 10)

        """test with 0 argument"""
        r1.update()
        self.assertEqual(r1.__str__(), '[Rectangle] (10) 10/10 - 10/10')

        """test with 1 argument"""
        r1.update(89)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 10/10 - 10/10')

        """test with 2 arguments"""
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 10/10 - 2/10')

        """test with 3 arguments"""
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 10/10 - 2/3')

        """test with 4 arguments"""
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 4/10 - 2/3')

        """test with 5 arguments"""
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 4/5 - 2/3')

        """test with id == 0"""
        r1.update(0)
        self.assertEqual(r1.__str__(), '[Rectangle] (0) 4/5 - 2/3')

        """test with negative id"""
        r1.update(-5)
        self.assertEqual(r1.__str__(), '[Rectangle] (-5) 4/5 - 2/3')

        """test with id None"""
        r1.update(None)
        self.assertEqual(r1.__str__(), '[Rectangle] (None) 4/5 - 2/3')

        """test with id None and args"""
        r1.update(None, 1, 2, 3)
        self.assertEqual(r1.__str__(), '[Rectangle] (None) 3/5 - 1/2')

        """test with two updates"""
        r1.update(0, 5, 6, 7, 8)
        r1.update(9, 10, 11, 12, 13)
        self.assertEqual(r1.__str__(), '[Rectangle] (9) 12/13 - 10/11')

        """test with string for width"""
        with self.assertRaises(TypeError):
            r1.update(89, "width")

        """test with list for width"""
        with self.assertRaises(TypeError):
            r1.update(89, [1, 2])

        """test with number negative for width"""
        with self.assertRaises(ValueError):
            r1.update(89, -1)

        """test with 0 for width"""
        with self.assertRaises(ValueError):
            r1.update(89, 0)

        """test with string for height"""
        with self.assertRaises(TypeError):
            r1.update(89, 1, "height")

        """test with list for height"""
        with self.assertRaises(TypeError):
            r1.update(89, 1, [1, 2])

        """test with number negative for height"""
        with self.assertRaises(ValueError):
            r1.update(89, 1, -1)

        """test with 0 for height"""
        with self.assertRaises(ValueError):
            r1.update(89, 1, 0)

        """test with string for x"""
        with self.assertRaises(TypeError):
            r1.update(89, 1, 2, "x")

        """test with list for x"""
        with self.assertRaises(TypeError):
            r1.update(89, 1, 3, [1, 2])

        """test with number negative for x"""
        with self.assertRaises(ValueError):
            r1.update(89, 1, 3, -2)

        """test with string for y"""
        with self.assertRaises(TypeError):
            r1.update(89, 1, 2, 3, "y")

        """test with list for y"""
        with self.assertRaises(TypeError):
            r1.update(89, 1, 2, 3, [1, 2])

        """test with number negative for y"""
        with self.assertRaises(ValueError):
            r1.update(89, 1, 2, 3, -2)

        """test with strings for width and height"""
        with self.assertRaises(TypeError):
            r1.update(89, "width", "height")

        """test with strings for width and height" and x and y"""
        with self.assertRaises(TypeError):
            r1.update(89, "width", "height", "x", "y")

        """test with strings for width and x"""
        with self.assertRaises(TypeError):
            r1.update(89, "width", 2, "x")

        """test with strings for width and y"""
        with self.assertRaises(TypeError):
            r1.update(89, "width", 2, 3, "y")

        """test with strings for height and x"""
        with self.assertRaises(TypeError):
            r1.update(89, 1, "height", "x")

        """test with strings for height and y"""
        with self.assertRaises(TypeError):
            r1.update(89, 1, "height", 2, "y")

        """test with strings for x and y"""
        with self.assertRaises(TypeError):
            r1.update(89, 1, 2, "x", "y")


class TestDisplay(unittest.TestCase):
    """Test of display method"""

    @staticmethod
    def capture_out(r, method):
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(r)
        else:
            r.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_display(self):
        """test with width and height"""
        r1 = Rectangle(2, 3, 0, 0, 0)
        capture = TestDisplay.capture_out(r1, "display")
        self.assertEqual("##\n##\n##\n", capture.getvalue())

        """test with x"""
        r1 = Rectangle(2, 2, 1)
        capture = TestDisplay.capture_out(r1, "display")
        self.assertEqual(" ##\n ##\n", capture.getvalue())

        """test with width height x y"""
        r1 = Rectangle(2, 2, 1, 1)
        capture = TestDisplay.capture_out(r1, "display")
        self.assertEqual("\n ##\n ##\n", capture.getvalue())


if __name__ == '__main__':
    unittest.main()
