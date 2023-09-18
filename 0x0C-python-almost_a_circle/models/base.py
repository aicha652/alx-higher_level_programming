#!/usr/bin/python3
"""Create a  class Base"""
import json


class Base:
    """Define a class with private attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the JSON string
        representation of list_dictionaries"""
        if (list_dictionaries is None) or (len(list_dictionaries) == 0):
            return "[]"
        else:
            jsondict = json.dumps(list_dictionaries)
            return jsondict

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes the JSON string
        representation of list_objs to a file"""

        file_name = cls.__name__ + ".json"
        """The filename must be: <Class name>.json"""

        with open(file_name, "w") as output_file:
            list_dict = [obj.to_dictionary() for obj in list_objs]
            """applying to_dictionary() method  to each object to get a
            dictionary representation of the object's attributes."""

            json_list = Base.to_json_string(list_dict)
            output_file.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        """static method that returns the list of the
        JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class method that returns an instance
        with all attributes already set"""
        dummy = cls(1, 1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """class method that returns a list of instances"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "r") as file:
            json_data = file.read()  # read json data  from file
            list_data = cls.from_json_string(json_data)
            list_instance = [cls.create(**data) for data in list_data]
        return list_instance
