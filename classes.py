"""
classes - Python library for testing purposes.
"""
import numpy as np
import importlib

__version__ = "0.0.1a"


class TestClass:
    def __init__(self, name, c_type, color):
        self.name = name
        self.class_type = c_type
        self.color = color

    def testFunction(self, descriptor=None):
        """
        Returns a print with a sentence with the descriptor as string.

        :param descriptor: The descriptor, duh.
        :type descriptor: str or None
        :return: A sentence with the descriptor
        :rtype: str
        """
        if descriptor == None:
            return "Nothing to see here"
        else:
            return "This function is "+descriptor

    def changeName(self, new_name):
        self.name = new_name

    def changeColor(self, new_color):
        self.color = new_color

    def externalFunction(self, function_file):
        self.module = importlib.import_module(function_file)

    def changeClassStatus(self):
        importlib.reload(self.module)
        if self.module.myFunction(self.class_type):
            self.class_type = 'useless'

    def __str__(self):
        """
        Returns a string in case the class itself gets printed.
        """
        return str("This is a test function for readthedocs.io, " + self.name + ", " + self.class_type + ", " + self.color)

def main():
    test = TestClass("clasecita", "clasetipo", "verde")
    print(test)

if __name__ == '__main__': main()
