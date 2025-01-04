import pandas as pd
import numpy as np
import pytest
import seaborn as sns
from uni_variate_analysis.uni_variate_analysis import Uni_Variate_Analyzer, NumericUniAnalysis, CategoricalUniAnalysis
from analyze_data.analyze_package import DataInspector

@pytest.fixture
def sample_df():
    return pd.read_csv('sample_data/train.csv')

@pytest.fixture
def sample_columns(sample_df):

    data_inspector = DataInspector()
    return data_inspector.get_columns(sample_df)

def test_numericunivariate(sample_df, sample_columns):
    '''
    Testing function for NumericUniAnalysis()
    :param sample_df: Testing Sample Data
    :return: None
    '''
    analyzer = Uni_Variate_Analyzer(NumericUniAnalysis())
    col_dict = sample_columns
    for col in col_dict['numeric'][:5]:
        analyzer.analyze(sample_df, col)

def test_categoricalcunivariate(sample_df, sample_columns):
    '''
    Testing function for CategoricalUniAnalysis()
    :param sample_df: Testing Sample Data
    :return: None
    '''
    analyzer = Uni_Variate_Analyzer(CategoricalUniAnalysis())
    col_dict = sample_columns
    for col in col_dict['categorical'][:5]:
        analyzer.analyze(sample_df, col)