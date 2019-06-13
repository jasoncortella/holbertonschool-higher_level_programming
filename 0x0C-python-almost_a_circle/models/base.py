#!/usr/bin/python3
"""Define Base Class"""

import json
import csv
import turtle


class Base:
    """Base Class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def test_reset():
        """resets __nb_objects for testing purposes"""
        Base.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        write_list = []
        if list_objs is not None:
            for elm in list_objs:
                write_list.append(cls.to_dictionary(elm))
        with open(cls.__name__ + ".json", 'w') as myFile:
            myFile.write(cls.to_json_string(write_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and len(dictionary) != 0:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        build_list = []
        try:
            with open(cls.__name__ + ".json", 'r') as myFile:
                read = Base.from_json_string(myFile.read())
                for elm in read:
                    build_list.append(cls.create(**elm))
                return build_list
        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes to csv"""
        with open(cls.__name__ + ".csv", 'w', newline='') as myFile:
            if list_objs is None or len(list_objs) == 0:
                myFile.write("[]")
            elif cls.__name__ is "Rectangle":
                for elm in list_objs:
                    csv.writer(myFile).writerow([elm.id,
                                                 elm.width,
                                                 elm.height,
                                                 elm.x,
                                                 elm.y])
            else:
                for elm in list_objs:
                    csv.writer(myFile).writerow([elm.id,
                                                 elm.size,
                                                 elm.x,
                                                 elm.y])

    @classmethod
    def load_from_file_csv(cls):
        """deserializes csv"""
        build_list = []
        try:
            with open(cls.__name__ + ".csv", 'r') as myFile:
                for elm in csv.reader(myFile):
                    if cls.__name__ is "Rectangle":
                        dictionary = {"id": int(elm[0]),
                                      "width": int(elm[1]),
                                      "height": int(elm[2]),
                                      "x": int(elm[3]),
                                      "y": int(elm[4])}
                    else:
                        dictionary = {"id": int(elm[0]),
                                      "size": int(elm[1]),
                                      "x": int(elm[2]),
                                      "y": int(elm[3])}
                    build_list.append(cls.create(**dictionary))
        except:
            pass
        return build_list
