
'''
NAME: train_clf
PARAMS:
- clf: the classifier object to train
- X_train: the training data
- y_train: the training labels
DESCRIPTION:
RETURN: the trained classifier object
'''
def train_clf(clf, X_train, y_train):
    clf.fit(X_train, y_train)
    return clf

'''
NAME: predict
PARAMS:
- clf: the classifier object to train
- X_train: the test data
DESCRIPTION:
RETURN: the trained classifier object
'''
def predict(clf, X_train):
    return clf.predict(X_train)

'''
NAME: train_sgd_clf
PARAMS:
- X_train: the training data
- y_train: the training labels
DESCRIPTION:
RETURN: the trained classifier object
'''
def train_sgd_clf(X_train, y_train):
    from sklearn.linear_model import SGDClassifier
    return train_clf(SGDClassifier(), X_train, y_train)

'''
NAME: train_knn_clf
PARAMS:
- X_train: the training data
- y_train: the training labels
DESCRIPTION:
RETURN: the trained classifier object
'''
def train_knn_clf(X_train, y_train):
    from sklearn.neighbors import KNeighborsClassifier
    return train_clf(KNeighborsClassifier(), X_train, y_train)

'''
NAME: train_gp_clf
PARAMS:
- X_train: the training data
- y_train: the training labels
DESCRIPTION:
RETURN: the trained classifier object
'''
def train_gp_clf(X_train, y_train):
    from sklearn.gaussian_process import GaussianProcessClassifier
    return train_clf(GaussianProcessClassifier(), X_train, y_train)

'''
NAME: train_gnb_clf
PARAMS:
- X_train: the training data
- y_train: the training labels
DESCRIPTION:
RETURN: the trained classifier object
'''
def train_gnb_clf(X_train, y_train):
    from sklearn.naive_bayes import GaussianNB
    return train_clf(GaussianNB(), X_train, y_train)

'''
NAME: train_mnb_clf
PARAMS:
- X_train: the training data
- y_train: the training labels
DESCRIPTION:
RETURN: the trained classifier object
'''
def train_mnb_clf(X_train, y_train):
    from sklearn.naive_bayes import MultinomialNB
    return train_clf(MultinomialNB(), X_train, y_train)

'''
NAME: train_cnb_clf
PARAMS:
- X_train: the training data
- y_train: the training labels
DESCRIPTION:
RETURN: the trained classifier object
'''
def train_cnb_clf(X_train, y_train):
    from sklearn.naive_bayes import ComplementNB
    return train_clf(ComplementNB(), X_train, y_train)

'''
NAME: train_bnb_clf
PARAMS:
- X_train: the training data
- y_train: the training labels
DESCRIPTION:
RETURN: the trained classifier object
'''
def train_bnb_clf(X_train, y_train):
    from sklearn.naive_bayes import BernoulliNB
    return train_clf(BernoulliNB(), X_train, y_train)

'''
NAME: train_adaboost_clf
PARAMS:
- X_train: the training data
- y_train: the training labels
DESCRIPTION:
RETURN: the trained classifier object
'''
def train_adaboost_clf(X_train, y_train):
    from sklearn.ensemble import AdaBoostClassifier
    return train_clf(AdaBoostClassifier(), X_train, y_train)

'''
NAME: train_random_forest_clf
PARAMS:
- X_train: the training data
- y_train: the training labels
DESCRIPTION:
RETURN: the trained classifier object
'''
def train_random_forest_clf(X_train, y_train):
    from sklearn.ensemble import RandomForestClassifier
    return train_clf(RandomForestClassifier(), X_train, y_train)
