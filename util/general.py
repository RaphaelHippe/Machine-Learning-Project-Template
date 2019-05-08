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
    if os.path.isfile(file):
        if file.find('_') == -1:
            new_file = file + '_0'
        else:
            curr_version = file.split('_')[-1]
            new_file = rreplace(file, '_{}'.format(curr_version), '_{}'.format(int(curr_version)+1), 1)
    else:
        new_file = file + '_0'
    to_txt(new_file, str)


# '''
# NAME: import_from_uri
# PARAMS:
# - file: file path
# - str: the string to save in the txt file
# DESCRIPTION: Creates a new file with the path "file" and "str" as content.
# RETURN: -
# '''
# def import_from_uri(uri, absl=False):
#     import os
#     import imp
# 	if not absl:
#         uri = os.path.normpath(os.path.join(os.path.dirname(__file__), uri))
# 	path, fname = os.path.split(uri)
# 	mname, ext = os.path.splitext(fname)
#
# 	no_ext = os.path.join(path, mname)
#
# 	if os.path.exists(no_ext + '.pyc'):
# 		try:
# 			return imp.load_compiled(mname, no_ext + '.pyc')
# 		except:
# 			pass
# 	if os.path.exists(no_ext + '.py'):
# 		try:
# 			return imp.load_source(mname, no_ext + '.py')
# 		except:
# 			pass
