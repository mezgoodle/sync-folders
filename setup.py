from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='sync-folders',
    packages = ['sync_folders'],
    version = '0.1.5',
    license='MIT',
    description = 'Library for synchronization two folders',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author = 'Maxim Zavalniuk',
    author_email = 'mezgoodle@gmail.com',
    url = 'https://github.com/mezgoodle/sync-folders',
    # download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
    keywords = ['folders', 'files', 'synchronization', 'sync-folders'],
)