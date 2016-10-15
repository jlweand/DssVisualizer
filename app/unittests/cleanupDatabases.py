import unittest
from datetime import datetime, timezone
from pprint import pprint
from plugins.datasource.mongodb.pyKeyLogger import PyKeyLogger
from plugins.datasource.mongodb.multiExcludeThroughput import MultiExcludeThroughput
from plugins.datasource.mongodb.multiIncludeThroughput import MultiIncludeThroughput
from plugins.datasource.mongodb.tsharkThroughput import TsharkThroughput
from core.config.dataImportConfig import DataImportConfig

class CleanupDatabases(unittest.TestCase):

    def test_cleanEverythingUp(self):
        rightNow = "2016-10-10 10:10:10"

        keypress = PyKeyLogger().getKeyPressCollection()
        keypress.delete_many({})
        DataImportConfig().importKeypressData("Alex", "Super summer Event", "here are some comments", rightNow)

        click = PyKeyLogger().getClickCollection()
        click.delete_many({})
        DataImportConfig().importClick("Alex", "Super summer Event", "here are some comments", rightNow)

        timed = PyKeyLogger().getTimedCollection()
        timed.delete_many({})
        DataImportConfig().importTimed("Alex", "Super summer Event", "here are some comments", rightNow)

        multiExcludeThroughput = MultiExcludeThroughput().getMultiExcludeThroughputCollection()
        multiExcludeThroughput.delete_many({})
        DataImportConfig().importMultiExcludeThroughput("Alex", "Super summer Event", "here are some comments", rightNow)

        multiIncludeThroughput = MultiIncludeThroughput().getMultiIncludeThroughputCollection()
        multiIncludeThroughput.delete_many({})
        DataImportConfig().importMultiIncludeThroughput("Alex", "Super summer Event", "here are some comments", rightNow)

        tsharkThroughput = TsharkThroughput().getTsharkThroughputCollection()
        tsharkThroughput.delete_many({})
        DataImportConfig().importTsharkThroughput("Alex", "Super summer Event", "here are some comments", rightNow)

        jsonData = PyKeyLogger().selectClickData('2014-08-01 00:00:00', '2018-08-02 00:00:00')
        pprint(jsonData)

if __name__ == '__main__':
    unittest.main()

#python -m unittests.cleanupDatabases
