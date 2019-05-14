import yaml
import pandas as pd
import os

def main(config):

    # loading data
    if config['general']['data']['type'] == 'csv':
        if os.path.isdir(config['general']['data']['path']):
            files = ['{}/{}'.format(config['general']['data']['path'], f) for f in os.listdir(config['general']['data']['path']) if f.endswith('.csv')]
            df = pd.concat((pd.read_csv(f, index_col=None, header=0) for f in files), ignore_index=True, axis=0)
        else:
            df = pd.read_csv('{}.csv'.format(config['general']['data']['path']))
        from data_preparation.cleaning import drop_csv_column
        df = drop_csv_column(df)
    elif config['general']['data']['type'] == 'pickle':
        df = pd.read_pickle('{}.pkl'.format(config['general']['data']['path']))
    else:
        from util.exceptions import UnknownKeyError
        raise UnknownKeyError(config['general']['data']['type'], 'data type while loading data set')


    # data understanding
    # description
    if config['data_understanding']['description']['execute']:
        from data_understanding.data_description import describe_data
        describe_data(df, config['general']['data']['name'], config['data_understanding']['description']['n'])
    # plots
    # histograms
    if config['data_understanding']['plots']['histograms']['execute']:
        from data_understanding.data_plots import plot_histograms
        plot_histograms(df,
                        columns=config['data_understanding']['plots']['histograms']['columns'],
                        label=config['general']['data']['label'],
                        format=config['data_understanding']['plots']['histograms']['format'])
    # boxplots
    if config['data_understanding']['plots']['boxplots']['execute']:
        from data_understanding.data_plots import plot_boxplots
        plot_boxplots(df,
                        columns=config['data_understanding']['plots']['boxplots']['columns'],
                        label=config['general']['data']['label'],
                        format=config['data_understanding']['plots']['boxplots']['format'])
    # categorical scatter
    if config['data_understanding']['plots']['cat_scatter']['execute']:
        from data_understanding.data_plots import plot_cat_scatter
        plot_cat_scatter(df,
                        x_cols=config['data_understanding']['plots']['cat_scatter']['x_cols'],
                        y=config['general']['data']['label'])
    # categorical point
    if config['data_understanding']['plots']['cat_point']['execute']:
        from data_understanding.data_plots import plot_cat_point
        plot_cat_point(df,
                        x_cols=config['data_understanding']['plots']['cat_point']['x_cols'],
                        y=config['general']['data']['label'])
    # categorical violin
    if config['data_understanding']['plots']['cat_violin']['execute']:
        from data_understanding.data_plots import plot_cat_violin
        plot_cat_violin(df,
                        x_cols=config['data_understanding']['plots']['cat_point']['x_cols'],
                        y=config['general']['data']['label'])

    # data preparation
    # from util.machine_learning import extract_X_y
    # X, y = extract_X_y(df, label=config['general']['data']['label'])

    if config['data_preparation']['clean_labels']:
        from data_preparation.cleaning import clean_labels
        df = clean_labels(df, config['general']['data']['label'])

    if config['data_preparation']['drop_columns']['execute']:
        from data_preparation.feature_engineering import drop_columns
        df = drop_columns(df, config['data_preparation']['drop_columns']['cols'])

    if config['data_preparation']['cleaning']['remove_NaN_rows']:
        from data_preparation.cleaning import remove_NaN_rows
        df = remove_NaN_rows(df)
    if config['data_preparation']['cleaning']['remove_NaN_columns']:
        from data_preparation.cleaning import remove_NaN_columns
        df = remove_NaN_columns(df)
    if config['data_preparation']['cleaning']['replace_NaN_with_mean']:
        from data_preparation.cleaning import replace_NaN_with_mean
        df = replace_NaN_with_mean(df)

    if config['data_preparation']['encodings']['execute']:
        from data_preparation.encodings import apply_leave_one_out_encoding
        df = apply_leave_one_out_encoding(df, categorical_columns=config['data_preparation']['encodings']['categorical_columns'], label=config['general']['data']['label'])

    if config['data_preparation']['cleaning']['remove_NaN_rows']:
        from data_preparation.cleaning import remove_NaN_rows
        df = remove_NaN_rows(df)
    if config['data_preparation']['cleaning']['remove_NaN_columns']:
        from data_preparation.cleaning import remove_NaN_columns
        df = remove_NaN_columns(df)
    if config['data_preparation']['cleaning']['replace_NaN_with_mean']:
        from data_preparation.cleaning import replace_NaN_with_mean
        df = replace_NaN_with_mean(df)

    if config['data_preparation']['store_prepared']['execute']:
        df.to_csv('./tmp/datasets/{}.csv'.format(config['general']['data']['name']))

    if config['data_preparation']['data_split']['execute']:
        if config['data_preparation']['data_split']['validation_set']:
            from util.machine_learning import train_val_test_split
            X_train, y_train, X_test, y_test, X_val, y_val = train_val_test_split(df,
                                                                                  label=config['general']['data']['label'],
                                                                                  split=config['data_preparation']['data_split']['split'],
                                                                                  seed=config['data_preparation']['data_split']['seed'])
        else:
            from util.machine_learning import train_test_split
            X_train, y_train, X_test, y_test = train_test_split(df,
                                                                label=config['general']['data']['label'],
                                                                split=config['data_preparation']['data_split']['split'],
                                                                seed=config['data_preparation']['data_split']['seed'])

    # TODO: exception if X_train, y_train etc is not defined
    # modeling
    if config['modeling']['classification']['execute']:
        from modeling.classification import get_classifier_function
        clf_list = []
        for clf_key in config['modeling']['classification']['classifiers']:
            train_clf = get_classifier_function(clf_key)
            import numpy as np
            print(np.isnan(np.sum(X_train)))
            clf = train_clf(X_train, y_train)
            clf_list.append((clf_key, clf))

    # evaluation
    if config['evaluation']['classification']['execute']:
        from evaluation.scoring import get_metric_function
        scores = []
        for (clf_key, clf) in clf_list:
            from modeling.classification import predict
            if config['data_preparation']['data_split']['validation_set']:
                y_pred_val = predict(clf, X_val)
            y_pred = predict(clf, X_test)
            for metric_key in config['evaluation']['classification']['metrics']:
                score = get_metric_function(metric_key)
                from util.machine_learning import cross_validation
                if config['data_preparation']['data_split']['validation_set']:
                    cv_val_score = cross_validation(score, (y_val, y_pred_val), n=config['evaluation']['classification']['cross_val'])

                cv_score = cross_validation(score, (y_test, y_pred), n=config['evaluation']['classification']['cross_val'])

                scores.append((clf_key, metric_key, cv_score))


        from evaluation.scoring import save_score
        save_score(config['general']['data']['name'], scores, config['evaluation']['classification']['cross_val'])





if os.path.isfile('config.yaml'):
    with open('config.yaml', 'r') as stream:
        try:
            config = yaml.load(stream)
            main(config)
        except yaml.YAMLError as exc:
            print(exc)
else:
    from util.exceptions import NoConfigFileError
    raise NoConfigFileError(None)
