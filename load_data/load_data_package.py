import tempfile
from abc import ABC, abstractmethod
import zipfile
from tempfile import tempdir

import pandas as pd
import os




class DataLoadBasic(ABC):
    """
    A basic abstract class for data loaders to load dataframes from various formats.
    """

    @abstractmethod
    def load_data(self, path: str) -> pd.DataFrame:
        """
        Abstract method for loading a dataframe from a file.

        Args:
            path (str): File path of the data to load.

        Returns:
            pd.DataFrame: The loaded dataframe.
        """
        pass

class CSVLoader(DataLoadBasic):
    '''
    Data Loader for CSV files.
    '''

    @staticmethod
    def file_validator(file_path: str) -> bool:
        '''
        validator to check if it is a valid csv file

        :param file_path: (str) file_path of the file to be loaded as csv file

        :return: True if the file_path is for csv file, False if not
        '''
        return file_path.lower().endswith('.csv')

    def load_data(self, path: str) -> pd.DataFrame:
        '''
        Function in the DataLoadBasic to load data and return the dataframe

        :param path: (str) file path to be processed, should be csv file

        :return: processed data frame
        '''

        if not CSVLoader.file_validator(path):
            raise ValueError("The input file should be csv file")

        try:
            return pd.read_csv(path)
        except Exception as e:
            raise IOError(f"failed to read the csv file {e}")

class ExcelLoader(DataLoadBasic):
    '''
    Class used to load excel file
    '''

    @staticmethod
    def file_validator(file_path: str) -> bool:
        '''
        validator to check if it is a valid Excel file

        :param file_path: (str) file_path of the file to be loaded as Excel file

        :return: True if the file_path is for Excel file, False if not
        '''

        valid_extensions = ('.xlsx', '.xls')
        return file_path.lower().endswith(valid_extensions)

    def load_data(self, path: str) -> pd.DataFrame:
        '''
        Main function used to load and return the Excel file

        :param path: File path for the Excel to be loaded

        :return: combined_df (pd.DataFrame) containing the processed file
        '''

        if not ExcelLoader.file_validator(path):
            raise ValueError('Invalid file type: Expect Excel file')

        try:
            df = pd.read_excel(path, sheet_name=None)
            combined_df = pd.concat(df.values(), ignore_index=True)
            return combined_df
        except Exception as e:
            raise IOError(f"File can not be read {e}")

class ZipLoader(DataLoadBasic):
    '''
    Class used to load Zip file
    '''

    def __init__(self, file_type: str = None):
        self.file_type = file_type


    @staticmethod
    def file_validator(file_path: str) -> bool:
        '''
        validator to check if it is a valid Zip file

        :param file_path: (str) file_path of the file to be loaded as Zip file

        :return: True if the file_path is for Zip file, False if not
        '''


        return file_path.lower().endswith('.zip')

    def load_data(self, path: str) -> pd.DataFrame:
        '''
        This is the main function for loading the Zip file

        :param path: file path for the zip file

        :return: Data Frame
        '''

        if not ZipLoader.file_validator(path):
            raise ValueError("File must be zip file")

        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                with zipfile.ZipFile(path, 'r') as zip_ref:
                    zip_ref.extractall(temp_dir)

                extracted_file = os.listdir(temp_dir)
                csv_files = [f for f in extracted_file if CSVLoader.file_validator(f)]
                excel_file = [f for f in extracted_file if ExcelLoader.file_validator(f)]

                if len(csv_files) == 0 and self.file_type == 'csv':
                    raise FileNotFoundError("No csv file found inside the zip")

                if len(excel_file) == 0 and self.file_type == 'excel':
                    raise FileNotFoundError("No excel file found inside the zip")

                if self.file_type != 'excel':
                    combined_csv = pd.DataFrame()
                    for f in csv_files:
                        csv_file_path = os.path.join(temp_dir, f)
                        df = pd.read_csv(csv_file_path)
                        combined_csv = pd.concat([combined_csv,df], ignore_index= True)

                if self.file_type != 'csv':
                    combined_excel = pd.DataFrame()
                    data_loader = ExcelLoader()
                    for f in excel_file:
                        excel_file_path = os.path.join(temp_dir, f)
                        df = data_loader.load_data(excel_file_path)
                        combined_excel = pd.concat([combined_excel, df], ignore_index= True)

                if (not self.file_type) and not (combined_csv.columns.equals(combined_excel.columns)):
                    raise ValueError("Files inside the zip have different table format")

                if self.file_type == 'excel':
                    return combined_excel
                elif self.file_type == 'csv':
                    return combined_csv

                combined_table = pd.concat([combined_csv, combined_excel], ignore_index= True)

                return combined_table

        except Exception as e:
            raise IOError("Zip file load failed")


class Data_Loader_Handler():
    '''
    Class combined all the data load class and set strategy to load data
    '''

    def __init__(self, strategy: DataLoadBasic = None):
        self._strategy = strategy

    def set_strategy(self, strategy: DataLoadBasic) -> None:
        '''
        Function used to change the data load strategy based on file type

        :param strategy: (DataLoadBasic) Different DataLoadBasic based on file type

        :return: None
        '''

        self._strategy = strategy

    def load_data(self, file_path: str) -> pd.DataFrame:
        '''
        Main function in handler that used to load data, will detect the best loader if not provided

        :param file_path (str): file path to the file want to load

        :return: pd.DataFrame
        '''
        if not self._strategy:
            if CSVLoader.file_validator(file_path):
                self._strategy = CSVLoader()

            elif ExcelLoader.file_validator(file_path):
                self._strategy = ExcelLoader()

            elif ZipLoader.file_validator(file_path):
                self._strategy = ZipLoader()

            else:
                raise ValueError("Current file is not supported in DataLoader")

        return self._strategy.load_data(file_path)


