import unittest
from datetime import datetime
from core.config.dataImportConfig import DataImportConfig

class DataImportTest(unittest.TestCase):
    now = datetime.now()
    nowString = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')

    def test_1insertKeypressData(self):
        size = DataImportConfig().importKeypressData("Alex", "Super summer Event", "here are some comments", self.nowString)
        self.assertEqual(size, 46)

    def test_2importClick(self):
        size = DataImportConfig().importClick("Alex", "Super summer Event", "here are some comments", self.nowString)
        self.assertEqual(size, 12)

    def test_3importTimed(self):
        size = DataImportConfig().importTimed("Alex", "Super summer Event", "here are some comments", self.nowString)
        self.assertEqual(size, 34)

    def test_4importMultiExcludeThroughput(self):
        size = DataImportConfig().importMultiExcludeThroughput("Alex", "Super summer Event", "here are some comments", self.nowString)
        self.assertEqual(size, 128)

    def test_5importMultiExcludeProtocol(self):
        size = DataImportConfig().importMultiExcludeProtocol("Alex", "Super summer Event", "here are some comments", self.nowString)
        self.assertEqual(size, 128)

    def test_6importMultiIncludeThroughput(self):
        size = DataImportConfig().importMultiIncludeThroughput("Alex", "Super summer Event", "here are some comments", self.nowString)
        self.assertEqual(size, 128)

    def test_7importMultiIncludeProtocol(self):
        size = DataImportConfig().importMultiIncludeProtocol("Alex", "Super summer Event", "here are some comments", self.nowString)
        self.assertEqual(size, 128)

    def test_8importTsharkThroughput(self):
        size = DataImportConfig().importTsharkThroughput("Alex", "Super summer Event", "here are some comments", self.nowString)
        self.assertEqual(size, 130)

    def test_9importTsharkProtocol(self):
        size = DataImportConfig().importTsharkProtocol("Alex", "Super summer Event", "here are some comments", self.nowString)
        self.assertEqual(size, 130)


if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_dataimport
