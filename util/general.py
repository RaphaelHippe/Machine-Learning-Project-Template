import os
# from multiprocessing import Pool
# from functools import partial
# import time
# import tqdm


'''
NAME: create_folder
PARAMS:
- dir: the path of the directory to create
DESCRIPTION: Creates the directory if it does not exist already.
RETURN: -
'''
def create_folder(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

'''
NAME: create_workspace
PARAMS:
-
DESCRIPTION: creates a workspace in tmp folder wich is ignored by git. Created data sets,
images and evaluation results can be found in the respective subfolders.
NOTE: Call this from the root main.py only
RETURN: -
'''
def create_workspace():
    create_folder('./tmp')
    create_folder('./tmp/datasets')
    create_folder('./tmp/images')
    create_folder('./tmp/evaluation')

'''
NAME: to_file_save_name
PARAMS:
- str: the string to manipulate
DESCRIPTION: Converts all "/" and "." within the string to "_"
RETURN: the manipulated string
'''
def to_file_save_name(str):
    return str.replace('/', '_').replace('.', '_')

'''
NAME: rreplace
PARAMS:
- s: string to operate on
- old: part of the string to be replaced
- new: string to replace old with
- occurrence: how many times the old string is replaced with the new string
DESCRIPTION: TODO
RETURN: -
'''
def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

'''
NAME: to_txt
PARAMS:
- file: file path
- str: the string to save in the txt file
DESCRIPTION: Creates a new file with the path "file" and "str" as content.
RETURN: -
'''
def to_txt(file, str):
    f = open('{}.txt'.format(file),'w')
    f.write(str)
    f.close()

'''
NAME: to_txt_with_versioning
PARAMS:
- file: file path
- str: the string to save in the txt file
DESCRIPTION: Always creates a new file with the path "file" and "str" as content.
If a file with this name already excists a new file with the suffix "_x" with x being
a upwards counting number is created.
RETURN: -
'''
def to_txt_with_versioning(file, str):
    if not os.path.isfile(file + '.txt') and not file.find('_v') == -1:
        to_txt(file, str)
    elif file.find('_v') == -1:
        to_txt_with_versioning(file + '_v0', str)
    else:
        curr_version = file.split('_v')[-1]
        new_file = rreplace(file, '_v{}'.format(curr_version), '_v{}'.format(int(curr_version)+1), 1)
        to_txt_with_versioning(new_file, str)

def create_config_yaml():
    from collections import OrderedDict
    import yaml
    def ordered_dict_representer(self, value):  # can be a lambda if that's what you prefer
        return self.represent_mapping('tag:yaml.org,2002:map', value.items())
    yaml.add_representer(OrderedDict, ordered_dict_representer)
    config = OrderedDict(
        general = OrderedDict(
            data = OrderedDict(
                path = 'path/to/dataset/from/project/root',
                type = 'csv',
                label = 'y',
                name = 'dataset_name'
            )
        ),
        data_understanding = OrderedDict(
            description = OrderedDict(
                execute = False,
                include = 'all',
                n = 5
            ),
            plots = OrderedDict(
                execute = False,
                histograms = OrderedDict(
                    execute = False,
                    columns = -1,
                    format = 'png'
                ),
                boxplots = OrderedDict(
                    execute = False,
                    columns = -1,
                    format = 'png'
                )
            )
        ),
        data_preparation = OrderedDict(
            drop_columns = OrderedDict(
                execute = False,
                cols = ['a']
            ),
            encodings = OrderedDict(
                execute = False,
                encoding = 'LeaveOneOut',
                categorical_columns = ['a', 'b']
            ),
            data_split = OrderedDict(
                execute = False,
                validation_set = False,
                split = [0.8, 0.2],
                seed = None
            ),
        ),
        modeling = OrderedDict(
            classification = OrderedDict(
                execute = False,
                classifiers = ['knn']
            )
        ),
        evaluation = OrderedDict(
            classification = OrderedDict(
                execute = False,
                cross_val = 5,
                metrics = ['acc']
            )
        )
    )
    with open('config.yaml', 'w') as outfile:
        yaml.dump(config, outfile, default_flow_style=False)
