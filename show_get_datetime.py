# Option 1
>>> import datetime
>>> datetime.datetime.now()
datetime(2009, 1, 6, 15, 8, 24, 78915)
And just the time:

>>> datetime.datetime.time(datetime.datetime.now())
datetime.time(15, 8, 24, 78915)
The same but slightly more compact:

>>> datetime.datetime.now().time()
See the documentation for more info.

To save typing, you can import the datetime object from the datetime module:

>>> from datetime import datetime
Then remove the leading datetime. from all the above.

harley-holcombe @ stackoverflow
edited by matt  @ stackoverflow

-----------------------------------

# Option 2
>>> from time import gmtime, strftime
>>> strftime("%Y-%m-%d %H:%M:%S", gmtime())
'2009-01-05 22:14:39'

ray-vega @ stackoverflow
