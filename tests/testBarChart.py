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

    def testBarChart(self):
        fig = global_namespace.get('fig', None)
        self.assertIsNotNone(fig, "Variable 'fig' is not defined.")
        self.assertTrue(any(['Bar' in str(type(i)) for i in fig.data]), "Your plot should be a bar chart using the Plotly library.")
