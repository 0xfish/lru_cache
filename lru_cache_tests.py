"""
LRU Cache data structure unit tests.

"""
from lru_cache_ds import lru_cache
import unittest

class TestStringMethods(unittest.TestCase):

    def test_negative(self):
        self.assertRaises(AssertionError, lru_cache, -1)
    def test_non_integer(self):
        self.assertRaises(AssertionError, lru_cache, 10.5)
    def test_simple_integer(self):
        DUT = lru_cache(1)
        DUT.put(1,1)
        self.assertEqual(DUT.get(1), 1)
    def test_simple_string(self):
        DUT = lru_cache(1)
        DUT.put("test","test")
        self.assertEqual(DUT.get("test"), "test")
    def test_simple_class(self):
        class test:
            x = 1
        a, b = test(), test()
        DUT = lru_cache(1)
        DUT.put(a,b)
        self.assertEqual(DUT.get(a), b)
    def test_simple_get_set_integer(self):
        DUT = lru_cache(2)
        DUT.put(1,1)
        DUT.put(2,2)
        self.assertEqual(DUT.get(1), 1)
        DUT.put(3,3)
        self.assertRaises(AssertionError, DUT.get, 2)
        DUT.put(4,4)
        self.assertRaises(AssertionError, DUT.get, 1)
        self.assertEqual(DUT.get(3), 3)
        self.assertEqual(DUT.get(4), 4)
    def test_duplicate_get_set_integer(self):
        DUT = lru_cache(2)
        DUT.put(1,1)
        DUT.put(2,2)
        self.assertEqual(DUT.get(1), 1)
        DUT.put(2,3)
        self.assertEqual(DUT.get(1), 1)
        self.assertEqual(DUT.get(2), 3)
        DUT.put(3,3)
        self.assertRaises(AssertionError, DUT.get, 1)
        DUT.put(4,4)
        self.assertRaises(AssertionError, DUT.get, 1)
        self.assertEqual(DUT.get(3), 3)
        self.assertEqual(DUT.get(4), 4)
    def test_large_cache(self):
        DUT = lru_cache(1000000)
        for i in range(1000000):
            DUT.put(i,i)
        for i in range(1000000):
            self.assertEqual(DUT.get(i), i)
    def test_large_cache_II(self):
        DUT = lru_cache(1000000)
        for i in range(1000000):
            DUT.put(i,i)
        DUT.put(1000000 + 1, 1000000 + 1)
        self.assertRaises(AssertionError, DUT.get, 0)
    def test_mix_type(self):
        DUT = lru_cache(2)
        DUT.put("test", "test")
        DUT.put(1,1)
        self.assertEqual(DUT.get("test"), "test")
        self.assertEqual(DUT.get(1), 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)