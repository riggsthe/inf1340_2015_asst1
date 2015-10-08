#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""
__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


# Note how many shares Lakshmi bought and establish a variable for those shares
number_of_shares_bought = 2000
# Establish a variable for the amount of money each share cost to buy
price_per_share_buy = 900.00
# Establish a total cost variable which multiples the amount of shares bought by the cost per share
total_cost = (number_of_shares_bought * price_per_share_buy)

# Establish the broker's commission on this purchase by multiplying the total cost by 3%
broker_commission = total_cost * 0.03

# Note how many shares Lakshmi sold and establish a variable for those shares
number_of_shares_sold = 2000
# Establish a variable for the new price per share to sell
price_per_share_sell = 942.75
# Establish a total gain variable which multiplies the number of shares sold by the new price per share
total_gain = (number_of_shares_sold * price_per_share_sell)

# Establish the broker's second commission by multiplying the total gain by 3%
second_broker_commission = total_gain * 0.03

# Establish the total profit of Lakshmi's trading on its own by subtracting the total cost from the total gain
profit = total_gain - total_cost

# Figure out the broker's total fees by adding the first broker commission to the second broker commission
broker_total_fee = broker_commission + second_broker_commission

# Establish the amount of money Lakshmi had at the end of the day by subtracting the broker's total
# fee from Lakshmi's profits
end_of_the_day = profit - broker_total_fee
print end_of_the_day
