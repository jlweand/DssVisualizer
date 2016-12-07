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

from core.config.configDatasources import ConfigDatasources
from core.config.configRenderers import ConfigRenderers
from core.apis.datasource.manualScreenShot import ManualScreenShot
from core.apis.datasource.multiExcludeProtocol import MultiExcludeProtocol
from core.apis.datasource.multiIncludeProtocol import MultiIncludeProtocol
from core.apis.datasource.pyClick import PyClick
from core.apis.datasource.pyKeyPress import PyKeyPress
from core.apis.datasource.pyTimed import PyTimed
from core.apis.datasource.tsharkProtocol import TsharkProtocol


class Submission:

    def editAnnotation(self, queryDict):
        """Adds or Updates an annotation.

        :param queryDict: the request from the javascript
        :type queryDict: dict
        """
        itemType = queryDict['type'][0]
        annotation = queryDict['annotation'][0]
        eventName = queryDict['eventName'][0]
        techName = queryDict['techName'][0]
        start = queryDict['start'][0]
        if itemType == 'keypress':
            PyKeyPress().addAnnotationToKeyPressTimeline(start, annotation, techName, eventName)
        elif itemType == 'click':
            PyClick().addAnnotationToClickTimeline(start, annotation, techName, eventName)
        elif itemType == 'timed':
            PyTimed().addAnnotationToTimedTimeline(start, annotation, techName, eventName)
        elif itemType == 'multi_exclude':
            MultiExcludeProtocol().addAnnotationToMultiExcludeProtocolTimeline(start, annotation, techName, eventName)
        elif itemType == 'multi_include':
            MultiIncludeProtocol().addAnnotationToMultiIncludeProtocolTimeline(start, annotation, techName, eventName)
        elif itemType == 'tshark':
            TsharkProtocol().addAnnotationToTsharkProtocolTimeline(start, annotation, techName, eventName)
        elif itemType == 'screenshot':
            ManualScreenShot().addAnnotationToManualScreenShotTimeline(start, annotation, techName, eventName)

    def editData(self, queryDict):
        """Adds or edits the 'fixedData' attribute.

        :param queryDict: the request from the javascript
        :type queryDict: dict
        """
        itemID = queryDict['itemID'][0]
        itemType = queryDict['type'][0]
        editType = queryDict['editType'][0]  # delete for delete, edit for edit
        start = queryDict['start'][0]
        try:
            className = queryDict['className'][0]
        except KeyError:
            className = ''
        try:
            content = queryDict['content'][0]
        except KeyError:
            content = ''
        try:
            title = queryDict['title'][0]
        except KeyError:
            title = ''
        try:
            annotation = queryDict['annotation'][0]
        except KeyError:
            annotation = ''
        try:
            comment = queryDict['comment'][0]
        except KeyError:
            comment = ''
        try:
            dataType = queryDict['dataType'][0]
        except KeyError:
            dataType = ''

        if editType == 'delete':
            delete = True
        else:
            delete = ''

        if itemType == 'keypress':
            if annotation != '':
                PyKeyPress().modifyAnnotationKeyPress(itemID, annotation)
            PyKeyPress().modifyFixedKeyPressData(itemID, '', content, className, start, delete)

        elif itemType == 'click':
            if annotation != '':
                PyClick().modifyAnnotationClick(itemID, annotation)
            PyClick().modifyFixedClickData(itemID, '', content, className, start, title, dataType, delete)

        elif itemType == 'timed':
            if annotation != '':
                PyTimed().modifyAnnotationTimed(itemID, annotation)
            PyTimed().modifyFixedTimedData(itemID, '', content, className, start, title, dataType, delete)

        elif itemType == 'multi_exclude':
            if annotation != '':
                MultiExcludeProtocol().modifyAnnotationMultiExcludeProtocol(itemID, annotation)
            MultiExcludeProtocol().modifyFixedMultiExcludeProtocolData(itemID, '', content, className, title, start, delete)

        elif itemType == 'multi_include':
            if annotation != '':
                MultiIncludeProtocol().modifyAnnotationMultiIncludeProtocol(itemID, annotation)
            MultiIncludeProtocol().modifyFixedMultiIncludeProtocolData(itemID, '', content, className, title, start, delete)

        elif itemType == 'tshark':
            if annotation != '':
                TsharkProtocol().modifyAnnotationTsharkProtocol(itemID, annotation)
            TsharkProtocol().modifyFixedTsharkProtocolData(itemID, '', content, className, title, start, delete)

        elif itemType == 'screenshot':
            if annotation != '':
                ManualScreenShot().modifyAnnotationManualScreenShot(itemID, annotation)
            ManualScreenShot().modifyFixedManualScreenShotData(itemID, '', content, className, start, title, dataType, comment, delete)

    def updateConfiguration(self, queryDict):
        """Submits the changes to update the config.json

        :param queryDict: the request from the javascript
        :type queryDict: dict
        """
        database = queryDict['database'][0]
        pcap = queryDict['pcap'][0]
        pyKeyLogger = queryDict['pyKeyLogger'][0]
        screenshots = queryDict['screenshots'][0]
        ConfigDatasources().setDefaultDatasource(database)
        ConfigRenderers().setDefaultRenderer("pcap", pcap)
        ConfigRenderers().setDefaultRenderer("pyKeyLogger", pyKeyLogger)
        ConfigRenderers().setDefaultRenderer("screenshots", screenshots)
