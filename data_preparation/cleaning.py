import pandas as pd

from util.exceptions import DataFrameTypeError

'''
NAME: remove_NaN_rows
PARAMS:
- df: the DataFrame containing the data
- how: 'any' or 'all' (same as pandas)
DESCRIPTION: removes all rows containing any/all NaN values
RETURN: the manipulated DataFrame
'''
def remove_NaN_rows(df, how='any'):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df')
    df.dropna(how=how)
    return df

'''
NAME: remove_NaN_columns
PARAMS:
- df: the DataFrame containing the data
- how: 'any' or 'all' (same as pandas)
DESCRIPTION: removes all columns containing any/all NaN values
RETURN: the manipulated DataFrame
'''
def remove_NaN_columns(df, how='any'):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df')
    df.dropna(how=how, axis='columns')
    return df

'''
NAME: replace_NaN_with_mean
PARAMS:
- df: the DataFrame containing the data
DESCRIPTION: replaces all NaN values with the mean of the respective column, uses
numeric columns only
RETURN: the manipulated DataFrame
'''
def replace_NaN_with_mean(df):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df')
    mean = df.mean(numeric_only=True).to_dict()
    df.fillna(mean)
    return df