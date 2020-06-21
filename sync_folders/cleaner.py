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

nowTime = time.time()             # Get current time in seconds
ageTime = nowTime - 60*60*24*DAYS # Minus DAYS in seconds

def delete_old_files(folder):
    global TOTAL_DELETED_FILE
    global TOTAL_DELETED_SIZE
    for path, dirs, files in os.walk(folder):
        for file in files:
            fileName = os.path.join(path, file) # get Full path to file
            fileTime = os.path.getmtime(fileName)
            if fileTime < ageTime:
                sizeFile = os.path.getsize(fileName)
                TOTAL_DELETED_SIZE += sizeFile
                TOTAL_DELETED_FILE += 1
                print(f"Deleting file: {fileName}")
                os.remove(fileName)

def delete_empty_dir(folder):
    global TOTAL_DELETED_DIRS
    for path, dirs, files in os.walk(folder):
        if not dirs and not files:
            TOTAL_DELETED_DIRS += 1
            print(f"Deleting empty dir: {path}")
            os.rmdir(path)

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