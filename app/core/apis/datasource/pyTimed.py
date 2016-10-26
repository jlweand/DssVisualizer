from core.config.configReader import ConfigReader
#from plugins.datasource.mongodb.common import Common
from core.apis.datasource.common import Common

class PyTimed:
    """PyTimed API.  Most of these methods must be overwritten in your plugin.
    Datasource plugin must have a file named pyTimed.py with a class name of PyTimed
    """

    def getPlugin(self):
        """Internal method to get an instance of the active plugin"""
        return ConfigReader().getInstanceOfDatasourcePlugin("PyTimed")

    def selectTimedData(self, startDate, endDate, techName, eventName):
        """Override: Select the timed data by start and end date. The input here will be strings, datetimes will be passed to the plugin.

        :param startDate: The a string value of the local datetime to begin search on
        :type startDate: str
        :param endDate: The a string value of the local datetime to end search on
        :type endDate: str
        :returns: JSON object
        """
        pyTimed = self.getPlugin()
        jsonData = pyTimed.selectTimedData(Common().formatDateStringToUTC(startDate), Common().formatDateStringToUTC(endDate), techName, eventName)
        return jsonData

    def selectTimedDataById(self, dataId):
        """Override: Select the Timed data by its ID

        :param dataId: The ID of the Data point
        :type dataId: str
        :returns: JSON object
        """
        pyTimed = self.getPlugin()
        jsonData = pyTimed.selectTimedDataById(dataId)
        return jsonData

    def insertFixedTimedData(self,dataId, timed_id, content, className, startDate, title, typeTimed):
        """Override: Inserts a new record of the data. Does not overwrite the original key press.

        :param oldDataId: The key of the original timed data
        :type oldDataId: str
        :param content: The updated content
        :type content: str
        :param _type: The updated type
        :type _type: str
        :param classname: The updated class name
        :type classname: str
        :param title: The updated title
        :type title: str
        :param start: The string value of the updated datetime of the event, datetime UTC will be passed to the plugin.
        :type start: str
        :returns: newly created id.
        """
        pyTimed = self.getPlugin()
        result = pyTimed.insertFixedTimedData(dataId, timed_id, content, className, Common().formatDateStringToUTC(startDate), title, typeTimed)
        return result

    def updateFixedTimedData(self, dataId, timed_id, content, className, startDate, title, typeTimed):
        """Override: Updates the record of the 'fixed' timed data.

        :param dataId: The ID of the 'fixed' timed data to edit.
        :type dataId: str
        :param content: The updated content
        :type content: str
        :param _type: The updated type
        :type _type: str
        :param classname: The updated class name
        :type classname: str
        :param title: The updated title
        :type title: str
        :param start: The string value of the updated datetime of the event, datetime UTC will be passed to the plugin.
        :type start: str
        :returns: The modified count.
        """
        pyTimed = self.getPlugin()
        result = pyTimed.updateFixedTimedData(dataId, timed_id, content, className, Common().formatDateStringToUTC(startDate), title, typeTimed)
        return result

    def deleteFixedTimedData(self, dataId):
        """Override: Delete a 'fixed' timed data.

        :param dataId: The ID of the 'fixed' data to delete
        :type dataId: str
        :returns: The deleted count.
        """
        pyTimed = self.getPlugin()
        result = pyTimed.deleteFixedTimedData(dataId)
        return result

    def addAnnotationTimed(self, dataId, annotationText):
        """Override: Add an annotation to the Timed object.

        :param dataId: The ID of the data to add the annotation to.
        :type dataId: str
        :param annotationText: The annotation text
        :type annotationText: str
        :returns: The modified count.
        """
        pyTimed = self.getPlugin()
        return pyTimed.addAnnotationTimed(dataId, annotationText)

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
        pyTimed = self.getPlugin()
        return pyTimed.editAnnotationTimed(dataId, oldAnnotationText, newAnnotationText)

    #delete an annotation for the dataId
    def deleteAnnotationTimed(self, dataId, annotationText):
        """Override: Delete one annotation from the Timed object.

        :param dataId: The ID of the data to remove the annotation from.
        :type dataId: str
        :param annotationText: The annotation text to remove.
        :type annotationText: str
        :returns: The modified count.
        """
        pyTimed = self.getPlugin()
        return pyTimed.deleteAnnotationTimed(dataId, annotationText)

    # deletes all annotations for the dataId
    def deleteAllAnnotationsForTimed(self, dataId):
        """Override: Delete all annotations from the Timed object.

        :param dataId: The ID of the data to remove all annotations from.
        :type dataId: str
        :returns: The modified count.
        """
        pyTimed = self.getPlugin()
        return pyTimed.deleteAllAnnotationsForTimed(dataId)

    # add an annotation to the timeline, not a datapoint
    def addAnnotationToTimedTimeline(self, startTime, annotationText):
        """Override: Ands an annotation to the timeline (not a data point)

        :param startTime: The datetime string in local time to add the annotation to.  Will be converted to UTC before passing on to plugin
        :type startTime: str
        :param annotationText: The annotation text to add.
        :type annotationText: str
        :returns: The modified count.
         """

        pyTimed = self.getPlugin()
        return pyTimed.addAnnotationToTimedTimeline(Common().formatDateStringToUTC(startTime), annotationText)
