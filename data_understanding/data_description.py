import pandas as pd

from util.exceptions import DataFrameTypeError
from util.general import to_txt

def describe_data(df, name, include='all'):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)

    file_content = 'Data description for {}\n'.format(name)

    file_content += df.describe(include=include).T.to_string()

    file_content += '\n\nThe data set has {} columns.'.format(len(df.columns))

    file_content += '\n\nThe data set has {} NaN values.'.format(df.isnull().values.sum())

    to_txt('./tmp/datasets/{}_description'.format(name), file_content)
