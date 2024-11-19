import unittest
import json
import pandas as pd


with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-exercise" in j:
            exec(compile("".join(i['source']), '<string>', 'exec'))


# todo: replace this with an actual test
class TestCase(unittest.TestCase):

    def testBarChart(self):
        self.assertTrue(any(['Bar' in str(type(i)) for i in fig.data]), "Your plot should be a bar chart using the plotly library.")
