"""
myFunction - Python module/function for testing importlib library
"""

__version__ = "0.0.1a"


def myFunction(class_type):
    """
    Basic function that return False or, a string and True.
    
    :param class_type: Name of the type for the class.
    :type class_type: str or None
    :return: True if the type is 'test' or False in any other case.
    :rtype: boolean
    """
    if class_type == 'test':
        print("Class needs a type change")
        return True
    return False

def main():
    """
    Function to test the correct operation of the function

    >>> main()
    False
    """
    print(myFunction('toast'))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
