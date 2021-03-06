#  Copyright (C) 2016  Jamie Acosta, Jennifer Weand, Juan Soto, Mark Eby, Mark Smith, Andres Olivas
#
# This file is part of DssVisualizer.
#
# DssVisualizer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DssVisualizer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DssVisualizer.  If not, see <http://www.gnu.org/licenses/>.

import unittest
from datetime import datetime
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
from plugins.datasource.mongodb.manualScreenShot import ManualScreenShot
from core.config.dataImport import DataImport
from core.apis.datasource.common import Common

class SetupMongoDatasource(unittest.TestCase):

    def test_cleanEverythingUp(self):
        now = datetime.now()
        rightNow = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
        # techName = "Alex"
        # eventName = "Super Summer Event"
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

        manualScreenShot = ManualScreenShot().getManualScreenShotCollection()
        manualScreenShot.delete_many({})

        DataImport().importAllDataFromFiles("json/unittestDatasets/superSummerAlex", "Alex", "Super Summer Event", comments, rightNow, False)
        DataImport().importAllDataFromFiles("json/unittestDatasets/superSummerTom", "Tom", "Super Summer Event", comments, rightNow, False)
        DataImport().importAllDataFromFiles("json/unittestDatasets/anotherJulie", "Julie", "Another Event", comments, rightNow, False)
        DataImport().importAllDataFromFiles("json/unittestDatasets/anotherAlex", "Alex", "Another Event", comments, rightNow, False)
        DataImport().importAllDataFromFiles("json/unittestDatasets/unicornWillow", "Willow", "Unicorns and more!", comments, rightNow, False)

        # DataImport().importAllDataFromFiles("json/1very small", "Very Small", "z1Very Small", "Very Small", rightNow, False)
        # DataImport().importAllDataFromFiles("json/2small", "Small", "z2Small", "Small", rightNow, False)
        # DataImport().importAllDataFromFiles("json/3medium", "Medium", "z3Medium", "Medium", rightNow, False)
        # DataImport().importAllDataFromFiles("json/4large", "Large", "z4Large", "Large", rightNow, False)

        jsonData = PyKeyPress().selectKeyPressData(Common().formatDateStringToUTC('2016-10-18 18:26:36'),
                                                   Common().formatDateStringToUTC('2016-10-18 18:26:36'),
                                                   ['Willow'], ['Unicorns and more!'], [])
        pprint(jsonData)
        self.assertIsNotNone(jsonData)

if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_setupMongoDatasource
