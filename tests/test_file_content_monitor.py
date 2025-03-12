import pathlib
import unittest

from src.file_content_monitor import FileContentMonitor


class MockProducer:
    def send(self, topic, value):
        pass


class TestFileContentMonitor(unittest.TestCase):
    producer = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.producer = MockProducer()
        cls.file_path = pathlib.Path(__file__).parent / "./test.txt"
        cls.nonempty_raw_content = ".123inside\nfile"

    def setUp(self):
        super().setUp()

        self.file_content_monitor = FileContentMonitor(self.producer)

    def test_should_get_empty_content_when_updated_with_empty_content(self):
        self.file_content_monitor.update("")

        assert self.file_content_monitor.content == ""

    def test_should_get_content_when_updated_with_nonempty_content(self):
        self.file_content_monitor.update(self.nonempty_raw_content)

        assert self.nonempty_raw_content == self.file_content_monitor.content


if __name__ == "__main__":
    unittest.main()
