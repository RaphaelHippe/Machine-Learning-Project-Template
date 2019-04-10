import os
from multiprocessing import Pool
from functools import partial
import time
import tqdm


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