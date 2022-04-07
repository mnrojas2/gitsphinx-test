"""
main - runs all the thingy
"""
import sys
from classes import *
from tqdm import tqdm
import time

__version__ = "0.0.1a"


def main():
    clasebase = TestClass("La clase", "test", "red")

    for i in range(40):
        if i % 2 == 0:
            print("Loop", i, clasebase)

        if i == 10:
            clasebase.changeName("DrMario")
        elif i == 15:
            clasebase.changeColor("Blue")
        elif i == 20:
            clasebase.externalFunction("myFunction")
        elif i == 30:
            clasebase.changeClassStatus()
        time.sleep(0.1)
    input()


if __name__ == '__main__': main()
