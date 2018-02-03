#!/usr/bin/python

# Python v2.7

#
# Top-level data structures:
# 'catalogue': currently stores the pricing for items.
# 'offers':    holds information about any available offers.
# 'basket':    holds the items to be purchased.
# 'purchases': a list of purchase class instances for the items in the basket. 
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
# e.g.
# class MyDict(dict):
#    def __getitem__(self, item):
#        return dict.__getitem__(self, item) % self
#
# dictionary = MyDict({
#
#     'user' : 'gnucom',
#     'home' : '/home/%(user)s',
#     'bin' : '%(home)s/bin' 
# })
offers = { "beans":{ "unique_code":"2for1-beans",
                     "quantity":2,
                     "offer_price":catalogue["beans"]["list_price"] },
           "coca-cola":{ "unique_code":"3for2-coca-cola",
                         "quantity":3,
                         "offer_price":2 * catalogue["coca-cola"]["list_price"] },
           "onions":{ "unique_code":"reduced-onions",
                      "quantity":1,
                      "offer_price":0.29 }, # UKpounds 0.29/kg
           "gem":{ "unique_code":"3for6-ales",
                   "quantity":3,
                   "offer_price":6.0 }, # UKpounds 6.00
           "spitfire":{ "unique_code":"3for6-ales",
                        "quantity":3,
                        "offer_price":6.0 },
           "tribute":{ "unique_code":"3for6-ales",
                       "quantity":3,
                       "offer_price":6.0 }
}

# basket
# ------
# A list of tuples: the items and their quantities:
basket = [ ("beans",3),
           ("coca-cola",2),
           ("oranges",0.2) ]

# purchases
# ---------
# Need an instance of a class to hold a purchase, as we will want a method to
# calcuate the savings made on any offers applied to the purchases.
class purchase:
    """doc string"""
    items = []
    unique_offer_code = ""
    quantity = 0
    offer_price = 0

# initialise with a single purchase instance, to hold the standard purchases
purchases = [ purchase() ]

if __name__ == '__main__':
    """doc string"""

    for item in basket:
        print item[0]
        # Extend the tuple with the list price:
        scanned_item = (item[0], item[1], catalogue[item[0]]["list_price"])
        # Check if there is an offer for that item:
        if scanned_item[0] in offers:
            # if yes, see if we have an open offer_purchase
            #   if no create new offer_purchase(s) and setup as appropriate
            #   if yes fill out, close and create accordingly

            print offers[scanned_item[0]]
        else:
            # if no, add to the default purchase holder
            purchases[0].items.append(scanned_item)


    # for purchase in purchases report costs
