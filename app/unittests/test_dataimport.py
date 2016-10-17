import unittest
import datetime
from core.config.dataImportConfig import DataImportConfig

class DataImportTest(unittest.TestCase):

    def test_insertKeypressData(self):
        size = DataImportConfig().importKeypressData("Alex", "Super summer Event", "here are some comments", datetime.datetime.now())
        self.assertEqual(size, 24)

    def test_importClick(self):
        size = DataImportConfig().importClick("Alex", "Super summer Event", "here are some comments", datetime.datetime.now())
        self.assertEqual(size, 8)

    def test_importTimed(self):
        size = DataImportConfig().importTimed("Alex", "Super summer Event", "here are some comments", datetime.datetime.now())
        self.assertEqual(size, 21)

    def test_importTsharkThroughput(self):
        size = DataImportConfig().importTsharkThroughput("Alex", "Super summer Event", "here are some comments", datetime.datetime.now())
        self.assertEqual(size, 67)

    def test_importMultiIncludeThroughput(self):
        size = DataImportConfig().importMultiIncludeThroughput("Alex", "Super summer Event", "here are some comments", datetime.datetime.now())
        self.assertEqual(size, 77)

    def test_importMultiExcludeThroughput(self):
        size = DataImportConfig().importMultiExcludeThroughput("Alex", "Super summer Event", "here are some comments", datetime.datetime.now())
        self.assertEqual(size, 77)

    def test_importMultiExcludeProtocol(self):
        size = DataImportConfig().importMultiExcludeProtocol("Alex", "Super summer Event", "here are some comments", datetime.datetime.now())
        self.assertEqual(size, 77)

    def test_importMultiIncludeProtocol(self):
        size = DataImportConfig().importMultiIncludeProtocol("Alex", "Super summer Event", "here are some comments", datetime.datetime.now())
        self.assertEqual(size, 77)

    def test_importTsharkProtocol(self):
        size = DataImportConfig().importTsharkProtocol("Alex", "Super summer Event", "here are some comments", datetime.datetime.now())
        self.assertEqual(size, 67)


if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_dataimport
