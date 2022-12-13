#!/usr/bin/python3
"""
Define class Base
"""

import json
import csv


class Base:
    """
    creating class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init method with id parameter
        :param id:
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returning json file
        :param list_dictionaries:
        :return:
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        method that saves the json file
        :param list_objs:
        :return:
        """
        dictionary_list = None
        if list_objs is not None:
            dictionary_list = [i.to_dictionary() for i in list_objs]
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            f.write(Base.to_json_string(dictionary_list))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        method to save json csv file
        :param list_objs:
        :return:
        """
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
        method that updates and adds to the file
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
        returning the instance 'create' with parameter
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
        a method that return cls
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
        """
        a method that opens from json file
        :return:
        """
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
        """
        a method that updates a current argument
        :param param:
        :return:
        """
        pass
