from sklearn.datasets import load_wine, load_breast_cancer
import pandas as pd

from util.machine_learning import train_val_test_split
from data_understanding.data_plots import plot_histograms, plot_boxplots
from data_understanding.data_description import describe_data

data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['y'] = data.target

describe_data(df, 'breast_cancer')

# plot_histograms(df, columns=['proline'], format='svg', label='y')
# plot_boxplots(df, label='y')

#
# X_train, y_train, X_val, y_val, X_test, y_test = train_val_test_split(df, label='y')
#
# print(X_train.shape)
# print(y_train.shape)
# print(X_val.shape)
# print(y_val.shape)
# print(X_test.shape)
# print(y_test.shape)
