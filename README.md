# Snaketree
Poor man's python implementation of the tree command which I missed on Windows.

# Initial setup
You only have to do this once:
`python -m venv myvenv`

Then you can install the dependencies:
`venv/Scripts/activate`.

If you need to (re-install dependencies):
`pip install -r requirements.txt`

# Usage
Currently only executed as direct python script.
`python app.py`

You can configure the level of depth of course.
`python app.py --L=3`

Ask for help:
`python app.py -h`

Run the tests:
`python -m unittest -v test_tree`