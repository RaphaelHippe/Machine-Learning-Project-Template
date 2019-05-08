
'''
NAME: calc_accuracy
PARAMS:
- X_test: the test data
- y_test: the test labels
DESCRIPTION:
RETURN: accuracy score
'''
def calc_accuracy(y_test, y_pred):
    from sklearn.metrics import accuracy_score
    return accuracy_score(y_test, y_pred)

'''
NAME: calc_precision
PARAMS:
- X_test: the test data
- y_test: the test labels
DESCRIPTION:
RETURN: precision score
'''
def calc_precision(y_test, y_pred, average=None):
    from sklearn.metrics import precision_score
    return precision_score(y_test, y_pred, average=average)

'''
NAME: calc_recall
PARAMS:
- X_test: the test data
- y_test: the test labels
DESCRIPTION:
RETURN: recall score
'''
def calc_recall(y_test, y_pred, average=None):
    from sklearn.metrics import recall_score
    return recall_score(y_test, y_pred, average=average)

'''
NAME: calc_f1
PARAMS:
- X_test: the test data
- y_test: the test labels
DESCRIPTION:
RETURN: f1 score
'''
def calc_f1(y_test, y_pred, average=None):
    from sklearn.metrics import f1_score
    return f1_score(y_test, y_pred, average=average)


def get_metric_function(metric_key):
    if metric_key == 'acc':
        return calc_accuracy
    elif metric_key == 'f1':
        return calc_f1
    elif metric_key == 'recall':
        return calc_recall
    elif metric_key == 'precision':
        return calc_precision
    else:
        from util.exceptions import UnknownKeyError
        raise UnknownKeyError(metric_key, 'scoring metric')


def save_score(name, scores, cv_n):
    from util.general import to_txt_with_versioning
    file_content = 'Evaluation for {}\n'.format(name)
    file_content += '\n All scores have been cross validated {} times'.format(cv_n)

    for (clf_key, metric_key, cv_score) in scores:
        file_content += '\n {} {} scored: {}'.format(clf_key, metric_key, cv_score)

    to_txt_with_versioning('./tmp/evaluation/{}_eval'.format(name), file_content)
