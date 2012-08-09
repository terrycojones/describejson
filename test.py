from unittest import TestCase
from describejson import JsonItem


class TestDescribeJson(TestCase):
    """
    Tests for the JsonItem class.
    """
    def testEmptyList(self):
        item = JsonItem([])
        self.assertEqual("1 list of length 0.",
                         item.__str__())

    def testListWithOneInt(self):
        item = JsonItem([4])
        self.assertEqual("1 list of length 1. Values:\n  1 int",
                         item.__str__())

    def testListWithOneDict(self):
        item = JsonItem([{}])
        self.assertEqual("1 list of length 1. Values:\n  1 dict of length 0.",
                         item.__str__())

    def testListWithAnEmptyList(self):
        item = JsonItem([[]])
        self.assertEqual("1 list of length 1. Values:\n  1 list of length 0.",
                         item.__str__())

    def testListWithAListWithAnInt(self):
        item = JsonItem([[4]])
        self.assertEqual('\n'.join(["1 list of length 1. Values:",
                                    "  1 list of length 1. Values:",
                                    "    1 int"]),
                         item.__str__())

    def testListWithOneDictAndOneInt(self):
        item = JsonItem([{}, 4])
        self.assertEqual('\n'.join(["1 list of length 2. Values:",
                                    "  1 dict of length 0.",
                                    "  1 int"]),
                         item.__str__())

    def testListWithTwoInts(self):
        item = JsonItem([4, 5])
        self.assertEqual("1 list of length 2. Values:\n  2 ints",
                         item.__str__())

    def testListWithTwoUnequalListsTypeCompare(self):
        item = JsonItem([[4, 5], [6]], strictness='type')
        self.assertEqual('\n'.join(["1 list of length 2. Values:",
                                    "  2 lists of length 2. Values:",
                                    "    2 ints"]),
                         item.__str__())

    def testListWithTwoUnequalListsLengthCompare(self):
        item = JsonItem([[4, 5], [6, 7]], strictness='length')
        self.assertEqual('\n'.join(["1 list of length 2. Values:",
                                    "  2 lists of length 2. Values:",
                                    "    2 ints"]),
                         item.__str__())

    def testListWithTwoUnequalListsKeysCompare(self):
        item = JsonItem([[4, 5], [6, 7]], strictness='keys')
        self.assertEqual('\n'.join(["1 list of length 2. Values:",
                                    "  1 list of length 2. Values:",
                                    "    2 ints",
                                    "  1 list of length 2. Values:",
                                    "    2 ints"]),
                         item.__str__())

    def testListWithTwoEqualListsKeysCompare(self):
        item = JsonItem([[4, 5], [4, 5]], strictness='keys')
        self.assertEqual('\n'.join(["1 list of length 2. Values:",
                                    "  2 lists of length 2. Values:",
                                    "    2 ints"]),
                         item.__str__())

    def testListWithTwoEqualListsEqualCompare(self):
        item = JsonItem([[4, 5], [4, 5]], strictness='equal')
        self.assertEqual('\n'.join(["1 list of length 2. Values:",
                                    "  2 lists of length 2. Values:",
                                    "    2 ints"]),
                         item.__str__())

    def testEmptyDict(self):
        item = JsonItem({})
        self.assertEqual("1 dict of length 0.",
                         item.__str__())

    def testDictWithOneStrKey(self):
        item = JsonItem({'x': u'y'})
        self.assertEqual("1 dict of length 1. Values:\n  1 unicode",
                         item.__str__())

    def testDictWithTwoStrKeys(self):
        item = JsonItem({'a': u'b', 'c': u'd'})
        self.assertEqual("1 dict of length 2. Values:\n  2 unicodes",
                         item.__str__())

    def testDictWithOneIntKey(self):
        item = JsonItem({'x': 4})
        self.assertEqual("1 dict of length 1. Values:\n  1 int",
                         item.__str__())

    def testDictWithOneEmptyDictKey(self):
        item = JsonItem({'a': {}})
        self.assertEqual("1 dict of length 1. Values:\n  1 dict of length 0.",
                         item.__str__())

    def testDictWithOneEmptyListKey(self):
        item = JsonItem({'a': []})
        self.assertEqual("1 dict of length 1. Values:\n  1 list of length 0.",
                         item.__str__())

    def testDictWithOneFloatKey(self):
        item = JsonItem({'a': 4.3})
        self.assertEqual("1 dict of length 1. Values:\n  1 float",
                         item.__str__())

    def testDictWithOneBooleanKey(self):
        item = JsonItem({'a': True})
        self.assertEqual("1 dict of length 1. Values:\n  1 boolean",
                         item.__str__())

    def testDictWithOneNoneKey(self):
        item = JsonItem({'a': None})
        self.assertEqual("1 dict of length 1. Values:\n  1 None",
                         item.__str__())

    def testDictWithOneLongKey(self):
        item = JsonItem({'a': 100L})
        self.assertEqual("1 dict of length 1. Values:\n  1 long",
                         item.__str__())

    def testDictWithOneUnicodeKey(self):
        item = JsonItem({'a': u'xxx'})
        self.assertEqual("1 dict of length 1. Values:\n  1 unicode",
                         item.__str__())

    def testListWithTwoUnequalDictsTypeCompare(self):
        item = JsonItem([{'a': 3}, {'b': 4}], strictness='type')
        self.assertEqual('\n'.join(["1 list of length 2. Values:",
                                    "  2 dicts of length 1. Values:",
                                    "    1 int"]),
                         item.__str__())

    def testListWithTwoSameLengthDictsLengthCompare(self):
        item = JsonItem([{'a': 3}, {'b': 4}], strictness='length')
        self.assertEqual('\n'.join(["1 list of length 2. Values:",
                                    "  2 dicts of length 1. Values:",
                                    "    1 int"]),
                         item.__str__())

    def testListWithTwoDifferentLengthDictsLengthCompare(self):
        item = JsonItem([{'a': 3}, {'b': 4, 'c': 5}], strictness='length')
        self.assertEqual('\n'.join(["1 list of length 2. Values:",
                                    "  1 dict of length 1. Values:",
                                    "    1 int",
                                    "  1 dict of length 2. Values:",
                                    "    2 ints"]),
                         item.__str__())

    def testListWithTwoDifferentDictsEqualCompare(self):
        item = JsonItem([{'a': 3, 'b': 4}, {'a': 3, 'b': 6}],
                        strictness='equal')
        self.assertEqual('\n'.join(["1 list of length 2. Values:",
                                    "  1 dict of length 2. Values:",
                                    "    2 ints",
                                    "  1 dict of length 2. Values:",
                                    "    2 ints"]),
                         item.__str__())

    def testListWithTwoEqualDictsEqualCompare(self):
        item = JsonItem([{'a': 3, 'b': 4}, {'a': 3, 'b': 4}],
                        strictness='equal')
        self.assertEqual('\n'.join(["1 list of length 2. Values:",
                                    "  2 dicts of length 2. Values:",
                                    "    2 ints"]),
                         item.__str__())

    def testInt(self):
        item = JsonItem(4)
        self.assertEqual("1 int",
                         item.__str__())


if __name__ == '__main__':
    import unittest
    unittest.main()
