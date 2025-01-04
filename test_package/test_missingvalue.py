import pandas as pd
import numpy as np
import pytest
import seaborn as sns
from missing_value.missing_value_analysis import SimpleMissingAnalyzer


@pytest.fixture
def sample_df():
    return pd.read_csv('sample_data/train.csv')

def test_missvalueanalysis(sample_df):
    '''
    Testing function to test the missing value analysis function

    :param sample_df (pd.DataFrame): sample data for testing
    :return: None
    '''

    missing_analyer = SimpleMissingAnalyzer()
    print(missing_analyer.analyze(sample_df))