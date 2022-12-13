#!/usr/bin/python3
"""creating a base class"""

import json
import csv


class Base:
    """base class to soon be inherited"""
    __nb_objects = 0

    def __init__(self, id=None):
        """function for base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method to_json_string with parameter
        :param list_dictionaries:
        :return:
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method to save json file
        """
        dictionary_list = None
        if list_objs is not None:
            dictionary_list = [i.to_dictionary() for i in list_objs]
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            f.write(Base.to_json_string(dictionary_list))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        global dict_list
        if list_objs is not None:
            if cls.__name__ == "Square":
                dict_list = [['id', 'size', 'x', 'y']]
                dict_list.extend([[i.id, i.size, i.x, i.y] for i in list_objs])
            else:
                dict_list = [['id', 'width', 'height', 'x', 'y']]
                c_li = [[i.id, i.width, i.height, i.x, i.y] for i in list_objs]
                dict_list.extend(c_li)
        with open(cls.__name__ + '.csv', 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(dict_list)

    @staticmethod
    def from_json_string(json_string):
        """
        static method to add and update
        :param json_string:
        :return:
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returning the class instance
        :param dictionary:
        :return:
        """
        if cls.__name__ == 'Square':
            shape = cls(1)
        else:
            shape = cls(1)
        shape.update(**dictionary)
        return shape

    @classmethod
    def load_from_file(cls):
        """
        class method that loads csv file
        :return:
        """
        try:
            with open(cls.__name__ + '.json') as f:
                text = f.read()
                return [cls.create(**i) for i in cls.from_json_string(text)]
        except FileNotFoundError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        try:
            with open(cls.__name__ + '.csv') as f:
                text_dict = csv.DictReader(f)
                if cls.__name__ == 'Square':
                    return [cls.create(**{'id': int(i['id']),
                                          'size': int(i['size']),
                                          'x': int(i['x']),
                                          'y': int(i['y'])
                                          }) for i in text_dict]
                else:
                    return [cls.create(**{'id': int(i['id']),
                                          'width': int(i['width']),
                                          'height': int(i['height']),
                                          'x': int(i['x']),
                                          'y': int(i['y'])
                                          }) for i in text_dict]
        except FileNotFoundError:
            return []

    def update(self, param):
        pass
