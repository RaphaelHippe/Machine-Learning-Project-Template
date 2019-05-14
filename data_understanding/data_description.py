import pandas as pd

from util.exceptions import DataFrameTypeError
from util.general import to_txt_with_versioning

def describe_data(df, name, n, include='all'):
    if not isinstance(df, pd.DataFrame):
        raise DataFrameTypeError('df', df)

    file_content = 'Data description for {}\n'.format(name)

    file_content += df.describe(include=include).T.to_string()

    file_content += '\n\nThe data set has {} columns.'.format(len(df.columns))

    file_content += '\n\nThe data set has {} NaN values.'.format(df.isnull().values.sum())

    file_content += '\n\nDataFrame data types:\n\n'

    file_content += df.dtypes.to_string()

    file_content += '\n\nDataFrame head{}:\n\n'.format(n)

    file_content += df.head(n).to_string()

    file_content += '\n\n DataFrame tail{}:\n\n'.format(n)

    file_content += df.tail(n).to_string()

    to_txt_with_versioning('./tmp/description/{}'.format(name), file_content)
