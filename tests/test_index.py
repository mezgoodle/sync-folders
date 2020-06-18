from sync_folders import main
from util import consts


def test_reading():
    assert main.read_file(consts.TEST_PATH) == consts.TEST_TEXT
    main.write_file(consts.TEST_PATH)
    assert main.read_file(consts.TEST_PATH, consts.TEST_CHANGE_TEXT) == consts.TEST_CHANGE_TEXT


def test_dir():
    assert set(main.list_dir(consts.TEST_DIR_PATH)) == set(consts.TEST_DIR_LIST)
    assert set(main.files_in_dir(consts.TEST_DIR_PATH)) == set(consts.TEST_FILES)
