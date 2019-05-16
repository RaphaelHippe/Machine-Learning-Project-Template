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
        raise DataFrameTypeError('df', df)
    df.dropna(how=how, inplace=True)
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
        raise DataFrameTypeError('df', df)
    df.dropna(how=how, axis='columns', inplace=True)
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
        raise DataFrameTypeError('df', df)
    mean = df.mean(numeric_only=True).to_dict()
    df.fillna(mean, inplace=True)
    return df

'''
NAME: drop_csv_column
PARAMS:
- df: the DataFrame containing the data
DESCRIPTION: drops the index column (Unnamed: 0) from CSV files
RETURN: the manipulated DataFrame
'''
def drop_csv_column(df):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    if 'Unnamed: 0' in df.columns:
        df.drop(['Unnamed: 0'], axis='columns', inplace=True)
    if 'Unnamed: 0.1' in df.columns:
        df.drop(['Unnamed: 0.1'], axis='columns', inplace=True)
    return df

'''
NAME: clean_labels
PARAMS:
- df: the DataFrame containing the data
- label: the column name of the labels
DESCRIPTION: encodes the labels using the ordinal encoder
RETURN: the encoded class labels
'''
def clean_labels(df, label):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    classes = df[label].unique().tolist()
    def transform_labels(row, label, classes):
        return classes.index(row[label])
    df[label] = df.apply(transform_labels, args=(label, classes), axis=1)
    return df

'''
NAME: clean_numeric
PARAMS:
- df: the DataFrame containing the data
- cols: list of columns to remove non numeric values
DESCRIPTION: cleans the data to remove non numeric values from otherwise numeric columns
RETURN: the cleaned DataFrame
'''
def clean_numeric(df, cols):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    for col in cols:
        df = df[df[col].apply(lambda x: is_number(x))]
    return df
