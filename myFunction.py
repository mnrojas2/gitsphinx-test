"""
myFunction - Python function for testing importlib library

"""

__version__ = "0.0.1a"


def myFunction(class_type):
    """
    Hace algo
    >>> myFunction('toast')
    False

    >>> myFunction('test')
    Class needs a type change
    True

    :param class_type: str
    :return: bool
    """
    if class_type == 'test':
        print("Class needs a type change")
        return True
    return False

def main():
    """
    Solo ejecuta el código

    >>> main()
    False
    """
    print(myFunction('toast'))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
