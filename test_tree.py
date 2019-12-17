import unittest
import tree

class TestTreeModule(unittest.TestCase):

    def test_bold(self):
        expected = '\033[1m' + "hello" + '\033[0m'
        result = tree.bold("hello")
        self.assertEqual(expected, result)

    def test_format_file_entry(self):
        path_name = "test_tree.cpython-38.pyc"
        expected = "-- test_tree.cpython-38.pyc 2"
        result = tree.format_path_entry(path_name, 2)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()