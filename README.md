# supermarket-kata
programming exercise to model a supermarket pricing calculator

## Summary

I have written a small pricing calculator using Python.  The data structures are predominantly dictionaries of dictionaries.  These are efficient and adaptable data structures.  Hash tabels have O(1) look up costs, which will allow the code to run relatively quickly at scale (not withstanding that Python is an interpreted language).  Python's implementation of a hash table is relatively efficient in terms of memory, using less than twice the space that would be occupied by a list.  The ease of adding new keys would allow the code to be adapted should requirements change or features be added.

Currently all the key data structures are initialised as literals (i.e. the data is hardwired) and not read from file.  However, there are several Python modules (sqlite3 and MySQLdb) which provide interfaces to databases using dictionary syntax and methods.  Thus the code would require relatively little change were we to switch to using, e.g. a catalogue or a menu of offers which were stored on file as relational databases.  I have spent no time formatting the output.  I have listed a number of ways in which I would like to improve the code below.

The code currently supports offers of the form '3 for 2', '2 for £1', 'any 3 ales for £6', 'apples 20% off' and 'onions for 29p/kg'. 

## How to run

* Simply run `python main.py`.  The code is wriiten in python v2.7.

## Good points

* The code can handle 'category offers' such as '3 ales for £6'.
* The code would efficiently scale due to O(1) lookups in hash tables (python dictionaries). 

## Points to note

* It would be nice to find a more elegant set of data structures, e.g. just a catalogue and a basket.  However, I believe that a purchases data structure is required to accomodate 'category offers'.  Also the catalogue and offers structures cannot be merged until I write a derived dictionary class that supports self reference.

## Areas for improvement

1. A derived dictionary class that supported self reference would remove some repeated values.
2. Using classes would make the code safer through encapsulation and using methods would simplify the cost calculation logic.
3. I would like to store the logic of the offer calculation in the offers data structure.  I could store functions in that dictionary and could use them as call-back functions from a method in e.g. a purchase class.
4. If we stored the list and offer prices in the purchase data structure, then we could also implement a 'cheapest purchase free' or 'free delivery over £100' offers as a final pass.
4. Currently the model only supports one offer per item listed in the catalogue.  This seems rather brittle.  It would be nice if the model worked out the best offer should more than one apply to the same item (such as 20% red wine and 2for1 wines in general).  However, we rarely see this sophistication in real supermarkets.
5. There is currently no testing!  If I wrote a process_basket() function at the top level, and stored the offer and list prices in the purchase data structures, then it would be simple enough to define some test cases along with known 'purchase bags' to use with e.g. python's unittest module.
6. I would like to relax the constraint that all items in a 'category offer' must currently have the same list price.
7. There are two look-ups into the offers data structure (by item from the basket and by offer code from the purchase bags).  By default Python provides a dictionary with one key to a value.  However, it would simplify the look up code if we were able to use multikey dictionary.  It would be interesting to explore the use of https://pypi.python.org/pypi/multi_key_dict.