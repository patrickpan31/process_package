import pandas as pd
import numpy as np
import pytest
from analyze_data.analyze_package import DataTypeStrategy, SummaryStatisticStrategy, DataInspector

@pytest.fixture
def sample_df():
    return pd.read_csv('sample_data/train.csv')

def test_data_type_strategy(sample_df):
    '''
    Testing function for the DataTypeStrategy()

    :param sample_df (pd.DataFrame) : sample dataframe used to test the DataTypeStrategy()

    :return:
    '''
    datatype_analyzer = DataTypeStrategy()
    datatype_analyzer.inspect_data(sample_df)
    numeric_columns = datatype_analyzer.get_numeric_columns(sample_df)
    categorical_columns = datatype_analyzer.get_categorical_columns(sample_df)
    assert numeric_columns
    assert categorical_columns
    assert (len(numeric_columns) + len(categorical_columns)) == len(sample_df.columns.to_list())

def test_summary_statistic_strategy(sample_df):
    '''
    Testing function for the SummaryStatisticStrategy()

    :param sample_df (pd.DataFrame) : sample dataframe used to test the SummaryStatisticStrategy()

    :return:
    '''
    summary_analyzer = SummaryStatisticStrategy()

    print(summary_analyzer.inspect_data(sample_df))

def test_datainspector(sample_df):
    '''
    Testing function for the DataInspector()

    :param sample_df (pd.DataFrame) : sample dataframe used to test the SummaryStatisticStrategy()

    :return: Analysis results based on strategy
    '''
    data_inspector = DataInspector(DataTypeStrategy())
    data_inspector.analyze(sample_df)
    columns_dict = data_inspector.get_columns(sample_df)
    assert isinstance(columns_dict, dict)
    assert ('numeric' in columns_dict)
    assert ('categorical' in columns_dict)




