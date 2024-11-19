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

    def testNamesProperNouns(self):
        #Checking names for only proper nouns
        typelist = isinstance(names, list)
        print(f"typelist")
        test = True
        for i in names:
            print(i)
            if (str(i).lower()==i) | (len(str(i).split(" "))>2):
                test = False
        self.assertTrue(test)