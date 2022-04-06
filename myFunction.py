"""
myFunction - Python function for testing importlib library
"""

__version__ = "0.0.1a"


def myFunction(class_type):
    if class_type == 'test':
        print("Class needs a type change")
        return True
    return False

def main():
    print(myFunction('test'))

if __name__ == '__main__': main()
