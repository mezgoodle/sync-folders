# imports
from datetime import datetime
import os
import shutil


# Function for converting time from timestamp
def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y, %H %M')
    return formated_date


# Function for reading the single file
def read_file(path=None):
    if not path:
        raise NameError('Required path to the file')
    with open(path, 'r') as f:
        data = f.read()
    return data


# Function for writing data in the single file
def write_file(path=None, data=None):
    if not path or not data:
        raise NameError('Required path to the file and data')
    with open(path, 'w') as f:
        f.write(str(data))


# Function that returns list of dirs
def list_dir(path=None):
    if not path:
        raise NameError('Required path to dir')
    dirs = []
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            dirs.append(entry)
    return dirs


# Function that returns list of files
def get_files(path):
    if not path:
        raise NameError('Required path to dir')
    files = []
    dir_entries = os.scandir(path)
    for entry in dir_entries:
        if entry.is_file():
            info = entry.stat()
            files.append({
                'name': entry.name,
                'date': info.st_mtime,
                'date_str': convert_date(info.st_mtime),
            })
    return files


# Main function for synchronize two folders
def sync(path_a=None, path_b=None):
    if not path_a or not path_b:
        raise NameError('Required path to both dirs')
    logs = ''
    files_in_a = get_files(path_a)
    files_in_b = get_files(path_b)
    same_files = []
    for file_a in files_in_a:
        for file_b in files_in_b:
            if file_b['name'] == file_a['name']:
                # compare dates
                if file_b['date'] < file_a['date']:
                    # change
                    shutil.copy2(path_a + '/' + file_a['name'], path_b)
                    logs += f"Change {file_a['name']} in {path_b}" + '\n'
            same_files.append(file_b['name'])
    for file_a in files_in_a:
        if not file_a['name'] in same_files:
            # move to b
            shutil.copy2(path_a + '/' + file_a['name'], path_b)
            logs += f"Create {file_a['name']} in {path_b}" + '\n'

    write_file('./logs.txt', logs)


# Function that prints list of files and their last modified date
def files(path=None):
    files = get_files(path)
    for file_ in files:
        print(f"{file_['name']}\t Last Modified: {file_['date_str']}")


# Function that prints list of dirs
def dirs(path):
    dirs = list_dir(path)
    for dir_ in dirs:
        print(dir_)
