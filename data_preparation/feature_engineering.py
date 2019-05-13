import pandas as pd

from util.exceptions import DataFrameTypeError

'''
NAME: drop_columns
PARAMS:
- df: the DataFrame containing the data
- cols: list of columns to drop
DESCRIPTION: drops all columns specified in cols
RETURN: the manipulated DataFrame
'''
def drop_columns(df, cols):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    df.drop(cols, axis='columns', inplace=True)
    return df
