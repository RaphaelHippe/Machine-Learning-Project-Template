
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
NAME: calc_precision_recall
PARAMS:
- X_test: the test data
- y_test: the test labels
DESCRIPTION:
RETURN: accuracy score
'''
def calc_precision_recall(y_test, y_pred, average=None):
    from sklearn.metrics import precision_score, recall_score
    precision = precision_score(y_test, y_pred, average=average)
    recall = recall_score(y_test, y_pred, average=average)
    return (precision, recall)

'''
NAME: calc_f1
PARAMS:
- X_test: the test data
- y_test: the test labels
DESCRIPTION:
RETURN: accuracy score
'''
def calc_f1(y_test, y_pred, average=None):
    from sklearn.metrics import f1_score
    return f1_score(y_test, y_pred, average=average)
