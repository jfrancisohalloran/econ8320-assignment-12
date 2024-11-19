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

    def testBarChartAxes(self):
        self.assertTrue((all([isinstance(i, str) for i in fig.data[0]['y']]) and len(fig.data[0]['y'])==20) or (all([isinstance(i, str) for i in fig.data[0]['x']]) and len(fig.data[0]['x'])==20), "Your bar chart should use the adjectives from the text as one of the axes.")