from sync_folders import main
from util import consts


def test_reading():
    assert main.read_file(consts.TEST_PATH) == 'text for the test'
    main.write_file(consts.TEST_PATH)
    assert main.read_file(
        consts.TEST_PATH) == 'some data to be written to the file'


def test_dir():
    print(main.list_dir(consts.TEST_DIR_PATH))
    assert main.list_dir(consts.TEST_DIR_PATH) == consts.TEST_DIR_LIST
