class DataSplitError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr('The sum of the split parameter does not add up to 1.0 instead got {}'.format(self.value))

class DataFrameTypeError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr('The type of the param "{}" is not of type pd.DataFrame.'.format(self.value))
