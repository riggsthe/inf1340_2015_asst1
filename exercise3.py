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
    # Issue an instruction to user to answer the first question
    first_input = raw_input("Is the car silent when you turn the key?")
    # Establish if statement if the answer to first input is yes (Y) or no (N)
    if first_input == "Y":
        # Instruct user to answer second question if the answer to input 1 is Y
        second_input = raw_input("Are the battery terminals corroded?")
        # Establish if and elif statements for Y or N answers to second question
        if second_input == "Y":
            # Since both answers produce dead ends use print statements to show the
            # final answers rather than an input function
            print("Clean terminals and try starting again.")
        elif second_input == "N":
            print("Replace cables and try again.")
    # Establish elif statement for if the answer to the second question is N
    elif first_input == "N":
        # Instruct user to answer third question if the answer to question 1 is N
        third_input = raw_input("Does the car make a clicking noise?")
        # Establish if and elif statements for Y or N answers to third question
        # Since a Y answer produces a dead end use a print statements to show the
        # final answer if Y
        if third_input == "Y":
            print("Replace the battery.")
        # Instruct user to answer fourth question if the answer to question 3 is N
        elif third_input == "N":
            fourth_input = raw_input("Does the car crank up but fail to start?")
            # Establish if and elif statements for Y or N answers to fourth question
            # Since a Y answer produces a dead end use a print statements to show the
            # final answer if Y
            if fourth_input == "Y":
                print("Check spark plug connections.")
            # Instruct user to answer fifth question
            if fourth_input == "N":
                fifth_input = raw_input("Does the engine start and then die?")
                if fifth_input == "Y":
                    sixth_input = raw_input("Does your car have fuel injection?")
                    if sixth_input == "Y":
                        print("Get it in for service.")
                    elif sixth_input == "N":
                        print("Check to ensure the choke is opening and closing.")
                        # catch dead end scenario
                elif fifth_input == "N":
                    print("Engine is not getting enough fuel. Clean fuel pump.")

# diagnose_car(raw_input)