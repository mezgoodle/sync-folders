from sync_folders import main


def test_creation():
    assert main.test_create_file('./').read_text() == CONTENT
    assert len(list('./'.iterdir())) == 1
