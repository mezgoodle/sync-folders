from datetime import datetime
import os
import shutil


def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y, %H %M')
    return formated_date


def read_file(path):
    with open(path, 'r') as f:
        data = f.read()
    return data


def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


def list_dir(path):
    dirs = []
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            dirs.append(entry)
    return dirs


def get_files(path):
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


def sync(path_a, path_b):
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


def files(path):
    files = get_files(path)
    for file_ in files:
        print(f"{file_['name']}\t Last Modified: {file_['date_str']}")


def dirs(path):
    dirs = list_dir(path)
    for dir_ in dirs:
        print(dir_)
