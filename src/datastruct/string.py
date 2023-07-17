import unittest


class String(unittest.TestCase):

    def test_method(self):
        s = "hello World"
        print(s.title())
        print(s.upper())
        print(s.lower())
        print(s.rstrip())
        print()
        self.assertEqual(True, True)

    def test_format(self):
        s = "hello {name}"
        print(s.format(name="world"))

        place = """world"""
        print(f"hello {place}")
        self.assertEqual(True, True)
