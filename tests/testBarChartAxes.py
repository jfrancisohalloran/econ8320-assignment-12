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

    def testBarChartAxes(self):
        fig = global_namespace.get('fig', None)
        self.assertIsNotNone(fig, "Variable 'fig' is not defined.")
        x_data = fig.data[0]['x']
        y_data = fig.data[0]['y']
        x_is_adjectives = all(isinstance(i, str) for i in x_data) and len(x_data) == 20
        y_is_adjectives = all(isinstance(i, str) for i in y_data) and len(y_data) == 20
        self.assertTrue(x_is_adjectives or y_is_adjectives, "Your bar chart should use the adjectives from the text as one of the axes.")
