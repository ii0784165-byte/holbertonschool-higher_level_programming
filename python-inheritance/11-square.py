#!/usr/bin/python3
"""
Module that defines the Square class inheriting from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Attributes:
        __size (int): Private size of the square
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the string representation of the square.
        """
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
