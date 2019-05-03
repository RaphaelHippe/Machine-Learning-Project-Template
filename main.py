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
        describe_data(df, config['general']['data']['name'])
    # plots
    if config['data_understanding']['plots']['execute']:
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
                            columns=config['data_understanding']['plots']['histograms']['columns'],
                            label=config['general']['data']['label'],
                            format=config['data_understanding']['plots']['histograms']['format'])

    # data preparation
    # from util.machine_learning import extract_X_y
    # X, y = extract_X_y(df, label=config['general']['data']['label'])

    if config['data_preparation']['encodings']['execute']:
        from data_preparation.encodings import apply_leave_one_out_encoding
        df = apply_leave_one_out_encoding(df, categorical_columns=config['data_preparation']['encodings']['categorical_columns'], label=config['general']['data']['label'])

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





with open('config.yaml', 'r') as stream:
    try:
        config = yaml.load(stream)
        main(config)
    except yaml.YAMLError as exc:
        print(exc)
