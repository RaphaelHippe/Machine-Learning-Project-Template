import yaml

from sklearn.datasets import load_wine, load_breast_cancer
import pandas as pd

from util.machine_learning import train_val_test_split, cross_validation
from data_understanding.data_plots import plot_histograms, plot_boxplots
from data_understanding.data_description import describe_data
from modeling.classification import train_knn_clf, predict, train_gnb_clf
from evaluation.scoring import calc_accuracy
from data_preparation.scaling import apply_min_max_scaling




def main(config):
    df = pd.read_csv('{}.csv'.format(config['general']['data']['path']))

    from data_preparation.encodings import apply_leave_one_out_encoding
    df = apply_leave_one_out_encoding(df, categorical_columns=config['data_preparation']['encodings']['categorical_columns'], label=config['general']['data']['label'])

    from data_understanding.data_description import describe_data
    describe_data(df, 'dd_encoded')





# with open('config.yaml', 'r') as stream:
#     try:
#         config = yaml.load(stream)
#         main(config)
#     except yaml.YAMLError as exc:
#         print(exc)


from util.general import create_config_yaml
create_config_yaml()
