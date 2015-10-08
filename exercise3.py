#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car(answer):
    """
    is the car silent when you turn the key?
    yes
    are the battery terminals corroded?
    yes
    clean terminals and try starting again
    test
    """
# Issue an instruction to user to answer the first question 1 
first_input = raw_input ("Is the car silent when you turn the key?")
if first_input == "Y":
    second_input = raw_input("Are the battery terminals corroded?")
    if second_input == "Y":
        print("Clean terminals and try starting again.")
    elif second_input == "N":
        print("Replace cables and try again.")
elif first_input == "N":
    third_input = raw_input("Does the car make a clicking noise?")
    if third_input == "Y":
        raw_input("Replace the battery.")
    elif third_input == "N":
        fourth_input = raw_input("Does the car crank up but fail to start?")
        if fourth_input == "Y":
            print("Check spark plug connections")
        if fourth_input == "N":
            fifth_input = raw_input("Does the engine start and then die?")
            if fifth_input == "Y":
                sixth_input = raw_input("Does your car have fuel injection?")
                if sixth_input == "Y":
                    print("Get it in for service.")
                elif sixth_input == "N":
                    print("Check to ensure the choke is opening and closing.")
            elif fifth_input == "N":
                print("Error.")
        



diagnose_car(raw_input)