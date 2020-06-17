from sync_folders import main


def test_creation():
    assert main.test_create_file(PosixPath('PYTEST_TMPDIR/test_create_file0')).read_text() == "CONTENT"
    assert len(list(PosixPath('PYTEST_TMPDIR/test_create_file0').iterdir())) == 1
