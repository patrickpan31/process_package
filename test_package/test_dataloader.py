import tempfile
from abc import ABC, abstractmethod
import zipfile
from tempfile import tempdir
import pytest

from load_data.load_data_package import CSVLoader, ExcelLoader, ZipLoader, Data_Loader_Handler

import pandas as pd
import os

@pytest.fixture
def sample_df():
    #create sample data frame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)
    return df

@pytest.fixture
def create_test_csv(sample_df):

    # Save as CSV
    csv_file_path = 'test_file.csv'
    sample_df.to_csv(csv_file_path, index=False)
    print(f"Test CSV file created: {csv_file_path}")

    # Yield the file path to the test and clean up afterward
    yield csv_file_path

    # Cleanup after test
    import os
    os.remove(csv_file_path)
    print(f"Test CSV file removed: {csv_file_path}")

@pytest.fixture
def create_test_excel(sample_df):


    # Save as CSV
    excel_file_path = 'test_file.xlsx'
    sample_df.to_excel(excel_file_path, index=False, sheet_name='Sheet1')

    print(f"Test EXCEL file created: {excel_file_path}")

    # Yield the file path to the test and clean up afterward
    yield excel_file_path

    # Cleanup after test
    import os
    os.remove(excel_file_path)
    print(f"Test Excel file removed: {excel_file_path}")

@pytest.fixture
def create_test_zip(create_test_excel, create_test_csv):
    import os
    import zipfile
    import shutil

    os.makedirs('test_files', exist_ok=True)
    zip_file_path = 'test_archive.zip'

    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        # Add the CSV and Excel files to the ZIP archive
        zipf.write(create_test_excel, arcname='test_file.xlsx')
        zipf.write(create_test_csv, arcname='test_file.csv')

    # Yield the file path to the test and clean up afterward
    yield zip_file_path

    # Cleanup after test
    shutil.rmtree('test_files')

    # Remove ZIP file
    os.remove(zip_file_path)
    print(f"Test zip file removed: {zip_file_path}")

def test_CSVLoader(create_test_csv):
    '''
    Test function to test if CSVLoader is working properly

    :param create_test_csv: (pytest_fixture) test csv file generated from the fixture

    :return: True | False
    '''
    csv_loader = Data_Loader_Handler(CSVLoader())
    df = csv_loader.load_data(create_test_csv)

    assert len(df) > 0
    assert list(df.columns) == ['Name', 'Age', 'City']

def test_ExcelLoader(create_test_excel):
    '''
    Test function to test if ExcelLoader is working properly

    :param create_test_excel: (pytest_fixture) test Excel file generated from the fixture

    :return: True | False
    '''
    excel_loader = Data_Loader_Handler(ExcelLoader())
    df = excel_loader.load_data(create_test_excel)

    assert len(df) > 0
    assert list(df.columns) == ['Name', 'Age', 'City']

def test_ZIPLoader(create_test_zip):
    '''
    Test function to test if ZipLoader is working properly

    :param create_test_excel: (pytest_fixture) test zip file generated from the fixture

    :return: True | False
    '''
    zip_loader = Data_Loader_Handler(ZipLoader())
    df = zip_loader.load_data(create_test_zip)

    assert len(df) > 0
    assert list(df.columns) == ['Name', 'Age', 'City']

def test_no_nameLoader(create_test_csv):
    '''
    Test function to test if ZipLoader is working properly

    :param create_test_excel: (pytest_fixture) test zip file generated from the fixture

    :return: True | False
    '''
    zip_loader = Data_Loader_Handler()
    df = zip_loader.load_data(create_test_csv)

    assert len(df) > 0
    assert list(df.columns) == ['Name', 'Age', 'City']


