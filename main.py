import yaml
import pandas as pd


def main(config):

    # loading data

    if config['general']['data']['type'] == 'csv':
        df = pd.read_csv('{}.csv'.format(config['general']['data']['path']))
    elif config['general']['data']['type'] == 'pickle':
        df = pd.read_pickle('{}.pkl'.format(config['general']['data']['path']))
    else:
        pass # TODO: Raise exception


    # data understanding
    # description
    if config['data_understanding']['description']['execute']:
        from data_understanding.data_description import describe_data
        describe_data(df, config['data_understanding']['description']['name'])
    # plots
    if config['data_understanding']['plots']['execute']:
        # histograms
        if config['data_understanding']['plots']['histograms']['execute']:
            from data_understanding.data_plots import plot_histograms
            plot_histograms(df,
                            columns=config['data_understanding']['plots']['histograms']['columns'],
                            label=config['data_understanding']['plots']['histograms']['label'],
                            format=config['data_understanding']['plots']['histograms']['format'])
        # boxplots
        if config['data_understanding']['plots']['boxplots']['execute']:
            from data_understanding.data_plots import plot_boxplots
            plot_boxplots(df,
                            columns=config['data_understanding']['plots']['histograms']['columns'],
                            label=config['data_understanding']['plots']['histograms']['label'],
                            format=config['data_understanding']['plots']['histograms']['format'])

    # data preparation
    if config['data_preparation']['data_split']['execute']:
        if config['data_preparation']['data_split']['validation_set']:
            from util.machine_learning import train_val_test_split
            X_train, y_train, X_test, y_test, X_val, y_val = train_val_test_split(df,
                                                                                  label=config['data_preparation']['data_split']['label']
                                                                                  split=config['data_preparation']['data_split']['split']
                                                                                  seed=config['data_preparation']['data_split']['seed'])
        else:
            from util.machine_learning import train_test_split
            X_train, y_train, X_test, y_test = train_test_split(df,
                                                                label=config['data_preparation']['data_split']['label']
                                                                split=config['data_preparation']['data_split']['split']
                                                                seed=config['data_preparation']['data_split']['seed'])

    # modeling
    if config['modeling']['classification']['execute']:
            for clf_key in config['modeling']['classification']['classifiers']:
                pass

    # evaluation




with open('config.yaml', 'r') as stream:
    try:
        config = yaml.load(stream)
        main(config)
    except yaml.YAMLError as exc:
        print(exc)
