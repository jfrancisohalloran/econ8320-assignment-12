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

    def testAdjectives(self):
        adjectives = global_namespace.get('adjectives', None)
        self.assertIsNotNone(adjectives, "Variable 'adjectives' is not defined.")
        df = isinstance(adjectives, pd.Series) or isinstance(adjectives, pd.DataFrame)
        length = len(adjectives) == 20
        self.assertTrue(df and length, "Adjectives should be a DataFrame or Series with 20 entries.")
