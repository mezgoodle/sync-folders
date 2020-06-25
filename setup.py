from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='sync-folders',
    packages=['sync_folders'],
    version='1.0.0',
    license='MIT',
    description='Library for synchronization two folders',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Maxim Zavalniuk',
    author_email='mezgoodle@gmail.com',
    url='https://github.com/mezgoodle/sync-folders',
    download_url='https://github.com/mezgoodle/sync-folders/archive/v1.0.0.tar.gz',
    keywords=[
        'folders',
        'files',
        'synchronization',
        'sync-folders'],
    classifiers=[
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
