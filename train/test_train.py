from unittest import TestCase
import pandas as pd
from train import clean_data

class TestTrain(TestCase):
    def clean_data_test(self):
        df = pd.dataFrame({
        'survived': [1, 0, 1],
        'pclass': [2, 3, 1],
        'sex': ['male', 'male', 'male'],
        'age': [15, 64, 32]
        })

        result_df = clean_data(df)

        self.assertEqual(result_df.shape[0], second=3)
        self.assertEqual(result_df['sex'][0], second=3)