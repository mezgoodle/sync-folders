#!/bin/python3

import shutil
import os
import sys

# purgelog.py mylog.txt 10 5

if len(sys.argv) < 4:
    raise NameError('Missing arguments')
    exit(1)

file_name  = sys.argv[1]
limitize   = int(sys.argv[2])
logsNumber = int(sys.argv[3])

