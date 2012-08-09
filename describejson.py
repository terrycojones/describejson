#!/usr/bin/env python

from types import (
    BooleanType, DictType, FloatType, IntType, ListType, LongType, NoneType,
    UnicodeType)

_typeToString = {
    BooleanType: 'boolean',
    DictType: 'dict',
    FloatType: 'float',
    IntType: 'int',
    ListType: 'list',
    LongType: 'long',
    NoneType: 'None',
    UnicodeType: 'unicode',
}


class JsonItem(object):
    DEFAULT_STRICTNESS = 'length'

    def __init__(self, item, indent=0, strictness=None):
        self._strictness = strictness or self.DEFAULT_STRICTNESS
        self._compare = getattr(self, '_eq_%s' % self._strictness)
        self._indent = indent
        self._duplications = 1
        self._type = type(item)
        if self._type == DictType:
            self._len = len(item)
            if strictness == 'keys':
                self._keys = sorted(item.keys())
            elif strictness == 'equal':
                self._item = item
            self._summarize(item.itervalues())
        elif self._type == ListType:
            self._len = len(item)
            if strictness in ('keys', 'equal'):
                self._item = item
            self._summarize(item)

    def _summarize(self, items):
        self._contents = []
        for i, item in enumerate(items):
            jsonItem = JsonItem(item, self._indent + 2, self._strictness)
            if i == 0:
                self._contents.append(jsonItem)
            else:
                if self._contents[-1] == jsonItem:
                    self._contents[-1]._duplications += 1
                else:
                    self._contents.append(jsonItem)

    def __eq__(self, other):
        return self._compare(other)

    def _eq_type(self, other):
        """Equality only according to item type."""
        return self._type == other._type

    def _eq_length(self, other):
        """Dicts and lists must have the same number of keys."""
        if self._type == other._type:
            if self._type == DictType or self._type == ListType:
                return self._len == other._len
            else:
                return True
        else:
            return False

    def _eq_keys(self, other):
        """Lists must be equal, dicts must have the same keys."""
        if self._type == other._type:
            if self._type == ListType:
                return self._item == other._item
            elif self._type == DictType:
                return self._keys == other._keys
            else:
                return True
        else:
            return False

    def _eq_equal(self, other):
        """Lists and dicts must be equal."""
        if self._type == other._type:
            if self._type == ListType:
                return self._item == other._item
            elif self._type == DictType:
                return self._item == other._item
            else:
                return True
        else:
            return False

    def _strList(self):
        prefix = '%s%s %s%s' % (
            self._indent * ' ', self._duplications, _typeToString[self._type],
            '' if self._duplications == 1 else 's')
        if self._type in (DictType, ListType):
            result = ['%s of length %d.%s' % (
                prefix, self._len, ' Values:' if self._len else '')]
            for item in self._contents:
                result.extend(item._strList())
        else:
            result = [prefix]
        return result

    def __str__(self):
        return '\n'.join(self._strList())


if __name__ == '__main__':
    from json import loads
    import optparse
    import sys

    opts = optparse.OptionParser()
    opts.add_option('-s', '--strictness', default=JsonItem.DEFAULT_STRICTNESS,
                    help=("How strictly to compare dicts and lists to "
                          "each other. Possible values are 'type': by type "
                          "only. 'length': by length. 'keys': lists by "
                          "equality, dicts by keys. 'equal': dicts and list "
                          "by equality. (default is '%default')."))
    args, opt = opts.parse_args()

    if args.strictness not in ('type', 'length', 'keys', 'equal'):
        print >>sys.stderr, 'Unknown strictness argument value.'
        sys.stdout = sys.stderr
        opts.print_help()
        sys.exit(1)

    try:
        j = loads(sys.stdin.read())
    except ValueError, e:
        print >>sys.stderr, 'Could not load JSON object from stdin.'
        sys.exit(1)

    print JsonItem(j, indent=0, strictness=args.strictness)
