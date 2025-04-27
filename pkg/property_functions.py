import pandas as pd

def to_float(series):
    return pd.to_numeric(
        series.astype(str).str.replace(',', ''),
        errors='coerce'
    ).astype(float)

def to_residential_type(category):
    if category == '01 ONE FAMILY DWELLINGS':
        return '1 Family'
    elif category == '02 TWO FAMILY DWELLINGS':
        return '2 Family'
    elif category == '03 THREE FAMILY DWELLINGS':
        return '3 Family'
    else:
        return 'Other'