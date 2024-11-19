import unittest
import json
import pandas


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

    def testAdjectives(self):
        #Checking adjectives list
        df = isinstance(adjectives, pandas.core.series.Series) | isinstance(adjectives, pandas.core.frame.DataFrame)
        length = len(adjectives)==20
        self.assertTrue(df & length)