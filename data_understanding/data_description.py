import pandas as pd

from util.exceptions import DataFrameTypeError
from util.general import to_txt

def describe_data(df, name):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df')

    file_content = 'Data description for {}\n'.format(name)

    file_content += df.describe().T.to_string()

    file_content += '\n\nThe data set has {} columns.'.format(len(df.columns))

    file_content += '\n\nThe data set has {} NaN values.'.format(df.isnull().values.sum())

    to_txt('./tmp/datasets/{}_description'.format(name), file_content)
