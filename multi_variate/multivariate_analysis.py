import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from abc import ABC, abstractmethod
import seaborn as sns

class MultiVariateBase(ABC):
    '''
    Base class for multivariate analysis strategies
    '''
    def analyze(self, df: pd.DataFrame):
        '''
        Analyze and visualize multiple variables relationship through Heatmap and Pairplot
        :param df (pd.DataFrame) : Selected Target Data Frame
        :return: Graphs
        '''
        self.get_heatmap(df)
        self.get_pairplot(df)

    def get_heatmap(self, df: pd.DataFrame):
        '''
        Generate the Heatmap for Target data frame
        :param df (pd.DataFrame) : Selected Target Data Frame
        :return: HeatMap Visual
        '''
        pass

    def get_pairplot(self, df: pd.DataFrame):
        '''
        Generate the pariplot for Target data frame
        :param df (pd.DataFrame) : Selected Target Data Frame
        :return: pariplot Visual
        '''
        pass


class SimpleMultivariateStrategy(MultiVariateBase):
    '''
    Simple Strategy class for analyzing multivariable in selected DataFrame
    '''

    def get_heatmap(self, df: pd.DataFrame):
        '''
        Generate the Heatmap for Target data frame
        :param df (pd.DataFrame) : Selected Target Data Frame
        :return: HeatMap Visual
        '''

        print("Generating Heatmap for selected data frame with specific features ........")
        plt.figure(figsize=(16,8))
        sns.heatmap(df.corr(), annot=True, fmt= '.2f', cmap='coolwarm')
        plt.title('Correlation HeatMap')
        plt.show()

    def get_pairplot(self, df: pd.DataFrame):
        '''
        Generate the pariplot for Target data frame
        :param df (pd.DataFrame) : Selected Target Data Frame
        :return: pariplot Visual
        '''

        print("Generating Pariplot for selected data frame with specific features ........")
        plt.figure(figsize=(12,8))
        sns.pairplot(df)
        # plt.title("Pairplot for Target DataFrame for Selected Features")
        plt.show()