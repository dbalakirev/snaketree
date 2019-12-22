import unittest
import tree
import tempfile

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

    def test_process_files_respects_depth(self):
        expected = (0,0)
        result = tree.process_files("","", indent_level = 2, maximum_depth = 2)
        self.assertEqual(expected, result)

    def test_process_files(self):
        parent = tempfile.mkdtemp()
        sub1 = tempfile.mkdtemp(dir=parent)
        sub2 = tempfile.mkdtemp(dir=parent)
        lowsub1 = tempfile.mkdtemp(dir=sub2)
        tempfile.mkstemp(dir=sub1)
        tempfile.mkstemp(dir=sub2)
        tempfile.mkstemp(dir=lowsub1)
        result = tree.process_files(parent, parent, 0, 3)
        expected = (3,3)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()