import unittest
from core.config.dataimport import DataImport

class DataImportTest(unittest.TestCase):

    def test_insertKeypressData(self):
        size = DataImport().importKeypressData("name", "computer")
        self.assertEqual(size, 24)

    def test_importClick(self):
        _id = DataImport().importClick("name", "computer")
        self.assertIsNotNone(_id)

    def test_importTimed(self):
        _id = DataImport().importTimed("name", "computer")
        self.assertIsNotNone(_id)

if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_dataimport
