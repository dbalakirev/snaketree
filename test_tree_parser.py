import unittest
import tree_parser
import tempfile

class TestTreeParserModule(unittest.TestCase):

    def test_bold(self):
        root_dir = dict()
        project_dir = dict()
        project_dir['file.txt'] = 'file.txt'
        root_dir['.vscode'] = project_dir
        root_dir['settings.json'] = 'settings.json'
        expected = """.
├── .vscode
│   └── file.txt
└── settings.json"""
        result = tree_parser.tree_to_string(root_dir)
        self.assertEqual(expected, result)
# └ ├ ─ │