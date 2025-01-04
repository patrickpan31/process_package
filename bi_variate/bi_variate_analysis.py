import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from abc import ABC, abstractmethod
import seaborn as sns

class Bi_Variate_Base(ABC):
    '''
    Base class for bi-variate analysis
    '''

    @abstractmethod
    def execute_analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        '''
        Base function to perform bi-variate analysis based on different strategies
        :param df (pd.DataFrame) : Target Data Frame
        :param feature1: feature that used to put on axis x
        :param feature2: feature that used to put on axis y
        :return: different analysis
        '''

        pass

class NumericvsNumericStrategy(Bi_Variate_Base):
    '''
    Numeric variable vs numeric variable strategy
    '''

    def execute_analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        '''

        Base function to perform bi-variate analysis based on different strategies
        :param df (pd.DataFrame) : Target Data Frame
        :param feature1: feature that used to put on axis x
        :param feature2: feature that used to put on axis y
        :return: different analysis

        '''
        print(f"Analyzing feature {feature1} vs {feature2}")
        plt.figure(figsize= (10,6))
        sns.scatterplot(x = feature1, y = feature2, data = df)
        plt.title(f'{feature1} vs {feature2}')
        plt.xlabel(f'{feature1}')
        plt.ylabel(f'{feature2}')
        plt.show()

class NumericvsCategoricalStrategy(Bi_Variate_Base):
    '''
    Analyze and visualize numeric variable to categorical variable
    '''

    def execute_analyze(self, df: pd.DataFrame, feature1: str, feature2: str):
        '''

        Base function to perform bi-variate analysis based on different strategies
        :param df (pd.DataFrame) : Target Data Frame
        :param feature1: feature that used to put on axis x
        :param feature2: feature that used to put on axis y
        :return: different analysis

        '''
        print(f"Analyzing feature {feature1} vs {feature2}")
        plt.figure(figsize=(10,6))
        sns.boxplot(x=feature1, y = feature2, data = df)
        plt.title(f'{feature1} vs {feature2}')
        plt.xlabel(f'{feature1}')
        plt.ylabel(f'{feature2}')
        plt.show()

class Bi_Variate_Analyzer():
    '''
    Bi-variate analysis strategy handler
    '''

    def __init__(self, strategy: Bi_Variate_Base):
        '''
        Set the Bi-Variate Strategy
        :param strategy (Bi_Variate_Base): Target analysis strategy
        '''
        self._strategy = strategy

    def set_strategy(self, strategy: Bi_Variate_Base):
        '''
        Swtich between different analysis strategy
        :param strategy (Bi_Variate_Base): Target analysis strategy
        :return: None
        '''

        self._strategy = strategy

    def analyze(self, x:str, y:str, df: pd.DataFrame):
        '''
        Main function to call the strategy to analyze specific features in df
        :param x (str): feature 1 to be analyzed, set to x axis
        :param y (str): feature 2 to be analyzed, set to y axis
        :param df (pd.DataFrame) : Target data frame
        :return: Differnet analysis strategy result
        '''
        return self._strategy.execute_analyze(df, x, y)