import os
import time

DAYS = 5
FOLDERS = [
    './test_a',
    './test_b',
    './test_c'
]

TOTAL_DELETED_SIZE = 0 # Total deleted size of all files
TOTAL_DELETED_FILE = 0 # Total deleted files
TOTAL_DELETED_DIRS = 0 # Total deleted empty folders

starttime = time.asctime()

for folder in FOLDERS:
    delete_old_files(folder) # Delete old files
    delete_empty_dir(folder) # Delete empty folders

finishtime = time.asctime()


print(f"START TIME: {starttime}")
print(f"Total deleted size: {TOTAL_DELETED_SIZE/1024/1024} MB")
print(f"Total deleted files: {TOTAL_DELETED_FILE}")
print(f"Total deleted empty folders: {TOTAL_DELETED_DIRS}")
print(f"FINISH TIME: {finishtime}")