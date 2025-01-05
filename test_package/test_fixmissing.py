from cgitb import handler

import pandas as pd
import numpy as np
import pytest
import seaborn as sns
from data_handler.missing_value_fix import Drop_Strategy, Fill_Strategy, Missing_Value_Handler
from analyze_data.analyze_package import DataInspector

@pytest.fixture
def sample_df():
    return pd.read_csv('sample_data/train.csv')

@pytest.fixture
def sample_df_small():
    data = {
        'A': [1, np.nan, np.nan,4],
        'B': [4, np.nan, 6, 8],
        'C': [7, 10, np.nan, 11]
    }
    df = pd.DataFrame(data)
    return df

@pytest.fixture
def sample_columns(sample_df):

    data_inspector = DataInspector()
    return data_inspector.get_columns(sample_df)

def test_drop_missing(sample_df_small):
    '''
    Testing function to test Drop_Strategy
    :param sample_df_small (pd.DataFrame): Testing DataFrame
    :return: None
    '''
    handler = Drop_Strategy()
    new_df = handler.handle(sample_df_small)
    diff = sample_df_small.dropna(axis=0)
    print(sample_df_small)
    assert diff.equals(new_df)
    print(new_df)

def test_fillstrategy(sample_df_small):
    '''
    Testing function to test Fill_Strategy
    :param sample_df_small (pd.DataFrame): Testing DataFrame
    :return: None
    '''
    handler = Fill_Strategy()
    new_df = handler.handle(sample_df_small)
    print(new_df)
    handler.set_method('constant')
    handler.set_value(3)
    new_df = handler.handle(sample_df_small)

    print(new_df)

def testing_missinghandler(sample_df_small):
    '''
    Testing function to test Missing_Value_Handler
    :param sample_df_small (pd.DataFrame): Testing DataFrame
    :return: None
    '''
    handler = Missing_Value_Handler()
    new_df = handler.process(sample_df_small)
    print(new_df)
    handler.set_strategy(Drop_Strategy())
    new_df = handler.process(sample_df_small)
    print(new_df)
    handler.set_strategy(Fill_Strategy())
    handler.set_method('constant')
    handler.set_value(3)
    new_df = handler.process(sample_df_small)
    print(new_df)
    handler.set_method('median')
    handler.set_value(3)
    new_df = handler.process(sample_df_small)
    print(new_df)