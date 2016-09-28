import unittest
from core.apis.datasource.pyKeyLogger import PyKeyLogger
from pymongo import MongoClient
import ujson
from pprint import pprint

class PyKeyLoggerTest(unittest.TestCase):

    def test_selectKeyPressData(self):
        jsonData = PyKeyLogger().selectKeyPressData()
        # pprint(jsonData)
        self.assertIsNotNone(jsonData)

    def test_selectClickData(self):
        jsonData = PyKeyLogger().selectClickData()
        # pprint(jsonData)
        self.assertIsNotNone(jsonData)

    def test_selectTimedData(self):
        jsonData = PyKeyLogger().selectTimedData()
        # pprint(jsonData)
        self.assertIsNotNone(jsonData)


if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_pyKeyLogger
