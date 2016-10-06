import unittest
import datetime
from pprint import pprint
from plugins.datasource.mongodb.pyKeyLogger import PyKeyLogger
from core.config.dataImportConfig import DataImportConfig

class CleanupDatabase(unittest.TestCase):

    def test_cleanEverythingUp(self):
        keypress = PyKeyLogger().getKeyPressCollection()
        keypress.delete_many({})
        DataImportConfig().importKeypressData("Alex", "Super summer Event", "here are some comments", datetime.datetime.now())

        click = PyKeyLogger().getClickCollection()
        DataImportConfig().importClick("Alex", "Super summer Event", "here are some comments", datetime.datetime.now())
        click.delete_many({})

        timed = PyKeyLogger().getTimedCollection()
        timed.delete_many({})
        DataImportConfig().importTimed("Alex", "Super summer Event", "here are some comments", datetime.datetime.now())

        jsonData = PyKeyLogger().selectKeyPressData('2016-09-01 00:00:00', '2016-09-20 00:00:00')
        pprint(jsonData)

if __name__ == '__main__':
    unittest.main()

#python -m unittests.cleanupDatabase
