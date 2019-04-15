import pandas as pd

from util.exceptions import DataFrameTypeError

'''
NAME: apply_max_abs_scaling
PARAMS:
- df: the DataFrame containing the data
DESCRIPTION:
RETURN: the manipulated DataFrame
'''
def apply_max_abs_scaling(df):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    from sklearn.preprocessing import MaxAbsScaler
    df[df.columns] = MaxAbsScaler().fit_transform(df[df.columns])
    return df

'''
NAME: apply_min_max_scaling
PARAMS:
- df: the DataFrame containing the data
DESCRIPTION:
RETURN: the manipulated DataFrame
'''
def apply_min_max_scaling(df):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    from sklearn.preprocessing import MinMaxScaler
    df[df.columns] = MinMaxScaler().fit_transform(df[df.columns])
    return df

'''
NAME: apply_normalizer_scaling
PARAMS:
- df: the DataFrame containing the data
DESCRIPTION:
RETURN: the manipulated DataFrame
'''
def apply_normalizer_scaling(df):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    from sklearn.preprocessing import Normalizer
    df[df.columns] = Normalizer().fit_transform(df[df.columns])
    return df

'''
NAME: apply_robust_scaler_scaling
PARAMS:
- df: the DataFrame containing the data
DESCRIPTION:
RETURN: the manipulated DataFrame
'''
def apply_robust_scaler_scaling(df):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    from sklearn.preprocessing import RobustScaler
    df[df.columns] = RobustScaler().fit_transform(df[df.columns])
    return df

'''
NAME: apply_standard_scaler_scaling
PARAMS:
- df: the DataFrame containing the data
DESCRIPTION:
RETURN: the manipulated DataFrame
'''
def apply_standard_scaler_scaling(df):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    from sklearn.preprocessing import StandardScaler
    df[df.columns] = StandardScaler().fit_transform(df[df.columns])
    return df
