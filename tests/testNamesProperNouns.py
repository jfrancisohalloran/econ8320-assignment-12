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

class TestCase(unittest.TestCase):

    def testNamesProperNouns(self):
        typelist = isinstance(names, list)
        print(f"typelist: {typelist}")
        test = typelist and len(names) > 0

        for i in names:
            print("Checking types in 'names':")
            print(f"{i}: {type(i)}")
            if str(i).lower() == i or len(str(i).split(" ")) > 2:
                test = False
                print(f"Invalid name found: {i}")
        self.assertTrue(test)
