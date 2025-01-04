import pandas as pd
import numpy as np
import pytest
import seaborn as sns
from bi_variate.bi_variate_analysis import Bi_Variate_Analyzer, NumericvsNumericStrategy, NumericvsCategoricalStrategy
from analyze_data.analyze_package import DataInspector

@pytest.fixture
def sample_df():
    return pd.read_csv('sample_data/train.csv')

@pytest.fixture
def sample_columns(sample_df):

    data_inspector = DataInspector()
    return data_inspector.get_columns(sample_df)

def test_numericvsnumeric(sample_df: pd.DataFrame, sample_columns:dict):
    '''
    Test function NumericvsNumericStrategy
    :param sample_df (pd.DataFrame): Sample Testing Data Frame
    :param sample_columns (dic) : sample dictionary
    :return:
    '''
    analyzer = Bi_Variate_Analyzer(NumericvsNumericStrategy())
    target = 'SalePrice'
    for col in sample_columns['numeric'][:5]:
        analyzer.analyze(col, target, sample_df)

def test_numericvscategorical(sample_df: pd.DataFrame, sample_columns:dict):
    '''
    Test function NumericvsCategoricalStrategy
    :param sample_df (pd.DataFrame): Sample Testing Data Frame
    :param sample_columns (dic) : sample dictionary
    :return:
    '''
    analyzer = Bi_Variate_Analyzer(NumericvsCategoricalStrategy())
    target = 'SalePrice'
    analyzer.analyze('OverallQual', target, sample_df)
    for col in sample_columns['categorical'][:5]:
        analyzer.analyze(col, target, sample_df)
