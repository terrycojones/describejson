describejson
============

Feed the `describejson.py` script some JSON on stdin and it will print a
summary of the structure of the JSON.

The only option is `--strictness` to determine how strictly JSON objects
and lists should be compared.  In order of increasing strictness, the
possible values are:

 - `type`: compare everything by type only.
 - `length`: compare lists and objects by length.
 - `keys`: compare lists by equality, objects by keys.
 - `equal`: compare objects and list by equality.

Strictness affects the amount of output you'll see. For example if a list
contains two lists, `describejson.py` will just tell you that very
concisely if you use `--strictness type`. If you want the fact that things
differ in length or contents, use a higher strictness level.

```
Terry Jones (terry@fluidinfo.com)
Aug 9, 2012
```
