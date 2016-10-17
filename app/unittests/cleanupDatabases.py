import unittest
from pprint import pprint
from plugins.datasource.mongodb.pyKeyLogger import PyKeyLogger
from plugins.datasource.mongodb.multiExcludeThroughput import MultiExcludeThroughput
from plugins.datasource.mongodb.multiIncludeThroughput import MultiIncludeThroughput
from plugins.datasource.mongodb.tsharkThroughput import TsharkThroughput
from plugins.datasource.mongodb.multiExcludeProtocol import MultiExcludeProtocol
from plugins.datasource.mongodb.multiIncludeProtocol import MultiIncludeProtocol
from plugins.datasource.mongodb.tsharkProtocol import TsharkProtocol
from core.config.dataImportConfig import DataImportConfig
from core.apis.datasource.common import Common

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

        multiExcludeProtocol = MultiExcludeProtocol().getMultiExcludeProtocolCollection()
        multiExcludeProtocol.delete_many({})
        DataImportConfig().importMultiExcludeProtocol("Alex", "Super summer Event", "here are some comments", rightNow)

        multiIncludeProtocol = MultiIncludeProtocol().getMultiIncludeProtocolCollection()
        multiIncludeProtocol.delete_many({})
        DataImportConfig().importMultiIncludeProtocol("Alex", "Super summer Event", "here are some comments", rightNow)

        tsharkProtocol = TsharkProtocol().getTsharkProtocolCollection()
        tsharkProtocol.delete_many({})
        DataImportConfig().importTsharkProtocol("Alex", "Super summer Event", "here are some comments", rightNow)

        jsonData = TsharkThroughput().selectTsharkThroughputData(Common().formatDateStringToUTC('2016-10-15 11:57:19'), Common().formatDateStringToUTC('2016-10-15 11:57:19'))
        pprint(jsonData)

if __name__ == '__main__':
    unittest.main()

#python -m unittests.cleanupDatabases
