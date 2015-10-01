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

# establish profit
profit = total_gain - total_cost
print ("Without factoring in her broker's commissions, Lakshmi made")
print profit
print ("from her trading.")

print("Her broker's total fee was")
# establish broker's total fee formula
broker_total_fee = broker_commission + second_broker_commission
print broker_total_fee

# establish end of the day take home by subtracting total broker fee from end profit
end_of_the_day = profit - broker_total_fee
print("Factoring in profits, costs and broker's commissions, Lakshmi had")
print end_of_the_day

# determine whether or not Lakshmi made a profit or lost money by determining if end of the day take home is positive or negative.
if end_of_the_day > 0:
    print("Lakshmi made a profit!")
if end_of_the_day < 0:
    print("Lakshmi lost money.")
if end_of_the_day == 0:
    print("Lakshmi broke even.")