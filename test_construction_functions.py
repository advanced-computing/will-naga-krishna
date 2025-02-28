import sys
import os
import pandas as pd
# import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.Construction_Application import remove_blanks, convert_to_float



def test_blank_removal():
    data = {
        'name': ['Alice', None, 'Charlie', None, 'Emma'],
        'age': [25, 30, 35, 40, 45]}
    
    df = pd.DataFrame(data)

    expected = {
        'name': ['Alice','Charlie','Emma'],
        'age': [25,35,45]
    }

    df_expected = pd.DataFrame(expected)
    
    #need to pass the column as a list bc of the axis=1 part of the function
    blanks_df = remove_blanks(df, ['name'])
    blanks_df = blanks_df.reset_index(drop=True)

    assert blanks_df.equals(df_expected)
    #this test passed



def test_converting_float():
    data_input = {
        'name': ['Alice', None, 'Charlie', None, 'Emma'],
        'age': ['25', '30', '35', '40', '45']}
    
    df = pd.DataFrame(data_input)

    expected_output = {
        'name': ['Alice', None, 'Charlie', None, 'Emma'],
        'age': [25.0, 30.0, 35.0, 40.0, 45.0]
    }

    df_expected_out = pd.DataFrame(expected_output)

    float_df = convert_to_float(df,['age'])
    float_df = float_df.reset_index(drop=True)

    assert float_df.equals(df_expected_out)
    #this test passed

