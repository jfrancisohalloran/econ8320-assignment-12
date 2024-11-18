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

    def testSentences(self):
        sentences = global_namespace.get('sentences', None)
        self.assertIsNotNone(sentences, "Variable 'sentences' is not defined.")
        self.assertIsInstance(sentences, int, "'sentences' should be an integer.")
        lengthsent = -5 <= (sentences - 125) <= 5
        self.assertTrue(lengthsent, "The number of sentences should be close to 125.")
