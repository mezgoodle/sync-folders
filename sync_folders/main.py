from datetime import datetime
import os


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


print(get_files('./')[0])
