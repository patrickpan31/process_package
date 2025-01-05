import pandas as pd
import numpy as np
import pytest
import seaborn as sns
from data_handler.data_transformation import LogTransformation
from analyze_data.analyze_package import DataInspector
from uni_variate_analysis.uni_variate_analysis import NumericUniAnalysis

@pytest.fixture
def sample_df():
    return pd.read_csv('sample_data/train.csv')

@pytest.fixture
def sample_columns(sample_df):

    data_inspector = DataInspector()
    return data_inspector.get_columns(sample_df)

@pytest.fixture
def sample_df_small():
    data = {
        'A': [1, np.nan, np.nan,4],
        'B': [4, np.nan, 6, 8],
        'C': [7, 10, np.nan, 11]
    }
    df = pd.DataFrame(data)
    return df

def test_logtransformation(sample_df_small: pd.DataFrame, sample_columns: dict, sample_df:pd.DataFrame):
    '''
    Testing function for LogTransformation()
    :param sample_df_small (pd.DataFrame): Sample testing data frame
    :param sample_columns (Dict): dictionary for numeric columns and categorical columns
    :return:
    '''
    transformer = LogTransformation(['A','B','C'])
    new_df = transformer.transform(sample_df_small)
    print(sample_df_small)
    print(new_df)
    analyzer = NumericUniAnalysis()
    analyzer.analyze(sample_df, 'SalePrice')
    transformer = LogTransformation(['SalePrice'])
    new_df = transformer.transform(sample_df)
    analyzer.analyze(new_df, 'SalePrice')
