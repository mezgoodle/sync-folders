from sync_folders import main


def test_reading():
    assert main.read_file('./tests/text.txt') == 'text for the test'
