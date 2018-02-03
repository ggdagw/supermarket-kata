#!/usr/bin/python

# Python v2.7

#
# Top-level data structures:
# 'catalogue': which currently stores the pricing for items.
# 'offers':    which holds information about any available offers.
# Hardwired values for this exercise, would read from file.
#

# catalogue
# ---------
# Using a dictionary of dictionaries for two reasons:
# 1. The outer dictionary will mean no looping upon lookup, and
# 2. The inner dictionary provides an expandable container should requirements
#    change.
catalogue = { "beans":{ "list_price":0.50 },
              "coca-cola":{ "list_price":0.70 }, 
              "oranges":{ "list_price":1.99 }
}

# offers
# ------
# Using a dictionary of dictioaries for similar reasons to above.
# Referencing entries in the catalogue so that pricing only held in one
# data structure.
# Could make a derived class of Dictionary, so that we can use a self reference to
# a key called, e.g. "ales" and thus use an unrepeated entry for a 'category offer',
# such as "Any 3 ales from the set {...} for UKpounds 6.
offers = { "beans":{ "code":"2for1",
                     "quantity":2,
                     "offer_price":catalogue["beans"]["list_price"] },
           "coca-cola":{ "code":"3for2",
                         "quantity":3,
                         "offer_price":2 * catalogue["coca-cola"]["list_price"] },
           "onions":{ "code":"reduced",
                      "quantity":1,
                      "offer_price":0.29 }, # UKpounds 0.29/kg
           "gem":{ "code":"nforx",
                   "quantity":3,
                   "offer_price":6.0 }, # UKpounds 6.00
           "spitfire":{ "code":"nforx",
                        "quantity":3,
                        "offer_price":6.0 },
           "tribute":{ "code":"nforx",
                       "quantity":3,
                       "offer_price":6.0 }
}

print "gem", offers["gem"]["offer_price"]
