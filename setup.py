from setuptools import setup

setup(
    name='sync-folders',
    packages = ['sync-folders'],
    package_dir={'': 'src'},
    version = '0.1.2',
    license='MIT',
    description = 'Library for synchronization two folders',
    author = 'Maxim Zavalniuk',
    author_email = 'mezgoodle@gmail.com',
    url = 'https://github.com/mezgoodle/sync-folders',
    # download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
    keywords = ['folders', 'files', 'synchronization', 'sync-folders'],
)