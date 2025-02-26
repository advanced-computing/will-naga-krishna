import pytest
import pandas as pd
from pages.Land_Price import to_float

def test_to_float():
    data = pd.Series(['1', '2', '3', '4', '5'])

    result = to_float(data)

    expected = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0], dtype=float)

    assert result.equals(expected)
# End snippet