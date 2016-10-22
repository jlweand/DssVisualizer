import unittest
from datetime import datetime
from core.config.dataImportConfig import DataImportConfig

class DataImportTest(unittest.TestCase):
    now = datetime.now()
    nowString = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
    techName = "Alex"
    eventName = "Super Summer Event"
    comments = "here are some comments"

    def test_1insertKeypressData(self):
        size = DataImportConfig().importKeypressData(self.techName, self.eventName, self.comments, self.nowString)
        self.assertEqual(size, 71)

    def test_2importClick(self):
        size = DataImportConfig().importClick(self.techName, self.eventName, self.comments, self.nowString, True, "abcd")
        self.assertEqual(size, 29)

    def test_3importTimed(self):
        size = DataImportConfig().importTimed(self.techName, self.eventName, self.comments, self.nowString, True, "abcd")
        self.assertEqual(size, 34)

    def test_4importMultiExcludeThroughput(self):
        size = DataImportConfig().importMultiExcludeThroughput(self.techName, self.eventName, self.comments, self.nowString)
        self.assertEqual(size, 222)

    def test_5importMultiExcludeProtocol(self):
        size = DataImportConfig().importMultiExcludeProtocol(self.techName, self.eventName, self.comments, self.nowString)
        self.assertEqual(size, 222)

    def test_6importMultiIncludeThroughput(self):
        size = DataImportConfig().importMultiIncludeThroughput(self.techName, self.eventName, self.comments, self.nowString)
        self.assertEqual(size, 221)

    def test_7importMultiIncludeProtocol(self):
        size = DataImportConfig().importMultiIncludeProtocol(self.techName, self.eventName, self.comments, self.nowString)
        self.assertEqual(size, 221)

    def test_8importTsharkThroughput(self):
        size = DataImportConfig().importTsharkThroughput(self.techName, self.eventName, self.comments, self.nowString)
        self.assertEqual(size, 371)

    def test_9importTsharkProtocol(self):
        size = DataImportConfig().importTsharkProtocol(self.techName, self.eventName, self.comments, self.nowString)
        self.assertEqual(size, 371)


if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_dataimport
