import pandas as pd

from util.exceptions import DataFrameTypeError

'''
NAME: apply_one_hot_encoding
PARAMS:
- df: DataFrame containing the data
DESCRIPTION:
RETURN:
'''
def apply_one_hot_encoding(df, categorical_columns):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    import category_encoders as ce
    encoder = ce.OneHotEncoder(cols=categorical_columns).fit(df.values)
    X_transformed = encoder.transform(df)
    return X_transformed

'''
NAME: apply_dummy_encoding
PARAMS:
- df: DataFrame containing the data
DESCRIPTION:
RETURN:
'''
def apply_dummy_encoding(df):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    X_transformed = pd.get_dummies(df)
    return X_transformed

'''
NAME: apply_backward_difference_encoding
PARAMS:
- df: DataFrame containing the data
DESCRIPTION:
RETURN:
'''
def apply_backward_difference_encoding(df, categorical_columns):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    import category_encoders as ce
    encoder = ce.BackwardDifferenceEncoder(cols=categorical_columns).fit(df.values)
    X_transformed = encoder.transform(df)
    X_transformed.drop(['intercept'], inplace=True, axis=1)
    return X_transformed

'''
NAME: apply_baseN_encoding
PARAMS:
- df: DataFrame containing the data
DESCRIPTION:
RETURN:
'''
def apply_baseN_encoding(df, categorical_columns):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    import category_encoders as ce
    encoder = ce.BaseNEncoder(base=3, cols=categorical_columns).fit(df.values)
    X_transformed = encoder.transform(df)
    return X_transformed

'''
NAME: apply_binary_encoding
PARAMS:
- df: DataFrame containing the data
DESCRIPTION:
RETURN:
'''
def apply_binary_encoding(df, categorical_columns):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    import category_encoders as ce
    encoder = ce.BinaryEncoder(cols=categorical_columns).fit(df.values)
    X_transformed = encoder.transform(df)
    return X_transformed

'''
NAME: apply_helmert_encoding
PARAMS:
- df: DataFrame containing the data
DESCRIPTION:
RETURN:
'''
def apply_helmert_encoding(df, categorical_columns):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    import category_encoders as ce
    encoder = ce.HelmertEncoder(cols=categorical_columns).fit(df.values)
    X_transformed = encoder.transform(df)
    X.drop(['intercept'], inplace=True, axis=1)
    return X_transformed

'''
NAME: apply_sum_encoding
PARAMS:
- df: DataFrame containing the data
DESCRIPTION:
RETURN:
'''
def apply_sum_encoding(df, categorical_columns):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    import category_encoders as ce
    encoder = ce.SumEncoder(cols=categorical_columns).fit(df.values)
    X_transformed = encoder.transform(df)
    X.drop(['intercept'], inplace=True, axis=1)
    return X_transformed

'''
NAME: apply_leave_one_out_encoding
PARAMS:
- df: DataFrame containing the data
- label: Column name of the label column (default 'y')
DESCRIPTION:
RETURN:
'''
def apply_leave_one_out_encoding(df, label='y', categorical_columns):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    import category_encoders as ce
    encoder = ce.LeaveOneOutEncoder(cols=categorical_columns).fit(df.drop([label], axis=1), df[label])
    X_transformed = encoder.transform(df)
    return X_transformed

'''
NAME: apply_target_encoding
PARAMS:
- df: DataFrame containing the data
- label: Column name of the label column (default 'y')
DESCRIPTION:
RETURN:
'''
def apply_target_encoding(df, label='y', categorical_columns):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    import category_encoders as ce
    encoder = ce.TargetEncoder(cols=categorical_columns).fit(df.drop([label], axis=1), df[label])
    X_transformed = encoder.transform(df)
    return X_transformed

'''
NAME: apply_ordinal_encoding
PARAMS:
- df: DataFrame containing the data
- label: Column name of the label column (default 'y')
DESCRIPTION:
RETURN:
'''
def apply_ordinal_encoding(df, label='y', categorical_columns):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    import category_encoders as ce
    encoder = ce.OrdinalEncoder(cols=categorical_columns).fit(df.drop([label], axis=1), df[label])
    X_transformed = encoder.transform(df)
    return X_transformed

'''
NAME: apply_weight_of_evidence_encoding
PARAMS:
- df: DataFrame containing the data
- label: Column name of the label column (default 'y')
DESCRIPTION:
RETURN:
'''
def apply_weight_of_evidence_encoding(df, label='y', categorical_columns):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    import category_encoders as ce
    encoder = ce.WOEEncoder(cols=categorical_columns).fit(df.drop([label], axis=1), df[label])
    X_transformed = encoder.transform(df)
    return X_transformed

'''
NAME: apply_pca
PARAMS:
- df: DataFrame containing the data
- label: Column name of the label column (default 'y')
DESCRIPTION:
RETURN:
'''
def apply_pca(df, label='y', categorical_columns):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    # TODO: implement
    return None
