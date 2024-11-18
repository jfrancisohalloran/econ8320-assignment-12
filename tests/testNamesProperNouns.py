import unittest
import json
import pandas as pd

with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type'] == 'code']

global_namespace = {}

for cell in code:
    source = "".join(cell['source'])
    if "#si-exercise" in source:
        exec(compile(source, '<string>', 'exec'), global_namespace)

class TestCase(unittest.TestCase):

    def testNamesProperNouns(self):
        names = global_namespace.get('names', None)
        self.assertIsNotNone(names, "Variable 'names' is not defined.")
        self.assertIsInstance(names, list, "'names' should be a list.")
        test = True
        for i in names:
            if (str(i).lower() == i) or (len(str(i).split(" ")) > 2):
                test = False
                break
        self.assertTrue(test, "All names should be proper nouns (capitalized and not multi-word).")
