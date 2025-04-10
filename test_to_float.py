# # import pytest
# import pandas as pd
# from pkg.to_float import to_float

# def test_to_float():
#     data = pd.Series(['1', '2', '3', '4', '5'])

#     result = to_float(data)

#     expected = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0], dtype=float)

#     assert result.equals(expected)
# # End snippet


#this passed the pytest

import pandas as pd
from pkg.property_functions import to_float

def test_to_float():

    data = pd.Series(['1', '2', '3', '4', '5'])
    result = to_float(data).reset_index(drop=True)

    expected = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])
    expected = expected.reset_index(drop=True)

    assert result.equals(expected)
