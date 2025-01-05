import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from abc import ABC, abstractmethod

from fontTools.subset import subset


class MissingValueFixBase(ABC):
    '''
    Base class defining different Missing Value Fix Strategies
    '''

    def handle(self, df: pd.DataFrame, feature: list = None) -> pd.DataFrame:
        '''
        Base Method for different Strategy to handle missing value
        :param df (pd.DataFrame) : Target DataFrame with missing
        :param feature: list = None: Specific columns to perform the fix
        :return (pd.DataFrame) : Processed DataFrame after the fix
        '''
        pass

class Drop_Strategy(MissingValueFixBase):
    '''
    Strategy to drop selected missing value
    '''

    def __init__(self, axis: int = 0, threshold: int = None):
        '''
        Set the initial value for the drop strategy, default drop on row with any none to drop
        :param axis: axis to perfrom the drop action
        :param threshold: minumum number of not-none value to be kept
        '''
        self.axis = axis
        self.threshold = threshold

    def handle(self, df: pd.DataFrame, feature: list = None) -> pd.DataFrame:
        '''
        Base Method for drop Strategy to handle missing value, if not feature provided, look at all table
        :param df (pd.DataFrame) : Target DataFrame with missing
        :param feature: list = None: Specific columns to perform the fix
        :return (pd.DataFrame) : Processed DataFrame after the drop
        '''

        try:
            new_df = df.copy()
            if feature is not None:
                new_df.dropna(subset = feature, axis = self.axis, thresh = self.threshold, inplace = True)
            else:
                if not self.threshold:
                    new_df.dropna(axis=self.axis, inplace=True)
                else:
                    new_df.dropna(axis=self.axis, thresh= self.threshold, inplace=True)
            print("Missing value dropped")
            return new_df
        except Exception as e:
            raise IOError("Can not drop")

class Fill_Strategy(MissingValueFixBase):

    '''
    Strategy to fill missing value with specific method
    '''

    def __init__(self, method: str = 'mean', value: str = None):
        '''
        Initialize the strategy with default mean filling method, value is used for constant method.
        :param method (str) : Method used to fill the missing value
        :param value: (str) : Default value for constant method
        '''
        self.method = method
        self.value = value

    def set_method(self, method: str):
        '''
        Change the default method for the filling strategy
        :param method (str): Target new method
        :return: None
        '''
        self.method = method

    def set_value(self, value: str):
        '''
        Change the default value for the filling strategy
        :param value (str): Target new value
        :return: None
        '''
        self.value = value


    def handle(self, df: pd.DataFrame, feature: list = None) -> pd.DataFrame:
        '''
        Base Method for drop Strategy to handle missing value, if not feature provided, look at all table
        :param df (pd.DataFrame) : Target DataFrame with missing
        :param feature: list = None: Specific columns to perform the fix
        :return (pd.DataFrame) : Processed DataFrame after the drop
        '''

        print(f"Perform the filling strategy {self.method}.........")

        new_df = df.copy()
        try:
            if self.method == 'mean':
                if feature:
                    for col in feature:
                        new_df[col] = new_df[col].fillna(new_df[col].mean())
                else:
                    for col in new_df.select_dtypes(include = 'number').columns:
                        new_df[col] = new_df[col].fillna(new_df[col].mean())

            if self.method == 'mode':
                if feature:
                    for col in feature:
                        new_df[col] = new_df[col].fillna(new_df[col].mode())
                else:
                    for col in new_df.columns:
                        new_df[col] = new_df[col].fillna(new_df[col].mode())

            if self.method == 'constant':
                if feature:
                    for col in feature:
                        new_df[col] = new_df[col].fillna(self.value)
                else:
                    for col in new_df.columns:
                        new_df[col] = new_df[col].fillna(self.value)

            print("Filling finished, if want to change different method, please call .set_method(), /n"
                  "selections are: 'mean', 'mode', 'constant'/n"
                  "To change the value for constant method, use .set_value() ")

            return new_df

        except Exception as e:
            raise IOError("Failed to fill with specific method")

class Missing_Value_Handler():
    '''
    Main handler for different missing value fixing method
    '''

    def __init__(self, strategy: MissingValueFixBase = Fill_Strategy()):
        '''
        Select the default missing value strategy
        :param strategy: MissingValueFixBase
        '''
        self._strategy = strategy

    def set_strategy(self, strategy: MissingValueFixBase):
        '''
        Function uses to switch between different missing value fixing strategy
        :param strategy (MissingValueFixBase): Target strategy
        :return: None
        '''
        self._strategy = strategy

    def set_method(self, method: str):
        '''
        Change the default method for the filling strategy
        :param method (str): Target new method
        :return: None
        '''
        if isinstance(self._strategy, Fill_Strategy):
            self._strategy.set_method(method)
        else:
            raise ValueError("Can not set method for non-filling strategy, please switch to Fill_Strategy()")

    def set_value(self, value: str):
        '''
        Change the default value for the filling strategy
        :param value (str): Target new value
        :return: None
        '''
        if isinstance(self._strategy, Fill_Strategy):
            self._strategy.set_value(value)
        else:
            raise ValueError("Can not set value for non-filling strategy, please switch to Fill_Strategy()")

    def process(self, df: pd.DataFrame, feature: list = None) -> pd.DataFrame:
        '''
        Main function to perform different missing value method
        :param df (pd.DataFrame) : Target DataFrame
        :param feature (list = None): Specific columns to be processed
        :return: pd.DataFrame -> cleaned DataFrame
        '''
        try:
            new_df = self._strategy.handle(df, feature)
            return new_df
        except Exception as e:
            raise IOError('Failed to process missing value')
