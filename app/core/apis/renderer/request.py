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

from core.apis.datasource.manualScreenShot import ManualScreenShot
from core.apis.datasource.multiExcludeProtocol import MultiExcludeProtocol
from core.apis.datasource.multiExcludeThroughput import MultiExcludeThroughput
from core.apis.datasource.multiIncludeProtocol import MultiIncludeProtocol
from core.apis.datasource.multiIncludeThroughput import MultiIncludeThroughput
from core.apis.datasource.pyClick import PyClick
from core.apis.datasource.pyKeyPress import PyKeyPress
from core.apis.datasource.pyTimed import PyTimed
from core.apis.datasource.tsharkProtocol import TsharkProtocol
from core.apis.datasource.tsharkThroughput import TsharkThroughput
from core.apis.datasource.snoopy import Snoopy

class Request:

    def getData(self, queryDict):
        """Selects the data from the data source and generates the javascript to be executed by the webkit.

        :param queryDict: the request from the javascript
        :type queryDict: dict
        :return: javascript to be executed
        """
        startDate = queryDict['startDate'][0]
        endDate = queryDict['endDate'][0]
        try:
            techNames = queryDict['techNames']
            techList = techNames[0].split(",")
        except KeyError:
            techList = []
        try:
            eventNames = queryDict['eventNames']
            eventList = eventNames[0].split(",")
        except KeyError:
            eventList = []
        try:
            eventTechNames = queryDict['eventTechNames']
            eventTechList = eventTechNames[0].split(",")
        except KeyError:
            eventTechList = []

        if queryDict['request'][0] == 'keypressData':
            keyData = PyKeyPress().selectKeyPressData(startDate, endDate, techList, eventList, eventTechList)
            clickData = PyClick().selectClickData(startDate, endDate, techList, eventList, eventTechList)
            timedData = PyTimed().selectTimedData(startDate, endDate, techList, eventList, eventTechList)

            js = "visualizeKeyData(%s, %s, %s);" % (keyData, clickData, timedData)
            return js
        
        elif queryDict['request'][0] == 'snoopyData':
            snoopyData = Snoopy().selectSnoopyData(startDate, endDate, techList, eventList, eventTechList)
            
            js = "visualizeSnoopyData(%s);" % (snoopyData)
            return js

        elif queryDict['request'][0] == 'pcapData':
            multiEx = MultiExcludeThroughput().selectMultiExcludeThroughputData(startDate, endDate, techList, eventList, eventTechList)
            multiExProt = MultiExcludeProtocol().selectMultiExcludeProtocolData(startDate, endDate, techList, eventList, eventTechList)

            multiInc = MultiIncludeThroughput().selectMultiIncludeThroughputData(startDate, endDate, techList, eventList, eventTechList)
            multiIncProt = MultiIncludeProtocol().selectMultiIncludeProtocolData(startDate, endDate, techList, eventList, eventTechList)

            tshark = TsharkThroughput().selectTsharkThroughputData(startDate, endDate, techList, eventList, eventTechList)
            tsharkProt = TsharkProtocol().selectTsharkProtocolData(startDate, endDate, techList, eventList, eventTechList)

            js = "visualizePCAPData(%s, %s, %s, %s, %s, %s);" % (multiEx, multiExProt, multiInc, multiIncProt, tshark, tsharkProt)
            return js

        elif queryDict['request'][0] == 'screenshotData':
            snap = ManualScreenShot().selectManualScreenShotData(startDate, endDate, techList, eventList, eventTechList)
            js = "visualizeSnapshotData(%s);" % (snap)
            return js
