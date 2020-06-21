#!/usr/bin/python3

import shutil
import os
import sys

# purgelog.py <log-file name> <limit in KB> <logs-files>

if len(sys.argv) < 4:
    raise NameError('Missing arguments')
    exit(1)

file_name = sys.argv[1]
limitize = int(sys.argv[2])
logsNumber = int(sys.argv[3])

if os.path.isfile(file_name):
    logfile_size = os.stat(file_name).st_size
    logfile_size /= 1024

    if logfile_size >= limitize:
        if logsNumber > 0:
            for currentFileNum in range(logsNumber, 1, -1):
                src = str(currentFileNum - 1) + '_' + file_name
                dst = str(currentFileNum) + '_' + file_name
                if os.path.isfile(src):
                    shutil.copyfile(src, dst)
                    print(f"Copied: {src} to {dst}")

            shutil.copyfile(file_name, '1_' + file_name)
            print(f"Copied: {file_name} to 1_{file_name}")
        myfile = open(file_name, 'w')
        myfile.close()
