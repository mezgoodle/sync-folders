# Synchronization folders package

Hello everyone! This is the repository of my package on Python "sync-folders".

## Table of contents

* [Table of contents](#table-of-contents)
* [Motivation](#motivation)
* [Build status](#build-status)
* [Code style](#code-style)
* [Dependencies](#dependencies)
* [Features](#features)
* [Installation](#installation)
* [Importing](#importing)
* [Fast usage](#fast-usage)
  + [Synchronization](#synchronization)
  + [Files output](#files-output)
  + [Dirs output](#dirs-output)
  + [Reading the file data](#reading-the-file-data)
  + [Write in the file](#write-in-the-file)
  + [List of the dirs](#list-of-the-dirs)
  + [List of the files](#list-of-the-files)
  + [Read zip-archive](#read-zip-archive)
  + [List of the elements in archive](#list-of-the-elements-in-archive)
  + [Extract element from archive](#extract-element-from-archive)
  + [Create archive](#create-archive)
  + [Cleaner](#cleaner)
  + [Purgelog](#purgelog)
* [API](#api)
  + [main.sync( path_a, path_b )](#mainsync--path-a--path-b--)
  + [main.files( path )](#mainfiles--path--)
  + [main.dirs( path )](#maindirs--path--)
  + [main.read_file( path )](#mainread-file--path--)
  + [main.write_file( path, data )](#mainwrite-file--path--data--)
  + [main.list_dir( path )](#mainlist-dir--path--)
  + [main.get_files( path )](#mainget-files--path--)
  + [main.read_zip( path )](#mainread-zip--path--)
  + [main.files_in_zip( path )](#mainfiles-in-zip--path--)
  + [main.extract( path_to_zip, path_to_file )](#mainextract--path-to-zip--path-to-file--)
  + [main.create_zip( files, path)](#maincreate-zip--files--path-)
  + [cleaner.cleaner( folders, limit )](#cleanercleaner--folders--limit--)
  + [purgelog.purgelog( log-file, limit, number )](#purgelogpurgelog--log-file--limit--number--)
* [Code Example](#code-example)
* [Tests](#tests)
* [Contributing](#contributing)
* [Credits](#credits)
* [License](#license)

## Motivation

Someday I made the script, that synchronizes two folders by date of theirs files. After time I've wanted to create package on [PyPi](https://pypi.org/). Also I've added some new features for work with files, in addition to **syncing**.

## Build status

Here you can see build status of [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration)/[continuous deployment](https://en.wikipedia.org/wiki/Continuous_deployment):

![Python package](https://github.com/mezgoodle/sync-folders/workflows/Python%20package/badge.svg)
![Lint Code Base](https://github.com/mezgoodle/sync-folders/workflows/Lint%20Code%20Base/badge.svg)
![Upload Python Package](https://github.com/mezgoodle/sync-folders/workflows/Upload%20Python%20Package/badge.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/sync-folders)

## Code style

I'm using [Codacy](https://www.codacy.com/) for automate my code quality.

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/fd161c5c72334c50a06ccfb8d50027ae)](https://www.codacy.com/manual/mezgoodle/sync-folders?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mezgoodle/sync-folders&amp;utm_campaign=Badge_Grade)

## Dependencies

> You can see all dependencies from `requirements.txt` [here](https://github.com/mezgoodle/sync-folders/network/dependencies).

## Features

With my package you can **sync** two folders, **manage** logs files, **delete** empty folders and old files, read and create **zip-archives**.

## Installation

First install [Python](https://www.python.org/downloads/).

> If you don't have *pip*, [install](https://pip.pypa.io/en/stable/installing/) it.

Then type in terminal:

```bash
pip install sync-folders --upgrade
```

## Importing

```python
# Import module
from sync_folders import main, purgelog, cleaner
```

## Fast usage

Example of usage this module

### Synchronization

```python
main.sync('./test_a', './test_b')
# Expected creation of `logs.txt`
```

### Files output

```python
main.files('./')
""" Expected output

.gitattributes   Last Modified: 18 Jun 2020, 08 52
.gitignore       Last Modified: 10 Jun 2020, 06 39
CONTRIBUTING.md  Last Modified: 23 Jun 2020, 12 26
LICENSE  Last Modified: 09 Jun 2020, 18 10
README.md        Last Modified: 23 Jun 2020, 18 20
requirements.txt         Last Modified: 10 Jun 2020, 15 00
setup.cfg        Last Modified: 10 Jun 2020, 07 08
setup.py         Last Modified: 21 Jun 2020, 14 03
_config.yml      Last Modified: 10 Jun 2020, 09 28
"""
```

### Dirs output

```python
main.dirs('./tests')
""" Expected output

.venv
test_a
test_b
"""
```

### Reading the file data

```python
print(main.read_file('./index.py'))
""" Expected output

from sync_folders import main, purgelog, cleaner

print(main.read_file('./index.py'))
"""
```

### Write in the file

 > Not an appending

```python
main.write_file('./test.txt', 'your text')
```

### List of the dirs

```python
main.list_dir('./')
""" Expected result

['.git', '.github', '.venv', 'sync_folders', 'tests', 'util']
"""
```

### List of the files

```python
main.get_files('./')
""" Expected result

[
  {'name': 'python-package.yml', 'date': 1592564708.6109703, 'date_str': '19 Jun 2020, 11 05'}, 
  {'name': 'python-publish.yml', 'date': 1591772746.2324488, 'date_str': '10 Jun 2020, 07 05'}
]
"""
```

### Read zip-archive

```python
main.read_zip('./test.zip')
""" Expected output

test_a/
            Compress size: 0.0 in KB
            Filesize: 0.0 in KB
test_a/test.docx
            Compress size: 8.490234375 in KB
            Filesize: 11.1572265625 in KB
test_b/
            Compress size: 0.0 in KB
            Filesize: 0.0 in KB
"""
```

### List of the elements in archive

```python
main.files_in_zip('test.zip')
""" Expected result

['test_a/', 'test_a/test.docx', 'test_b/']
"""
```

### Extract element from archive

```python
main.extract('test.zip', 'test_a/test.docx')
# Expected creation of `test_a/test.docx`
```

### Create archive

```python
main.create_zip(['_config.yml', 'LICENSE', 'setup.py'], './test.zip')
# Expected creation of `test.zip`
```

### Cleaner

```python
cleaner.cleaner(['./test_a', './test_a/test_c', './test_b'], 5)
# Expected creation of `logs.txt`
""" Expected output

START TIME: Tue Jun 23 22:01:00 2020
Total deleted size: 0.0 MB
Total deleted files: 0
Total deleted empty folders: 3
FINISH TIME: Tue Jun 23 22:01:00 2020
"""
```

### Purgelog

```python
purgelog.purgelog('./logs.txt', 5, 2)
""" Expected output
Copied: logs.txt to 1_logs.txt
"""
# Expected creation of `1_logs.txt`
```

## API

### main.sync( path_a, path_b )

Name    | Type     | Argument     | Default | Description
--------|----------|--------------|---------|------------
path_a | `string` | `<required>` | `None`  | the path to the directory
path_b | `string` | `<required>` | `None`  | the path to the directory

### main.files( path )

Name    | Type     | Argument     | Default | Description
--------|----------|--------------|---------|------------
path    | `string` | `<required>` | `None`  | the path to the directory

### main.dirs( path )

Name    | Type     | Argument     | Default | Description
--------|----------|--------------|---------|------------
path     | `string` | `<required>` | `None`  | the path to the directory

### main.read_file( path )

Name    | Type     | Argument     | Default | Description
--------|----------|--------------|---------|------------
path   | `string` | `<required>` | `None`  | the path to the file

### main.write_file( path, data )

Name    | Type     | Argument     | Default | Description
--------|----------|--------------|---------|------------
path   | `string` | `<required>` | `None`  | the path to the file
data | `string` | `<required>` | `None`  | the content

### main.list_dir( path )

Name    | Type     | Argument     | Default | Description
--------|----------|--------------|---------|------------
path     | `string` | `<required>` | `None`  | the path to the directory

### main.get_files( path )

Name    | Type     | Argument     | Default | Description
--------|----------|--------------|---------|------------
path    | `string` | `<required>` | `None`  | the path to the directory

### main.read_zip( path )

Name    | Type     | Argument     | Default | Description
--------|----------|--------------|---------|------------
path    | `string` | `<required>` | `None`  | the path to the archive

### main.files_in_zip( path )

Name    | Type     | Argument     | Default | Description
--------|----------|--------------|---------|------------
path    | `string` | `<required>` | `None`  | the path to the archive

### main.extract( path_to_zip, path_to_file )

Name    | Type     | Argument     | Default | Description
--------|----------|--------------|---------|------------
path_to_zip    | `string` | `<required>` | `None`  | the path to the archive
path_to_file    | `string` | `<not required>` | `None`  | the path to the need file for extracting

### main.create_zip( files, path)

Name    | Type     | Argument     | Default | Description
--------|----------|--------------|---------|------------
files    | `list` | `<required>` | `None`  | the list of pathes to the files for archiving
path    | `string` | `<required>` | `None`  | the path to the new archive

### cleaner.cleaner( folders, limit )

Name    | Type     | Argument     | Default | Description
--------|----------|--------------|---------|------------
folders     | `list` | `<required>` | `None`  | the array of the folders
limit | `int` | `<required>` | `None`  | the limit of the days for comparing

### purgelog.purgelog( log-file, limit, number )

Name    | Type     | Argument     | Default | Description
--------|----------|--------------|---------|------------
log-file     | `string` | `<required>` | `None`  | the path to the log-file
limit | `int` | `<required>` | `None`  | the limit of the maximum memory
number | `int` | `<required>` | `None`  | the number of the maximum available number of the logs file

## Code Example

Here you can see the function, that syncs two folders

```python
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
```

## Tests

Unit-testing with **pytest**:

:smile:I give you the [link](https://github.com/mezgoodle/sync-folders/actions?query=workflow%3A%22Python+package%22) to [GitHub Actions](https://github.com/features/actions), where you can see all my tests.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Also look at the [CONTRIBUTING.md](https://github.com/mezgoodle/Caesar-and-Vigenere-ciphers/blob/master/CONTRIBUTING.md).

## Credits

Links to videos and articles which helped me to build this project:

 - https://realpython.com/working-with-files-in-python/
 - https://www.youtube.com/watch?v=sb3118xptEM&list=PLg5SS_4L6LYt7Wmh8zBKjZ_ltaoDXSEmk&index=4
 - https://www.youtube.com/watch?v=mjyKFuwXVxY&list=PLg5SS_4L6LYt7Wmh8zBKjZ_ltaoDXSEmk&index=5

## License

![GitHub](https://img.shields.io/github/license/mezgoodle/sync-folders)

MIT © [mezgoodle](https://github.com/mezgoodle)
