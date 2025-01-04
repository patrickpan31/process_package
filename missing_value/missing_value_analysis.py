import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from abc import ABC, abstractmethod
import seaborn as sns

class MissValueAnalysis(ABC):
    '''
    Base class for analyzing the missing value
    '''

    def analyze(self, df: pd.DataFrame):
        '''
        Perform complete missing value anlaysis
        :param df (pd.DataFrame) : Target table for missing value analysis
        :return: None, perform specific analysis based on strategy
        '''
        self.identify_missing_value(df)
        self.visulize_missing_value(df)

    @abstractmethod
    def identify_missing_value(self, df: pd.DataFrame):
        '''
        Base function to identify missing data in the target data frame
        :param df (pd.DataFrame) : Target table for missing value analysis
        :return: Summary of how many missing values in each table
        '''
        pass

    @abstractmethod
    def visulize_missing_value(self, df: pd.DataFrame):
        '''
        Base function to visualize missing data in the target data frame
        :param df (pd.DataFrame) : Target table for missing value analysis
        :return: graph of how many missing values in each table
        '''
        pass

class SimpleMissingAnalyzer(MissValueAnalysis):
    '''
    Simple missing value analysis clusters method
    '''

    def identify_missing_value(self, df: pd.DataFrame):
        '''
        Base function to identify missing data in the target data frame
        :param df (pd.DataFrame) : Target table for missing value analysis
        :return: Summary of how many missing values in each table
        '''
        print("Missing data summary based on Columns: ")
        missing_values = df.isnull().sum()
        print(missing_values[missing_values>0])

    def visulize_missing_value(self, df: pd.DataFrame):
        '''
        Base function to visualize missing data in the target data frame
        :param df (pd.DataFrame) : Target table for missing value analysis
        :return: graph of how many missing values in each table
        '''

        print("Visualizing Missing Values......................")
        plt.figure(figsize=(12,8))
        sns.heatmap(df.isnull(), cbar= False, cmap= 'viridis')
        plt.title('Missing Visualization Heatmap')
        plt.show()

