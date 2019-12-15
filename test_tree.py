import unittest
import tree

class TestTreeModule(unittest.TestCase):

    def test_bold(self):
        expected = '\033[1m' + "hello" + '\033[0m'
        result = tree.bold("hello")
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()