import pandas as pd

# def to_borough_name(borough):
#     if borough == '1':
#         return 'Manhattan'
#     elif borough == '2':
#         return 'Bronx'
#     elif borough == '3':
#         return 'Brooklyn'
#     elif borough == '4':
#         return 'Queens'
#     elif borough == '5':
#         return 'Staten Island'
#     elif borough == 'MANHATTAN':
#         return 'Manhattan'
#     elif borough == 'BRONX':
#         return 'Bronx'
#     else:
#         return 'Unknown'

def to_float(series):
    return pd.to_numeric(
        series.astype(str).str.replace(',', ''),
        errors='coerce'
    )

