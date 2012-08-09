describejson
============

Feed the `describejson.py` script some JSON on stdin and it will print a
concise summary of the structure of the JSON.

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

The output could probably be more verbose / helpful in some cases, but it's
a difficult thing to get right, and the point is to produce a small summary
omitting as much detail as possible.

Here's an example summarizing a 24M JSON file:

```
$ python describejson.py < sample.json 
1 dict of length 3. Values:
  1 int
  1 dict of length 4. Values:
    1 list of length 17993. Values:
      17993 dicts of length 5. Values:
        1 unicode
        1 int
        1 list of length 0.
        2 unicodes
    1 list of length 0.
    1 list of length 11907. Values:
      11907 dicts of length 5. Values:
        1 unicode
        1 int
        1 list of length 1. Values:
          1 unicode
        2 unicodes
    1 list of length 28068. Values:
      28068 dicts of length 5. Values:
        1 unicode
        1 int
        1 list of length 0.
        2 unicodes
  1 unicode
```

That's a 24 line summary of a 24M JSON file :-) Looking at the same file
with `python -m json.tool` produces almost half a million lines of output.


```
Terry Jones (terry@fluidinfo.com)
Aug 9, 2012
```
