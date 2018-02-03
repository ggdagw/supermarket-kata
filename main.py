#!/usr/bin/python

# Python v2.7

# using a dictionary of dictionaries for two reasons:
# 1. The outer dictionary will mean no looping upon lookup, and
# 2. The inner dictionary provides an expandable container should requirements
#    change.
catalogue = { "beans":{ "list_price": 0.50 },
              "coca-cola":{ "list_price": 0.70 }, 
              "oranges":{ "list_price": 1.99 } }

print "beans", catalogue["beans"]["list_price"]
