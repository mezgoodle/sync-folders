import os
import time
from sync_folders import main


def delete_old_files(folder, ageTime):
    logs = ''
    global TOTAL_DELETED_FILE
    global TOTAL_DELETED_SIZE
    for path, dirs, files in os.walk(folder):
        for file in files:
            fileName = os.path.join(path, file)  # get Full path to file
            fileTime = os.path.getmtime(fileName)
            if fileTime < ageTime:
                sizeFile = os.path.getsize(fileName)
                TOTAL_DELETED_SIZE += sizeFile
                TOTAL_DELETED_FILE += 1
                logs += f"Deleting file: {fileName}" + '\n'
                os.remove(fileName)
    return logs


def delete_empty_dir(folder, logs):
    logs_in = logs
    global TOTAL_DELETED_DIRS
    empty_folders_in_this_run = 0
    for path, dirs, files in os.walk(folder):
        if not dirs and not files:
            TOTAL_DELETED_DIRS += 1
            empty_folders_in_this_run += 1
            logs_in += f"Deleting empty dir: {path}" + '\n'
            os.rmdir(path)
    if empty_folders_in_this_run > 0:
        delete_empty_dir(folder, logs_in)
    return logs_in


TOTAL_DELETED_SIZE = 0  # Total deleted size of all files
TOTAL_DELETED_FILE = 0  # Total deleted files
TOTAL_DELETED_DIRS = 0  # Total deleted empty folders


def cleaner(FOLDERS, DAYS):
    logs = ''
    nowTime = time.time()                    # Get current time in seconds
    ageTime = nowTime - 60 * 60 * 24 * DAYS  # Minus DAYS in seconds
    starttime = time.asctime()
    for folder in FOLDERS:
        logs += delete_old_files(folder, ageTime)      # Delete old files
        logs += delete_empty_dir(folder, '')           # Delete empty folders
    finishtime = time.asctime()

    print(f"START TIME: {starttime}")
    print(f"Total deleted size: {TOTAL_DELETED_SIZE/1024/1024} MB")
    print(f"Total deleted files: {TOTAL_DELETED_FILE}")
    print(f"Total deleted empty folders: {TOTAL_DELETED_DIRS}")
    print(f"FINISH TIME: {finishtime}")

    main.write_file('./logs.txt', logs)

cleaner(['test_a', 'test_b'], 0)