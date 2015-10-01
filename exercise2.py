#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.
# < 3 is an error
   # 3 sides is a triangle
   # 4 sides is a quadrilateral
   # 5 sides is a pentagon
   # 6 sides is a hexagon
   # 7 sides is a heptagon
   # 8 sides is a octagon
   # 9 sides is a enneagon
   # 10 sides is a decagon
   # >10 is an error

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape():
    # request input from user
    sides = raw_input("Input the number of sides your shape has!")
    # begin to display names for shapes with corresponding number of sides entered
    if sides == "3":
        print("Your shape is a triangle")
    elif sides == "4":
        print("Your shape is a quadrilateral")
    elif sides == "5":
        print("Your shape is a pentagon")
    elif sides == "6":
        print("Your shape is a hexagon")
    elif sides == "7":
        print("Your shape is a heptagon")
    elif sides == "8":
        print("Your shape is an octagon")
    elif sides == "9":
        print("Your shape is an enneagon")
    elif sides == "10":
        print("Your shape is a decagon")
    # In the case the input is not valid, display error
    else:
        print("Error")
name_that_shape()