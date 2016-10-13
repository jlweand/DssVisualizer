from core.config.configReader import ConfigReader

class PyKeyLogger:
    """PyKeyLogger API.  Most of these methods must be overwritten in your plugin.
    Datasource plugin must have a filenamed pyKeyLogger.py with a class name of PyKeyLogger
    """

    def getPlugin(self):
        """Internal method to get an instance of the active plugin"""
        return ConfigReader().getInstanceOfDatasourcePlugin("PyKeyLogger")

#Keypress#
    def selectKeyPressData(self, startDate, endDate):
        """Override: Select the key press data by start and end date.

        :param startDate: The datetime to return data
        :type startDate: datetime
        :param endDate: The datatime to return data
        :type endDate: datetime
        :returns: JSON object
        """
        pyKeyLogger = self.getPlugin()
        jsonData = pyKeyLogger.selectKeyPressData(startDate, endDate)
        return jsonData

    def selectKeyPressDataById(self, dataId):
        """Override: Select the key press data by its ID

        :param dataId: The ID of the Data point
        :type dataId: str
        :returns: JSON object
        """
        pyKeyLogger = self.getPlugin()
        jsonData = pyKeyLogger.selectKeyPressDataById(dataId)
        return jsonData

    def insertFixedKeyPressData(self, oldDataId, content, className, start):
        """Override: Inserts a new record of the data. Does not overrite the original key press.

        :param oldDataId: The key of the original key press data
        :type oldDataId: str
        :param content: The updated content
        :type content: str
        :param className: The updtaed class name
        :type className: str
        :param start: The updated datetime of the event.
        :type start: datetime
        :returns: newly created id.
        """
        pyKeyLogger = self.getPlugin()
        result = pyKeyLogger.insertFixedKeyPressData(oldDataId, content, className, start)
        return result

    def updateFixedKeyPressData(self, dataId, content, className, start):
        """Override: Updates the record of the 'fixed' key press data.

        :param dataId: The ID of the 'fixed' key press data to edit.
        :type dataId: str
        :param content: The updated content
        :type content: str
        :param className: The updtaed class name
        :type className: str
        :param start: The updated datetime of the event.
        :type start: datetime
        :returns: The modified count.
        """
        pyKeyLogger = self.getPlugin()
        result = pyKeyLogger.updateFixedKeyPressData(dataId, content, className, start)
        return result

    def deleteFixedKeyPressData(self, dataId):
        """Override: Delete a 'fixed' key press data.

        :param dataId: The ID of the 'fixed' data to delete
        :type dataId: str
        :returns: The deleted count.
        """
        pyKeyLogger = self.getPlugin()
        return pyKeyLogger.deleteFixedKeyPressData(dataId)

    def addAnnotationKeyPress(self, dataId, annotationText):
        """Override: Add an annotation to the key press object.

        :param dataId: The ID of the data to add the annotation to.
        :type dataId: str
        :param annotationText: The annotation text
        :type annotationText: str
        :returns: The modified count.
        """
        pyKeyLogger = self.getPlugin()
        return pyKeyLogger.addAnnotationKeyPress(dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationKeyPress(self, dataId, oldAnnotationText, newAnnotationText):
        """Override: Edit an annotation on the key press object.

        :param dataId: The ID of the data to edit the annotation of.
        :type dataId: str
        :param oldAnnotationText: The old annotation text
        :type oldAnnotationText: str
        :param newAnnotationText: The new annotation text
        :type newAnnotationText: str
        :returns: The modified count.
        """
        pyKeyLogger = self.getPlugin()
        return pyKeyLogger.editAnnotationKeyPress(dataId, oldAnnotationText, newAnnotationText)

    #delete an annotation for the dataId
    def deleteAnnotationKeyPress(self, dataId, annotationText):
        """Override: Delete one annotation from the key press object.

        :param dataId: The ID of the data to remove the annotation from.
        :type dataId: str
        :param annotationText: The annotation text to remove.
        :type annotationText: str
        :returns: The modified count.
        """
        pyKeyLogger = self.getPlugin()
        return pyKeyLogger.deleteAnnotationKeyPress(dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForKeyPress(self, dataId):
        """Override: Delete all annotations from the key press object.

        :param dataId: The ID of the data to remove all annotations from.
        :type dataId: str
        :returns: The modified count.
        """
        pyKeyLogger = self.getPlugin()
        return pyKeyLogger.deleteAllAnnotationsForKeyPress(dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToKeyPressTimeline(self, startTime, annotationText):
        """Override: Ands an annotation to the timeline (not a data point)

        :param startTime: The datetime to add the annotation to
        :type startTime: datetime
        :param annotationText: The annotation text to add.
        :type annotationText: str
        :returns: The modified count.
         """

        pyKeyLogger = self.getPlugin()
        return pyKeyLogger.addAnnotationToKeyPressTimeline(startTime, annotationText)

#Click#
    def selectClickData(self, startDate, endDate):
        """Override: Select the click data by start and end date.

        :param startDate: The datetime to return data
        :type startDate: datetime
        :param endDate: The datatime to return data
        :type endDate: datetime
        :returns: JSON object
        """
        pyKeyLogger = self.getPlugin()
        jsonData = pyKeyLogger.selectClickData(startDate, endDate)
        return jsonData

    def selectClickDataById(self, dataId):
        """Override: Select the Click data by its ID

        :param dataId: The ID of the Data point
        :type dataId: str
        :returns: JSON object
        """
        pyKeyLogger = self.getPlugin()
        jsonData = pyKeyLogger.selectClickDataById(dataId)
        return jsonData

    def insertFixedClickData(self, oldDataId, content, _type, classname, title, start, end):
        """Override: Inserts a new record of the data. Does not overrite the original key press.

        :param oldDataId: The key of the original click data
        :type oldDataId: str
        :param content: The updated content
        :type content: str
        :param _type: The updtaed type
        :type _type: str
        :param className: The updtaed class name
        :type className: str
        :param title: The updtaed title
        :type title: str
        :param start: The updated start datetime of the event.
        :type start: datetime
        :param end: The updated end datetime of the event.
        :type end: datetime
        :returns: newly created id.
        """
        pyKeyLogger = self.getPlugin()
        result = pyKeyLogger.insertFixedClickData(oldDataId, content, _type, classname, title, start, end)
        return result

    def updateFixedClickData(self, dataId, content, _type, classname, title, start, end):
        """Override: Updates the record of the 'fixed' click data.

        :param dataId: The ID of the 'fixed' click data to edit.
        :type dataId: str
        :param content: The updated content
        :type content: str
        :param _type: The updtaed type
        :type _type: str
        :param className: The updtaed class name
        :type className: str
        :param title: The updtaed title
        :type title: str
        :param start: The updated start datetime of the event.
        :type start: datetime
        :param end: The updated end datetime of the event.
        :type end: datetime
        :returns: The modified count.
        """
        pyKeyLogger = self.getPlugin()
        result = pyKeyLogger.updateFixedClickData(dataId, content, _type, classname, title, start, end)
        return result

    def deleteFixedClickData(self, dataId):
        """Override: Delete a 'fixed' click data.

        :param dataId: The ID of the 'fixed' data to delete
        :type dataId: str
        :returns: The deleted count.
        """
        pyKeyLogger = self.getPlugin()
        result = pyKeyLogger.deleteFixedClickData(dataId)
        return result

    def addAnnotationClick(self, dataId, annotationText):
        """Override: Add an annotation to the Click object.

        :param dataId: The ID of the data to add the annotation to.
        :type dataId: str
        :param annotationText: The annotation text
        :type annotationText: str
        :returns: The modified count.
        """
        pyKeyLogger = self.getPlugin()
        return pyKeyLogger.addAnnotationClick(dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationClick(self, dataId, oldAnnotationText, newAnnotationText):
        """Override: Edit an annotation on the Click object.

        :param dataId: The ID of the data to edit the annotation of.
        :type dataId: str
        :param oldAnnotationText: The old annotation text
        :type oldAnnotationText: str
        :param newAnnotationText: The new annotation text
        :type newAnnotationText: str
        :returns: The modified count.
        """
        pyKeyLogger = self.getPlugin()
        return pyKeyLogger.editAnnotationClick(dataId, oldAnnotationText, newAnnotationText)

    #delete an annotation for the dataId
    def deleteAnnotationClick(self, dataId, annotationText):
        """Override: Delete one annotation from the Click object.

        :param dataId: The ID of the data to remove the annotation from.
        :type dataId: str
        :param annotationText: The annotation text to remove.
        :type annotationText: str
        :returns: The modified count.
        """
        pyKeyLogger = self.getPlugin()
        return pyKeyLogger.deleteAnnotationClick(dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForClick(self, dataId):
        """Override: Delete all annotations from the Click object.

        :param dataId: The ID of the data to remove all annotations from.
        :type dataId: str
        :returns: The modified count.
        """
        pyKeyLogger = self.getPlugin()
        return pyKeyLogger.deleteAllAnnotationsForClick(dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToClickTimeline(self, startTime, annotationText):
        """Override: Ands an annotation to the timeline (not a data point)

        :param startTime: The datetime to add the annotation to
        :type startTime: datetime
        :param annotationText: The annotation text to add.
        :type annotationText: str
        :returns: The modified count.
         """

        pyKeyLogger = self.getPlugin()
        return pyKeyLogger.addAnnotationToClickTimeline(startTime, annotationText)

#Timed#
    def selectTimedData(self, startDate, endDate):
        """Override: Select the timed data by start and end date.

        :param startDate: The datetime to return data
        :type startDate: datetime
        :param endDate: The datatime to return data
        :type endDate: datetime
        :returns: JSON object
        """
        pyKeyLogger = self.getPlugin()
        jsonData = pyKeyLogger.selectTimedData(startDate, endDate)
        return jsonData

    def selectTimedDataById(self, dataId):
        """Override: Select the Timed data by its ID

        :param dataId: The ID of the Data point
        :type dataId: str
        :returns: JSON object
        """
        pyKeyLogger = self.getPlugin()
        jsonData = pyKeyLogger.selectTimedDataById(dataId)
        return jsonData

    def insertFixedTimedData(self, oldDataId, content, _type, classname, title, start, end):
        """Override: Inserts a new record of the data. Does not overrite the original key press.

        :param oldDataId: The key of the original timmed data
        :type oldDataId: str
        :param content: The updated content
        :type content: str
        :param _type: The updtaed type
        :type _type: str
        :param classname: The updtaed class name
        :type classname: str
        :param title: The updtaed title
        :type title: str
        :param start: The updated start datetime of the event.
        :type start: datetime
        :param end: The updated end datetime of the event.
        :type end: datetime
        :returns: newly created id.
        """
        pyKeyLogger = self.getPlugin()
        result = pyKeyLogger.insertFixedTimedData(oldDataId, content, _type, classname, title, start, end)
        return result

    def updateFixedTimedData(self, dataId, content, _type, classname, title, start, end):
        """Override: Updates the record of the 'fixed' timed data.

        :param dataId: The ID of the 'fixed' timed data to edit.
        :type dataId: str
        :param content: The updated content
        :type content: str
        :param _type: The updtaed type
        :type _type: str
        :param classname: The updtaed class name
        :type classname: str
        :param title: The updtaed title
        :type title: str
        :param start: The updated start datetime of the event.
        :type start: datetime
        :param end: The updated end datetime of the event.
        :type end: datetime
        :returns: The modified count.
        """
        pyKeyLogger = self.getPlugin()
        result = pyKeyLogger.updateFixedTimedData(dataId, content, _type, classname, title, start, end)
        return result

    def deleteFixedTimedData(self, dataId):
        """Override: Delete a 'fixed' timed data.

        :param dataId: The ID of the 'fixed' data to delete
        :type dataId: str
        :returns: The deleted count.
        """
        pyKeyLogger = self.getPlugin()
        result = pyKeyLogger.deleteFixedTimedData(dataId)
        return result

    def addAnnotationTimed(self, dataId, annotationText):
        """Override: Add an annotation to the Timed object.

        :param dataId: The ID of the data to add the annotation to.
        :type dataId: str
        :param annotationText: The annotation text
        :type annotationText: str
        :returns: The modified count.
        """
        pyKeyLogger = self.getPlugin()
        return pyKeyLogger.addAnnotationTimed(dataId, annotationText)

    # edit an annotation for the dataId
    def editAnnotationTimed(self, dataId, oldAnnotationText, newAnnotationText):
        """Override: Edit an annotation on the Timed object.

        :param dataId: The ID of the data to edit the annotation of.
        :type dataId: str
        :param oldAnnotationText: The old annotation text
        :type oldAnnotationText: str
        :param newAnnotationText: The new annotation text
        :type newAnnotationText: str
        :returns: The modified count.
        """
        pyKeyLogger = self.getPlugin()
        return pyKeyLogger.editAnnotationTimed(dataId, oldAnnotationText, newAnnotationText)

    #delete an annotation for the dataId
    def deleteAnnotationTimed(self, dataId, annotationText):
        """Override: Delete one annotation from the Timed object.

        :param dataId: The ID of the data to remove the annotation from.
        :type dataId: str
        :param annotationText: The annotation text to remove.
        :type annotationText: str
        :returns: The modified count.
        """
        pyKeyLogger = self.getPlugin()
        return pyKeyLogger.deleteAnnotationTimed(dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForTimed(self, dataId):
        """Override: Delete all annotations from the Timed object.

        :param dataId: The ID of the data to remove all annotations from.
        :type dataId: str
        :returns: The modified count.
        """
        pyKeyLogger = self.getPlugin()
        return pyKeyLogger.deleteAllAnnotationsForTimed(dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToTimedTimeline(self, startTime, annotationText):
        """Override: Ands an annotation to the timeline (not a data point)

        :param startTime: The datetime to add the annotation to
        :type startTime: datetime
        :param annotationText: The annotation text to add.
        :type annotationText: str
        :returns: The modified count.
         """

        pyKeyLogger = self.getPlugin()
        return pyKeyLogger.addAnnotationToTimedTimeline(startTime, annotationText)
