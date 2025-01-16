import pandas as pd
import numpy as np
import pytest
import seaborn as sns
from data_handler.merge_low_frequency import MergeStrategy
from analyze_data.analyze_package import DataInspector

@pytest.fixture
def sample_df():
    return pd.read_csv('sample_data/train.csv')

@pytest.fixture
def sample_columns(sample_df):
    data_inspector = DataInspector()
    return data_inspector.get_columns(sample_df)

def test_checker(sample_df, sample_columns):

    result_dict = MergeStrategy.check(sample_df, sample_columns['categorical'])

def test_handler(sample_df, sample_columns):

    handler = MergeStrategy()
    new_df = handler.handle(sample_df, sample_columns['categorical'])
    for feature in sample_columns['categorical']:
        print(new_df[feature].unique())


