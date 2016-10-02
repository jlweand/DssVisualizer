import unittest
from core.apis.datasource.pyKeyLogger import PyKeyLogger
import ujson
import pprint

class PyKeyLoggerTest(unittest.TestCase):

    def test_selectKeyPressData(self):
        jsonData = PyKeyLogger().selectKeyPressData('2016-08-01 00:00:00', '2016-08-20 00:00:00')
        self.assertEqual(9, len(jsonData))

    def test_selectKeyPressDataById(self):
        jsonData = PyKeyLogger().selectKeyPressDataById('57f02238578ad872fdeabd58')
        self.assertEqual(1, len(jsonData))

    # def test_selectClickData(self):
    #     jsonData = PyKeyLogger().selectClickData()
    #     # pprint(jsonData)
    #     self.assertIsNotNone(jsonData)
    #
    # def test_selectTimedData(self):
    #     jsonData = PyKeyLogger().selectTimedData()
    #     # pprint(jsonData)
    #     self.assertIsNotNone(jsonData)

if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_pyKeyLogger
