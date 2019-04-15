import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from util.exceptions import DataFrameTypeError
from util.general import to_file_save_name

def plot_histograms(df, columns=-1, label=None, format='png'):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)

    if columns == -1:
        columns = df.columns

    for col in columns:
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        if label == None or col == label:
            df.hist(column=col, ax=ax)
        else:
            df.hist(column=col, by=label, ax=ax)

        fig.suptitle('Histogram of {}'.format(col))
        plt.savefig('./tmp/images/{}_hist.{}'.format(to_file_save_name(col), format), format=format)
        plt.close(fig)

def plot_boxplots(df, columns=-1, label=None, format='png'):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)

    if columns == -1:
        columns = df.columns

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        if label == None or col == label:
            df.boxplot(column=col, ax=ax)
        else:
            df.boxplot(column=col, by=label, ax=ax)
        plt.savefig('./tmp/images/{}_box.{}'.format(to_file_save_name(col), format), format=format)
        plt.close(fig)
