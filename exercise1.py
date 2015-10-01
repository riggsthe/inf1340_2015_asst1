#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""
__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


# original notes left by prof money = 1000.00 print(money)

#TESSIE'S CODE STARTS!

# establish number_of_shares_bought = 2000
number_of_shares_bought = 2000
# establish price_per_share_buy = 900.00
price_per_share_buy = 900.00
# establish total cost formula
total_cost = (number_of_shares_bought * price_per_share_buy)
print ("Lakshmi spent")
print total_cost
print ("buying her shares.")

# establish first broker commission formula
broker_commission = total_cost * 0.03

print ("The broker fee on this first sale was")
print broker_commission

# two weeks later
print("Two Weeks Later...")
# establish number of shares sold
number_of_shares_sold = 2000
# establish price per share to sell
price_per_share_sell = 942.75
# establish total gain formula
total_gain = (number_of_shares_sold * price_per_share_sell)
print("Lakshmi made")
print total_gain
print("selling her shares.")
# establish second broker commission formula
second_broker_commission = total_gain * 0.03
print("The broker fee on this second sale was")
print second_broker_commission
# final_result = (total_gain - total_cost)
