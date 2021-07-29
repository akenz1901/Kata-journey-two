import unittest
from kata import duplicateEliminator


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_duplicate(self):
        self.assertEqual(duplicateEliminator.removeDuplicate(), [0, 1, 2, 3, 4])