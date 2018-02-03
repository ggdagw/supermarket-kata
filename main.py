#!/usr/bin/python

# Python v2.7

#
# Top-level data structures:
# 'catalogue': currently stores the pricing for items.
# 'offers':    holds information about any available offers.
# 'basket':    holds the items to be purchased.
# 'purchases': a dictionary of 'purchase bags' to hold the items in the basket. 
# The values for these data structures are Hardwired values for this exercise.
# Would otherwise read from file.
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
offers = { "beans":{ "unique_code":"3for2-beans",
                     "quantity":3,
                     "offer_price":2 * catalogue["beans"]["list_price"] },
           "coca-cola":{ "unique_code":"2for1-coca-cola",
                         "quantity":2,
                         "offer_price":catalogue["coca-cola"]["list_price"] },
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
# Using a dictionary of dictionaries again.
# Purchases is a dictionary of 'purchase bags', keyed by unique offer codes.
# Initialise with key "none" and empty 'purchase bag', to hold the standard purchases.
purchases = { "none":{ "items":[], "offer_price":0 } }

if __name__ == '__main__':
    """doc string"""

    for item in basket:
        # Extend the tuple with the list price:
        scanned_item = (item[0], item[1], catalogue[item[0]]["list_price"])
        # Check if there is an offer for that item:
        if scanned_item[0] in offers:
            # If yes, check if we already have a purchase bag for that offer:
            unique_offer_code = offers[scanned_item[0]]["unique_code"]
            if unique_offer_code in purchases: 
                # If yes, add this item:
                purchases[unique_offer_code]["items"].append(scanned_item)
            else:
                # If no create a new purchase bag for the offer and add the item:
                purchases[unique_offer_code] = { "items":[], "offer_price":0 }
                purchases[unique_offer_code]["items"].append(scanned_item)
        else:
            # if no, add to the default purchase holder
            purchases["none"]["items"].append(scanned_item)

    # report purchases costs
    for unique_offer_code in purchases:
        # standard purchases:
        if unique_offer_code == "none":
            print "standard purchases:"
            for scanned_item in purchases[unique_offer_code]["items"]:
                # print item
                print scanned_item[0], scanned_item[1] * scanned_item[2]
        # offers:
        else:
            print "offers:"
            for scanned_item in purchases[unique_offer_code]["items"]:
                offer_quantity = offers[scanned_item[0]]["quantity"]
                offer_price = offers[scanned_item[0]]["offer_price"]
                item_quantity = scanned_item[1]
                item_list_price = scanned_item[2]
                quotient = item_quantity // offer_quantity
                remainder = item_quantity % offer_quantity
                print scanned_item[0], scanned_item[1] * scanned_item[2], unique_offer_code, (quotient * offer_price + remainder * scanned_item[2])   
