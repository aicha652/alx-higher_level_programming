#!/usr/bin/python3
"""Unitest for base"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Define unitest for Base class"""

    def test_base_id(self):
        """Test id attribute"""
        b1 = Base()
        b2 = Base()
        b3 = Base(14)
        b4 = Base()
        b5 = Base(2)
        b6 = Base(-9)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 14)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, 2)
        self.assertEqual(b6.id, -9)


class TestToJsonString(unittest.TestCase):
    """unittest for to_json_string"""

    def test_to_json_string(self):
        """test type"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)

        """test None"""
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary.__str__(), "[]")

        """test empty"""
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary.__str__(), "[]")

        """test normal"""
        json_dictionary = Base.to_json_string([{'id': 12}])
        self.assertEqual('[{"id": 12}]', json_dictionary)


class TestToSaveToFile(unittest.TestCase):
    """unittest for save_to_file"""

    def test_to_save_to_file(self):
        """test for one rectangle"""
        r1 = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 53)

        """test for two rectangles"""
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 105)

        """test for one square"""
        s1 = Square(10, 7, 2, 8)
        Square.save_to_file([s1])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

        """test for two squares"""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 77)

        """test for overwrite"""
        s = Square(8, 5, 9, 2)
        Square.save_to_file([s1])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s1])
        Square.save_to_file([s])
        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

        """test for an empty list"""
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertTrue("[]", file.read())

        """test without arguments"""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

        """test for two arguments"""
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestFromJsonString(unittest.TestCase):
    """test for from_json_string"""

    def test_from_json_string(self):
        """test for empty string"""
        out_put = Rectangle.from_json_string("[]")
        self.assertEqual([], out_put)

        """test for None"""
        out_put = Rectangle.from_json_string(None)
        self.assertEqual([], out_put)

        json_list = Base.from_json_string('[{"id": 89}]')
        self.assertEqual([{'id': 89}], json_list)


class TestCreate(unittest.TestCase):
    """test for create"""

    def test_create(self):
        """test rectangle creation"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

        """test square creation"""
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)
        self.assertNotEqual(s1, s2)


class TestLoadFromFile(unittest.TestCase):
    """test for load_from_file method"""

    @classmethod
    def funct(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


if __name__ == "__main__":
    unittest.main()
