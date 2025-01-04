import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from abc import ABC, abstractmethod
import seaborn as sns

class UniVariateStrategy(ABC):
    '''
    Base class used for uni-variable analysis
    '''

    @abstractmethod
    def analyze(self, df: pd.DataFrame, feature: str) -> None:
        '''
        Main function used to analyze and visualize the univariable
        :param df (pd.DataFrame): target dataframe for analysis
        :param feature (str) : Target feature in target dataframe
        :return: Graph or summary for the analysis
        '''

        pass

class NumericUniAnalysis(UniVariateStrategy):

    '''
    Class from base UniVariateStategy to analyze numeric features
    '''

    def analyze(self, df: pd.DataFrame, feature: str) -> None:
        '''
        Main function used to analyze and visualize the univariable
        :param df (pd.DataFrame): target dataframe for analysis
        :param feature (str) : Target feature in target dataframe
        :return: Graph or summary for the analysis
        '''

        print(f"Analyzing feature {feature} .........")
        plt.figure(figsize=(10,6))
        sns.histplot(df[feature], kde= True, bins = 50)
        plt.title(f'Histogram for feature {feature}')
        plt.xlabel(f'{feature}')
        plt.ylabel('Frequency')
        plt.show()

class CategoricalUniAnalysis(UniVariateStrategy):

    '''
    Class from base UniVariateStategy to analyze numeric features
    '''

    def analyze(self, df: pd.DataFrame, feature: str) -> None:
        '''
        Main function used to analyze and visualize the univariable
        :param df (pd.DataFrame): target dataframe for analysis
        :param feature (str) : Target feature in target dataframe
        :return: Graph or summary for the analysis
        '''

        print(f"Analyzing the categorical feature {feature}")
        plt.figure(figsize=(10,6))

        # new_df = df.groupby(feature).size().reset_index(name = 'cnt').sort_values('cnt', ascending= False)
        # sns.barplot(x=feature, y = 'cnt', data = new_df, palette= 'viridis')

        sorted_order = df[feature].value_counts().index
        sns.countplot(x = feature, data = df, palette= 'muted', order = sorted_order)
        plt.title(f'Count Plot for feature {feature}')
        plt.xlabel(f'{feature}')
        plt.ylabel('Count')
        plt.show()

class Uni_Variate_Analyzer():
    '''
    Collection usage class for the Univariate Analysis Strategies
    '''

    def __init__(self, strategy: UniVariateStrategy):
        '''
        Setting the base strategy want to use for the analyzer
        :param strategy (UniVariateStrategy): Selected strategy
        '''

        self._strategy = strategy

    def set_strategy(self, strategy: UniVariateStrategy) -> None:
        '''
        Use to switch between different strategies for the analyzer
        :param strategy (UniVariateStrategy): Selected strategy
        :return: None
        '''

        self._strategy = strategy

    def analyze(self, df: pd.DataFrame, feature: str) -> None:
        '''
        Main function used to analyze and visualize the univariable
        :param df (pd.DataFrame): target dataframe for analysis
        :param feature (str) : Target feature in target dataframe
        :return: Graph or summary for the analysis
        '''
        try:
            self._strategy.analyze(df, feature)
        except Exception as e:
            raise ValueError("Can analyze the data, check if check to the correct strategy: /n"
                             "NumericUniAnalysis() or CategoricalUniAnalysis() /n"
                             "you can reset the strategy using .set_strategy() /n")


