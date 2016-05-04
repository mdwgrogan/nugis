""" An example to see how test runners are working in CircleCI
"""
import unittest


class TestExample(unittest.TestCase):
    def setUp(self):
        pass

    def test_a_failure(self):
        self.assertFalse(True)


if __name__ == '__main__':
    unittest.main()
