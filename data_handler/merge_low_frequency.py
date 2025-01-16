import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from abc import ABC, abstractmethod

class MergeLowShowBase(ABC):

    @abstractmethod
    def handle(self, df: pd.DataFrame, features: list) -> pd.DataFrame:
        '''
        Base method that handle the low frequency merge for categorical variabels
        :param df (pd.DataFrame): Target dataframe
        :param feature (list[str]): List of features to perfrom the action
        :return (pd.DataFrame): Cleaned and merged dataframe
        '''
        pass


class MergeStrategy(MergeLowShowBase):

    def __init__(self, threshold: float = 5):
        '''
        Define the threshold for considering as low frequency class, default value is 2
        :param threshold (float): threshold to identify
        '''

        self.threshold = threshold

    def set_threshold(self, threshold):
        '''
        Base method to change the threshold of the strategy
        :param threshold (float): New target threshold
        :return:
        '''

        self.threshold = threshold

    @staticmethod
    def check(df:pd.DataFrame, features: list, threshold: float = 5.0) -> bool:
        '''
        Validation function to see if the feature is considered as low frequency class
        :param df (pd.DataFrame): Target dataframe
        :param feature (list[str]): List of features to perfrom the action
        :return: True | False
        '''

        change_dict = {}
        for feature in features:
            total = df[feature].count()
            count_table = df[feature].value_counts()/total*100
            change_dict[feature] = {col : 'SMALL_GROUP' for col in count_table[count_table<=threshold].index.to_list()}
            # print(change_dict)

        return change_dict

    def handle(self, df: pd.DataFrame, features: list) -> pd.DataFrame:
        '''
        Base method that handle the low frequency merge for categorical variabels
        :param df (pd.DataFrame): Target dataframe
        :param feature (list[str]): List of features to perfrom the action
        :return (pd.DataFrame): Cleaned and merged dataframe
        '''

        mapping_dict = MergeStrategy.check(df, features, self.threshold)
        for feature in features:
            df[feature] = df[feature].map(lambda x: mapping_dict[feature].get(x, x))

        return df

