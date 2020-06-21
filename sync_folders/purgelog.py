#!/usr/bin/python3

import shutil
import os

# <log-file name> <limit in KB> <logs-files>


def purgelog(*args):
    if len(args) < 3:
        raise NameError('Missing arguments')
        exit(1)

    file_name = args[0]
    limitize = int(args[1])
    logsNumber = int(args[2])

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
