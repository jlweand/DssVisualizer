import unittest
from pprint import pprint
from plugins.datasource.mongodb.pyClick import PyClick
from plugins.datasource.mongodb.pyKeyPress import PyKeyPress
from plugins.datasource.mongodb.pyTimed import PyTimed
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
        techName = "Alex"
        eventName = "Super Summer Event"
        comments = "here are some comments"

        keypress = PyKeyPress().getKeyPressCollection()
        keypress.delete_many({})

        click = PyClick().getClickCollection()
        click.delete_many({})

        timed = PyTimed().getTimedCollection()
        timed.delete_many({})

        multiExcludeThroughput = MultiExcludeThroughput().getMultiExcludeThroughputCollection()
        multiExcludeThroughput.delete_many({})

        multiIncludeThroughput = MultiIncludeThroughput().getMultiIncludeThroughputCollection()
        multiIncludeThroughput.delete_many({})

        tsharkThroughput = TsharkThroughput().getTsharkThroughputCollection()
        tsharkThroughput.delete_many({})

        multiExcludeProtocol = MultiExcludeProtocol().getMultiExcludeProtocolCollection()
        multiExcludeProtocol.delete_many({})

        multiIncludeProtocol = MultiIncludeProtocol().getMultiIncludeProtocolCollection()
        multiIncludeProtocol.delete_many({})

        tsharkProtocol = TsharkProtocol().getTsharkProtocolCollection()
        tsharkProtocol.delete_many({})

        DataImportConfig().importAllDataFromFiles("json", techName, eventName, comments, rightNow)

        jsonData = TsharkThroughput().selectTsharkThroughputData(Common().formatDateStringToUTC('2016-10-15 11:57:19'),
                                                                 Common().formatDateStringToUTC('2016-10-15 11:57:19'))
        pprint(jsonData)

if __name__ == '__main__':
    unittest.main()

#python -m unittests.cleanupDatabases
