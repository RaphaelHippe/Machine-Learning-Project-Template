import pandas as pd
import numpy as np
from sklearn.utils import shuffle

from util.exceptions import DataSplitError, DataFrameTypeError

'''
NAME: train_test_split
PARAMS:
- df: A pandas DataFrame containing the whole data set.
- label: A string of the column to use as the label of the classification problem
default value is None specifies no label is present.
- split: A list specifying the split, dafault is 0.8 to 0.2.
- seed: the random seed to use for the random split.
RETURN:
- X_train: A numpy array containing the train data.
- y_train: A numpy array containing the train labels.
- X_test: A numpy array containing the test data.
- y_test: A numpy array containing the test labels.
DESCRIPTION: Splitting the data set randomly into a train and a test set. If labels
are present separate arrays are created and returned.
'''
def train_test_split(df, label=None, split=[0.8, 0.2], seed=None):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df')

    if not np.sum(split) == 1.0:
        raise DataSplitError(np.sum(split))

    df_new = df.copy()
    if seed == None:
        df_new = shuffle(df_new)
    else:
        df_new = shuffle(df_new, random_state=seed)

    m = len(df_new)
    train_end = int(split[0] * m)

    train = df_new[:train_end]
    test = df_new[train_end:]

    if label == None:
        return train.values, _, test.values, _

    y_train = train[label].values
    X_train = train.drop([label], axis=1).values
    y_test = test[label].values
    X_test = test.drop([label], axis=1).values

    return X_train, y_train, X_test, y_test

'''
NAME: train_test_val_split
PARAMS:
- df: A pandas DataFrame containing the whole data set.
- label: A string of the column to use as the label of the classification problem
default value is None specifies no label is present.
- split: A list specifying the split, dafault is 0.6 to 0.2 to 0.2.
- seed: the random seed to use for the random split.
RETURN:
- X_train: A numpy array containing the train data.
- y_train: A numpy array containing the train labels.
- X_val: A numpy array containing the validation data.
- y_val: A numpy array containing the validation labels.
- X_test: A numpy array containing the test data.
- y_test: A numpy array containing the test labels.
DESCRIPTION: Splitting the data set randomly into a train, a validation and a
test set. If labels are present separate arrays are created and returned.
'''
def train_val_test_split(df, label=None, split=[0.6, 0.2, 0.2], seed=None):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df')

    if not np.sum(split) == 1.0:
        raise DataSplitError(np.sum(split))

    df_new = df.copy()
    if seed == None:
        df_new = shuffle(df_new)
    else:
        df_new = shuffle(df_new, random_state=seed)

    m = len(df_new)
    train_end = int(split[0] * m)
    val_end = int(split[1] * m) + train_end

    train = df_new[:train_end]
    val = df_new[train_end:val_end]
    test = df_new[val_end:]

    if label == None:
        return train.values, _, val.values, _, test.values, _

    y_train = train[label].values
    X_train = train.drop([label], axis=1).values
    y_val = val[label].values
    X_val = val.drop([label], axis=1).values
    y_test = test[label].values
    X_test = test.drop([label], axis=1).values

    return X_train, y_train, X_val, y_val, X_test, y_test
