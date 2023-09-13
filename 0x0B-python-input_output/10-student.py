#!/usr/bin/python3
"""
10-student module
"""

class Student:
    """
        A class that defines a student by:
        Attributes:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        Methods:
            __init__ - Initializes the Student instance.
            to_json - Retrieves a dictionary representation of the Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """
            Initializes a Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        else:
            student_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    student_dict[attr] = getattr(self, attr)
            return student_dict
