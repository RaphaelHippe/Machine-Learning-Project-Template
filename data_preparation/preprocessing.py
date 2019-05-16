import pandas as pd

from util.exceptions import DataFrameTypeError
'''
NAME: apply_pca
PARAMS:
- df: pandas DataFrame
- label: the label (optional)
- n_components: number of prinipal components (optional)
DESCRIPTION: applies sklearns principal components analysis to the given DataFrame
and returns a new DataFrame with containing the principal components and if given
the label.
RETURN: new DataFrame
'''
def apply_pca(df, label=None, n_components=None):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)
    from sklearn.decomposition import PCA
    pca = PCA(n_components=n_components)
    if label == None:
        X = pd.DataFrame(pca.fit_transform(df), columns=['PCA%i' % i for i in range(n_components)], index=df.index)
    else:
        X = pd.DataFrame(pca.fit_transform(df.drop([label], axis=1)), columns=['PCA%i' % i for i in range(n_components)], index=df.index)
        X[label] = df[label]
    return X
