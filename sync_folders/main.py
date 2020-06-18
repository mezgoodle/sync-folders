def read_file(path):
    with open(path, 'r') as f:
        data = f.read()
    return data


def write_file(path):
    with open(path, 'w') as f:
        data = 'some data to be written to the file'
        f.write(data)
