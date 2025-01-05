import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from abc import ABC, abstractmethod

class FeatureEngineeringBase(ABC):
    '''
    Base class for different feature engineering strategy
    '''

    @abstractmethod
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        '''
        Base function to perform strategy feature transformation
        :param df (pd.DataFrame) : Target Data Frame for transformation
        :return: (pd.DataFrame) Transformed Data Frame
        '''
        pass

class LogTransformation(FeatureEngineeringBase):
    '''
    Perform Log Transformation for those skewed columns to make them more normal
    '''

    def __init__(self, features: list):
        '''
        Initial those features to be changed
        :param features (list[str]): List of column names
        '''
        self.features = features

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        '''
        Base function to perform log transformation
        :param df (pd.DataFrame) : Target Data Frame for transformation
        :return: (pd.DataFrame) Transformed Data Frame
        '''
        try:
            new_df = df.copy()
            print("Log Transformation starts............")
            for feature in self.features:
                new_df[feature] = np.log1p(new_df[feature])
                # log1p is log(1+x) to avoid log(0)
            print("Log Transformation finished")
            return new_df
        except Exception as e:
            raise IOError(f"Log transformation failed becuase of {e}")