import unittest
from app import bar, foo


class TestApp(unittest.TestCase):

    def test_foo(self):
        self.assertEqual(foo(), "This demo")

    def test_bar(self):
        self.assertEqual(bar(), "This demo, probably won't run")


unittest.main()
