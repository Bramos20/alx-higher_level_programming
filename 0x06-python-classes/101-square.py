#!/usr/bin/python3
"""
This is the Square module.
This module provides a simple Square class with initialize size.
Defaults size to 0. Raise error on invalid size inputs.
Attribute position which takes a default (0, 0) tuple.
Methods Getter and Setter properties for size and position.
Method area returns size of area of the square.
Method my_print prints the square using "#", moved over left and top using
position tuple.
Method __repr__ should return the string to print out the square.
"""


class Square:
    """A class which defines a square by size, which defaults 0.
    Also defines position using a tuple, which defaults (0, 0).
    Square can also get area, and print square using '#'.
    When printing, using position, offset on top and left.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("the size must be an integer")
        if size < 0:
            raise ValueError("the size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2 or \
           not all([type(i) == int for i in value]):
            raise TypeError("the position must be a tuple of 2 positive integers")
        self.__position = value

    def __repr__(self):
        return (self.get_str())

    def area(self):
        return self.__size * self.__size

    def get_str(self):
        total = ""
        if self.__size is 0:
            total += "\n"
            return total
        for i in range(self.__position[1]):
            total += "\n"
        for i in range(self.__size):
            total += (" " * self.__position[0])
            total += ("#" * self.__size)
            if i is not (self.__size - 1):
                total += "\n"
        return total

    def my_print(self):
        print(self.get_str())
