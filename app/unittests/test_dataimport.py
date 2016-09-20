import unittest
import datetime
from core.config.dataimport import DataImport

class DataImportTest(unittest.TestCase):

    def test_insertKeypressData(self):
        size = DataImport().importKeypressData("Alex", "Super summer Event", "here are some comments", datetime.datetime.now())
        self.assertEqual(size, 24)

    def test_importClick(self):
        size = DataImport().importClick("Alex", "Super summer Event", "here are some comments", datetime.datetime.now())
        self.assertEqual(size, 8)

    def test_importTimed(self):
        size = DataImport().importTimed("Alex", "Super summer Event", "here are some comments", datetime.datetime.now())
        self.assertEqual(size, 21)

if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_dataimport
