"""
classes - Python library for testing purposes.
"""
import numpy as np
import importlib

__version__ = "0.0.1a"


class TestClass:
    """
    TestClass - Class that contains some functions, just for testing purposes
    """
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
        """
        Function to change the name of the class
        :param new_name: The new name that wants to replace the old one.
        :type new_name: str
        :return: false
        :rtype: boolean
        """
        self.name = new_name

    def changeColor(self, new_color):
        """
        Function to change the assigned color of the class
        :param new_color: The new color that wants to replace the old one.
        :type: new_color: str
        :return: false
        :rtype: boolean
        """
        self.color = new_color

    def externalFunction(self, function_file):
        """
        Function to load an external function through the importlib library
        :param function_file: Name of the py file that contains the function.
        :type function_file: str
        :return: false
        :rtype: boolean
        """
        self.module = importlib.import_module(function_file)

    def changeClassStatus(self):
        """
        Function to update the class type, based on the info from the external function
        """
        importlib.reload(self.module)
        if self.module.myFunction(self.class_type):
            self.class_type = 'useless'

    def __str__(self):
        """
        Returns a string in case the class itself gets printed.
        """
        return str("This is a test function for readthedocs.io, " + self.name + ", " + self.class_type + ", " + self.color)

def main():
    """
    Function to test the correct operation of the class
    """
    test = TestClass("clasecita", "clasetipo", "verde")
    print(test)

if __name__ == '__main__': main()
