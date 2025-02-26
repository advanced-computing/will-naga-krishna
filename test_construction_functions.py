import sys
import os
import pandas as pd
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.Construction_Application import remove_blanks



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
    #this passed the test





