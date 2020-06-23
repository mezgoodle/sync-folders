# Synchronization folders script

Hello everyone! This is the repository of my package on Python "sync-folders".

## Table of contents
  * [Motivation](#motivation)
  * [Build status](#build-status)
  * [Code style](#code-style)
  * [Dependencies](#dependencies)
  * [Features](#features)
  * [Installation](#installation)
  * [Importing](#importing)
  * [Fast usage](#fast-usage)
  * [API](#api)
  * [Code Example](#code-example)
  * [Tests](#tests)
  * [Contributing](#contributing)
  * [License](#license)

## Motivation

Someday I made the script, that synchronizes two folders by date of theirs files. After time I've wanted to create package on [PyPi](https://pypi.org/). Also I've also added some new features for working with files, in addition to **syncing**.

## Build status

Here you can see build status of [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration)/[continuous deployment](https://en.wikipedia.org/wiki/Continuous_deployment):

![Python package](https://github.com/mezgoodle/sync-folders/workflows/Python%20package/badge.svg)
![Upload Python Package](https://github.com/mezgoodle/sync-folders/workflows/Upload%20Python%20Package/badge.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/sync-folders)

## Code style

I'm using [Codacy](https://www.codacy.com/) for automate my code quality.

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/fd161c5c72334c50a06ccfb8d50027ae)](https://www.codacy.com/manual/mezgoodle/sync-folders?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mezgoodle/sync-folders&amp;utm_campaign=Badge_Grade)

## Dependencies

> You can see all dependencies from `requirements.txt` [here](https://github.com/mezgoodle/sync-folders/network/dependencies).

## Features

With my package you can **sync** two folders, **manage** logs files, **delete** empty folders of old files.

## Installation

First install [Python](https://www.python.org/downloads/).

> If you don't have *pip*, [install](https://pip.pypa.io/en/stable/installing/) it.

Then:

```bash
pip install sync-folders --upgrade
```

## Importing

```python
# Import module
from sync_folders import main, purgelog, cleaner
```

## Fast usage

 - Synchronization
```python
main.sync('./path/to/first/dir', './path/to/second/dir')
# Expected creation of `logs.txt`
```

 - Files output
```python
main.files('./path/to/dir')
""" Expected output(example)

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

 - Dirs output
```python
main.dirs('./path/to/dir')
""" Expected output(example)

.venv
test_a
test_b
"""
```

 - Reading the file data
```python
print(main.read_file('./path/to/file'))
""" Expected output(example)

from sync_folders import main, purgelog, cleaner

print(main.read_file('./index.py'))
"""
```

 - Write in the file

 > No append

```python
main.write_file('./path/to/file', 'your text')
```

 - List of the dirs
```python
print(main.list_dir('./path/to/dir'))
""" Expected output(example)

['.git', '.github', '.venv', 'sync_folders', 'tests', 'util']
"""
```

 - List of the files
```python
print(main.list_dir('./path/to/dir'))
""" Expected output(example)

[
  {'name': 'python-package.yml', 'date': 1592564708.6109703, 'date_str': '19 Jun 2020, 11 05'}, 
  {'name': 'python-publish.yml', 'date': 1591772746.2324488, 'date_str': '10 Jun 2020, 07 05'}
]
"""
```

 - Cleaner
```python
cleaner.cleaner(['array', 'of', 'pathes', 'folders'], 'limit_of_day_for_files')
# Expected creation of `logs.txt`
""" Expected output(example)

START TIME: Tue Jun 23 22:01:00 2020
Total deleted size: 0.0 MB
Total deleted files: 0
Total deleted empty folders: 2
FINISH TIME: Tue Jun 23 22:01:00 2020
"""
```

 - Purgelof
```python
purgelog.purgelog('log-file name', '<limit in KB>', '<number of logs-files>')
""" Expected output(example)
Copied: logs.txt to 1_logs.txt
"""
# Expected creation of `1_logs.txt`
```

## API

### caesarEncrypt( value, amount, type )

Name    | Type     | Argument     | Default | Description
--------|----------|--------------|---------|------------
value     | `string` | `<required>` | `null`  | the message to encrypt
amount | `number` | `<required>` | `null`  | the key to encrypt the message with
type | `string` | `<required>` | `null`  | the type of language: latin or cyrillic

### caesarDecrypt( value, amount, type )

Name    | Type     | Argument     | Default | Description
--------|----------|--------------|---------|------------
value     | `string` | `<required>` | `null`  | the message to decrypt
amount | `number` | `<required>` | `null`  | the key to decrypt the message with
type | `string` | `<required>` | `null`  | the type of language: latin or cyrillic

### vigenereEncrypt( text, key, type )

Name    | Type     | Argument     | Default | Description
--------|----------|--------------|---------|------------
text     | `string` | `<required>` | `null`  | the message to encrypt
key | `string` | `<required>` | `null`  | the key to encrypt the message with
type | `string` | `<required>` | `null`  | the type of language: latin or cyrillic

### vigenereDecrypt( text, key, type )

Name    | Type     | Argument     | Default | Description
--------|----------|--------------|---------|------------
text     | `string` | `<required>` | `null`  | the message to decrypt
key | `string` | `<required>` | `null`  | the key to decrypt the message with
type | `string` | `<required>` | `null`  | the type of language: latin or cyrillic


## Code Example

Here you can see small example of ...

```python
```

## Tests

Unit-testing with **pytest**:

:smile:I give you the [link](https://github.com/mezgoodle/sync-folders/actions?query=workflow%3A%22Python+package%22) to [GitHub Actions](https://github.com/features/actions), where you can see all my tests.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Also look at the [CONTRIBUTING.md](https://github.com/mezgoodle/Caesar-and-Vigenere-ciphers/blob/master/CONTRIBUTING.md).

## Credits

Links to videos which helped me to build this project.

 - https://www.youtube.com/watch?v=sb3118xptEM&list=PLg5SS_4L6LYt7Wmh8zBKjZ_ltaoDXSEmk&index=4
 - https://www.youtube.com/watch?v=mjyKFuwXVxY&list=PLg5SS_4L6LYt7Wmh8zBKjZ_ltaoDXSEmk&index=5

## License

![GitHub](https://img.shields.io/github/license/mezgoodle/sync-folders)

MIT © [mezgoodle](https://github.com/mezgoodle)