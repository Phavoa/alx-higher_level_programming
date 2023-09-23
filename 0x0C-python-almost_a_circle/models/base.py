#!/usr/bin/python3
""" base module """

import json
import os
import csv


class Base:
    """
    Base implementation
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init - Initialize a Base instance.
        Args:
            id (int): object id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries to convert.

        Returns:
            str: A JSON string representation.
             If the input list is None or empty, it returns "[]".
       """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)


    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instances to a JSON file.

        Args:
            list_objs (list): A list of instances that inherit from Base.
        """
        filename = cls.__name__ + ".json"
        json_list = []

        if list_objs is not None:
            for obj in list_objs:
                json_list.append(obj.to_dictionary())

        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))


    @staticmethod
    def from_json_string(json_string):
        """
        Convert a list of dictionaries to a JSON string.

            Args:
                json_string: A string representing a list of dictionaries.

            Returns:
                str: A Python string.
                If the input list is None or empty, it returns "[]".
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)


    @classmethod
    def create(cls, **dictionary):
        """
        Create and return an instance with attributes set.

        Args:
            **dictionary: A dictionary containing attribute key-value pairs.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            elif cls.__name__ == "Square":
                new_instance = cls(1)
            else:
                new_instance = None

            new_instance.update(**dictionary)
            return new_instance


    @classmethod
    def load_from_file(cls):
        """
        Load instances from JSON file.

        Returns:
            list: List of instances of the class.
        """
        instances = []
        file_name = cls.__name__ + ".json"
        with open(file_name, 'r') as file:
            data = file.read()
            if os.path.exists(file_name):
                json_data = json.loads(data)
                for dic in json_data:
                    inst = cls.create(**dic)
                    instances.append(inst)
                return instances
            else:
                return []



    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize instances to a CSV file.

        Args:
            list_objs (list): List of instances to serialize.
        """
        file_name = cls.__name__ + ".csv"

        with open(file_name, mode='w', newline='') as f:
            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize instances from a CSV file.

        Returns:
            list: List of instances deserialized from the CSV file.
        """
        file_name = cls.__name__ + ".csv"
        instances = []

        with open(file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    instance = cls(
                        int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                elif cls.__name__ == "Square":
                    instance = cls(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                instances.append(instance)
        return instances
