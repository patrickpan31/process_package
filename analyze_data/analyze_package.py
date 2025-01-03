import pandas as pd
import numpy as np
from abc import ABC, abstractmethod

class Analysis_Strategy_Base(ABC):
    '''
    base class for all the data frame analysis method
    '''

    @abstractmethod
    def inspect_data(self, df: pd.DataFrame):
        '''
        General method in this class to perform specific analysis strategy

        :param df (pd.DataFrame): data frame to be analyzed

        :return: Based on strategy
        '''
        pass

class DataTypeStrategy(Analysis_Strategy_Base):
    '''
    Stategy used to analyze the data frame data type
    '''
    def inspect_data(self, df: pd.DataFrame):
        print("Starting Analyzing the data type and null value information")
        print(df.info())
        numeric_column = df.select_dtypes('number').columns.to_list()
        print(f'Numeric columns: {numeric_column}')
        categorical_column = df.select_dtypes('object').columns.to_list()
        print(f'Categorical columns: {categorical_column}')
        print('Analysis finished')

    def get_numeric_columns(self, df: pd.DataFrame) -> list:
        '''
        function to retrieve the numeric columns in the data frame

        :param df (pd.DataFrame) : target data frame

        :return (list): List of numeric columns
        '''
        return df.select_dtypes('number').columns.to_list()

    def get_categorical_columns(self, df: pd.DataFrame) -> list:
        '''
        function to retrieve the categorical columns in the data frame

        :param df (pd.DataFrame) : target dataframe

        :return (list): List of categorical columns
        '''

        return df.select_dtypes('object').columns.to_list()

class SummaryStatisticStrategy(Analysis_Strategy_Base):
    '''
    Class for getting the columns summary statistics
    '''

    def inspect_data(self, df: pd.DataFrame):
        '''
        Main function for the current strategy

        :param df (pd.DataFrame) : target dataframe

        :return (summary str): summary statistics for the target table
        '''

        print("Summary statistics for numeric columns: ")
        print(df.describe())
        print("Summary statistics for categorical columns: ")
        print(df.describe(include=['O']))


class DataInspector():
    '''
    Collection class that unified all the data analysis strategy for ease of usage
    '''
    def __init__(self, strategy: Analysis_Strategy_Base = DataTypeStrategy()) -> None:
        '''
        Initialize the DataInspector with the default strategy DataTypeStrategy
        :param strategy (Analysis_Strategy_Base): Strategy wants to use to analyze the data
        '''
        self._strategy = strategy

    def set_strategy(self, strategy = Analysis_Strategy_Base) -> None:
        '''
        Function use to switch between different analysis strategy

        :param strategy (Analysis_Strategy_Base): Strategy wants to use to analyze the data

        :return: None
        '''

        self._strategy = strategy

    def analyze(self, df: pd.DataFrame) -> None:
        '''
        Perform the analysis based on the defined strategy

        :param df (pd.DataFrame) : Data to be analyzed

        :return: Strategy analysis results
        '''
        self._strategy.inspect_data(df)

    def get_columns(self, df: pd.DataFrame) -> dict:
        '''
        Additional function used to get the numeric columns or the categorical columns
        Only valid for DataTypeStrategy()

        :param df (pd.DataFrame) : Data to be analyzed

        :return: dictionary containing numeric columns and categorical columns
        '''
        if self._strategy != DataTypeStrategy():
            self._strategy = DataTypeStrategy()

        try:
            return {'numeric': self._strategy.get_numeric_columns(df),
                    'categorical': self._strategy.get_categorical_columns(df)}
        except Exception as e:
            raise IOError("Failed to extract different types of columns")