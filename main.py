from sklearn.datasets import load_wine, load_breast_cancer
import pandas as pd

from util.machine_learning import train_val_test_split, cross_validation
from data_understanding.data_plots import plot_histograms, plot_boxplots
from data_understanding.data_description import describe_data
from modeling.classification import train_knn_clf, predict, train_gnb_clf
from evaluation.scoring import calc_accuracy
from data_preparation.scaling import apply_min_max_scaling


data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)


df['y'] = data.target

df = apply_min_max_scaling(df)
# describe_data(df, 'breast_cancer')



# plot_histograms(df, columns=['proline'], format='svg', label='y')
# plot_boxplots(df, label='y')

#
X_train, y_train, X_val, y_val, X_test, y_test = train_val_test_split(df, label='y')
#
# print(X_train.shape)
# print(y_train.shape)
# print(X_val.shape)
# print(y_val.shape)
# print(X_test.shape)
# print(y_test.shape)

clf = train_knn_clf(X_train, y_train)
y_pred = predict(clf, X_val)
# acc = calc_accuracy(y_val, y_pred)
acc = cross_validation(calc_accuracy, (y_val, y_pred), n=50)
print('acc', acc)
