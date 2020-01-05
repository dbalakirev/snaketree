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
        expected = {}
        result = tree.process_files("","", indent_level = 2, maximum_depth = 2)
        self.assertEqual(expected, result)

    def test_process_files(self):
        parent = tempfile.mkdtemp()
        sub1 = tempfile.mkdtemp(dir=parent)
        sub2 = tempfile.mkdtemp(dir=parent)
        lowsub1 = tempfile.mkdtemp(dir=sub2)
        tempfile.mkstemp(dir=sub1)[1]
        tempfile.mkstemp(dir=sub2)[1]
        tempfile.mkstemp(dir=lowsub1)[1]
        result = tree.process_files(parent, parent, 0, 3)
        def find_results(result):
            found_directories = 0
            found_files = 0
            for key in result:
                value = result[key]
                if (type(value) is dict):
                    files = find_results(value)
                    found_directories += files[0]
                    found_files += files[1]
                    found_directories += 1
                else:
                    found_files += 1
            return (found_directories, found_files)
        files = find_results(result)
        found_directories = files[0]
        found_files = files[1]
        self.assertEqual(3, found_directories)
        self.assertEqual(3, found_files)

if __name__ == '__main__':
    unittest.main()