#!/usr/bin/env python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the object to the specified file using pickle."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            pass

    @classmethod
    def deserialize(cls, filename):
        """Deserializes an object from the specified file using pickle."""
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                return None
        except (FileNotFoundError, pickle.UnpicklingError, EOFError):
            return None
