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
        DataImportConfig().importKeypressData(techName, eventName, comments, rightNow)

        click = PyClick().getClickCollection()
        click.delete_many({})
        DataImportConfig().importClick(techName, eventName, comments, rightNow, False, "")

        timed = PyTimed().getTimedCollection()
        timed.delete_many({})
        DataImportConfig().importTimed(techName, eventName, comments, rightNow, False, "")

        multiExcludeThroughput = MultiExcludeThroughput().getMultiExcludeThroughputCollection()
        multiExcludeThroughput.delete_many({})
        DataImportConfig().importMultiExcludeThroughput(techName, eventName, comments, rightNow)

        multiIncludeThroughput = MultiIncludeThroughput().getMultiIncludeThroughputCollection()
        multiIncludeThroughput.delete_many({})
        DataImportConfig().importMultiIncludeThroughput(techName, eventName, comments, rightNow)

        tsharkThroughput = TsharkThroughput().getTsharkThroughputCollection()
        tsharkThroughput.delete_many({})
        DataImportConfig().importTsharkThroughput(techName, eventName, comments, rightNow)

        multiExcludeProtocol = MultiExcludeProtocol().getMultiExcludeProtocolCollection()
        multiExcludeProtocol.delete_many({})
        DataImportConfig().importMultiExcludeProtocol(techName, eventName, comments, rightNow)

        multiIncludeProtocol = MultiIncludeProtocol().getMultiIncludeProtocolCollection()
        multiIncludeProtocol.delete_many({})
        DataImportConfig().importMultiIncludeProtocol(techName, eventName, comments, rightNow)

        tsharkProtocol = TsharkProtocol().getTsharkProtocolCollection()
        tsharkProtocol.delete_many({})
        DataImportConfig().importTsharkProtocol(techName, eventName, comments, rightNow)

        jsonData = TsharkThroughput().selectTsharkThroughputData(Common().formatDateStringToUTC('2016-10-15 11:57:19'), Common().formatDateStringToUTC('2016-10-15 11:57:19'))
        pprint(jsonData)

if __name__ == '__main__':
    unittest.main()

#python -m unittests.cleanupDatabases
