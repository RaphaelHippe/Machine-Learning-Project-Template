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

    for col in columns:
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        if label == None or col == label:
            df.boxplot(column=col, ax=ax)
        else:
            df.boxplot(column=col, by=label, ax=ax)
        plt.savefig('./tmp/images/{}_box.{}'.format(to_file_save_name(col), format), format=format)
        plt.close(fig)


def plot_cat_scatter(df, x_cols, y, format='png'):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    if y in x_cols:
        from util.exceptions import ConfigError
        raise ConfigError('The label "{}" was also configured as a feature in x_cols for function "plot_cat_scatter".'.format(y))
    import seaborn as sns
    import matplotlib.ticker as ticker
    # TODO: check y is not in x_cols
    for col in x_cols:
        g = sns.catplot(x=col, y=y, data=df)
        ax = g.axes[0,0]
        ax.set_xticklabels(df[col].unique().tolist(), rotation=90)
        N = df[col].nunique()
        plt.xticks(range(int(N)))
        plt.gca().margins(x=0)
        plt.gcf().canvas.draw()
        m = 0.1
        margin = m/plt.gcf().get_size_inches()[0]
        plt.gcf().subplots_adjust(left=margin, right=1.-margin, bottom=0.333)
        plt.gcf().set_size_inches(30, 7)

        plt.savefig('./tmp/images/{}_to_{}_cat_scatter.{}'.format(to_file_save_name(col), to_file_save_name(y), format), format=format)
        plt.close(plt.gcf())




def plot_cat_point(df, x_cols, y, format='png'):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    if y in x_cols:
        from util.exceptions import ConfigError
        raise ConfigError('The label "{}" was also configured as a feature in x_cols for function "plot_cat_point".'.format(y))
    import seaborn as sns
    import matplotlib.ticker as ticker
    for x_col in x_cols:
        for hue_col in x_cols:
            if x_col != hue_col:
                g = sns.catplot(x=x_col, y=y, hue=hue_col, kind='point', data=df)
                ax = g.axes[0,0]
                N = df[col].nunique()
                plt.xticks(range(N))
                plt.gca().margins(x=0)
                plt.gcf().canvas.draw()
                tl = plt.gca().get_xticklabels()
                maxsize = max([t.get_window_extent().width for t in tl])
                m = 0.2 # inch margin
                s = maxsize/plt.gcf().dpi*N+2*m
                margin = m/plt.gcf().get_size_inches()[0]

                plt.gcf().subplots_adjust(left=margin, right=1.-margin)
                plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])

                plt.savefig('./tmp/images/{}_to_{}_hue_{}_cat_point.{}'.format(to_file_save_name(x_col), to_file_save_name(y), to_file_save_name(hue_col), format), format=format)
                plt.close(plt.gcf())


def plot_cat_violin(df, x_cols, y, format='png'):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    if y in x_cols:
        from util.exceptions import ConfigError
        raise ConfigError('The label "{}" was also configured as a feature in x_cols for function "plot_cat_violin".'.format(y))
    import seaborn as sns
    import matplotlib.ticker as ticker
    for x_col in x_cols:
        for hue_col in x_cols:
            if x_col != hue_col:
                g = sns.catplot(x=x_col, y=y, hue=hue_col, kind='violin', data=df)
                ax = g.axes[0,0]
                N = df[col].nunique()
                plt.xticks(range(N))
                plt.gca().margins(x=0)
                plt.gcf().canvas.draw()
                tl = plt.gca().get_xticklabels()
                maxsize = max([t.get_window_extent().width for t in tl])
                m = 0.2 # inch margin
                s = maxsize/plt.gcf().dpi*N+2*m
                margin = m/plt.gcf().get_size_inches()[0]

                plt.gcf().subplots_adjust(left=margin, right=1.-margin)
                plt.gcf().set_size_inches(s, plt.gcf().get_size_inches()[1])

                plt.savefig('./tmp/images/{}_to_{}_hue_{}_cat_violin.{}'.format(to_file_save_name(x_col), to_file_save_name(y), to_file_save_name(hue_col), format), format=format)
                plt.close(plt.gcf())
