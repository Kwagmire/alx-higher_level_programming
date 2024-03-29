#!/usr/bin/python3
"""Task 1 of ALX Project(Python - Almost a circle)

This module defines a base model class.

"""
import json


class Base:
    """Base Model.

    This represents the base of all other classes in this project.

    """

    __nb_objects = 0  #: Number of instantiated bases.

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The identity of the new Base

        """
        if id is not None:
            self.id = id  #: This instance's identity
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list of dicts): what to represent

        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.

        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonFile:
            if not list_objs:
                jsonFile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jsonFile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): a string representation of a list of dicts

        """
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """Return an instance instantiated from a dictionary of attributes.

        Args:
            **dictionary (dict): key/value pairs of attributes to initialize.

        """
        if dictionary:
            if cls.__name__ == "Rectangle":
                newInstance = cls(2, 2)
            else:
                newInstance = cls(2)
            newInstance.update(**dictionary)
            return newInstance

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.

        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
