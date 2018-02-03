#!/usr/bin/python

# Python v2.7

#
# Top-level data structures:
# catalogue: which currently stores the pricing for items
# offers:    which holds information about any available offers
#

# catalogue
# ---------
# using a dictionary of dictionaries for two reasons:
# 1. The outer dictionary will mean no looping upon lookup, and
# 2. The inner dictionary provides an expandable container should requirements
#    change.
catalogue = { "beans":{ "list_price": 0.50 },
              "coca-cola":{ "list_price": 0.70 }, 
              "oranges":{ "list_price": 1.99 }
}

# offers
# ------
# using a dictionary of dictioaries for similar reasons to above.
# referencing entries in the catalogue so that pricing only held in one
# data structure.
offers = { "beans":{ "code":"2for1",
                     "quantity":2,
                     "offer_price":catalogue["beans"]["list_price"]}
}

print "beans", offers["beans"]["offer_price"]
