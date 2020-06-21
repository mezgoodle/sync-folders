from sync_folders import main, purgelog
from util import consts


def test_reading():
    assert main.read_file(consts.TEST_PATH) == consts.TEST_TEXT
    main.write_file(consts.TEST_PATH, consts.TEST_CHANGE_TEXT)
    assert main.read_file(consts.TEST_PATH) == consts.TEST_CHANGE_TEXT


def test_dir():
    assert set(
        main.list_dir(
            consts.TEST_DIR_PATH)) == set(
        consts.TEST_DIR_LIST)
    assert len(main.get_files(consts.TEST_DIR_PATH)) == consts.TEST_NUM


def test_sync():
    main.sync(consts.TEST_DIR_PATH_1, consts.TEST_DIR_PATH_2)
    assert main.read_file(
        consts.TEST_DIR_PATH_1 +
        consts.TEST_FILE_PATH) == main.read_file(
        consts.TEST_DIR_PATH_2 +
        consts.TEST_FILE_PATH)
    assert main.read_file(
        consts.TEST_DIR_PATH_1 +
        consts.TEST_FILE_PATH_1) == main.read_file(
        consts.TEST_DIR_PATH_2 +
        consts.TEST_FILE_PATH_1)
    main.sync(consts.TEST_DIR_PATH_2, consts.TEST_DIR_PATH_1)
    assert len(
        main.get_files(
            consts.TEST_DIR_PATH_1)) == len(
        main.get_files(
            consts.TEST_DIR_PATH_2))
    assert main.read_file(consts.TEST_FILE_PATH_2) != ''


def test_purgelog():
    main.write_file(consts.TEST_PURGE_PATH, consts.DATA)
    assert consts.DATA == main.read_file(consts.TEST_PURGE_PATH)
    purgelog.purgelog(consts.TEST_PURGE_PATH, 5, 2)
    assert consts.DATA == main.read_file(consts.TEST_PURGE_PATH_1)
