import pandas as pd
import numpy as np
import pytest
import seaborn as sns
from multi_variate.multivariate_analysis import SimpleMultivariateStrategy
from analyze_data.analyze_package import DataInspector

@pytest.fixture
def sample_df():
    return pd.read_csv('sample_data/train.csv')

@pytest.fixture
def sample_columns(sample_df):

    data_inspector = DataInspector()
    return data_inspector.get_columns(sample_df)

def test_simplemulti(sample_df, sample_columns):
    '''
    Testing function for SimpleMultivariateStrategy()
    :param sample_df: Testing Sample Data
    :return: None
    '''
    analyzer = SimpleMultivariateStrategy()
    analyzer.analyze(sample_df[['SalePrice','OverallQual', 'GrLivArea',  'GarageArea', 'YearBuilt', 'TotalBsmtSF']])