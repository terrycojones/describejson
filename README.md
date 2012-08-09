describejson
============

Feed the `describejson.py` script some JSON on stdin and it will print a
summary of the structure of the JSON.

The only option is `--strictness` to determine how strictly JSON objects
and lists should be compared.  Possible values are:

 - `type`: compare by type only.
 - `length`: compare by length.
 - `keys`: lists by equality, dicts by keys.
 - `equal`: dicts and list by equality.

Terry Jones
terry@jon.es
Aug 9, 2012
