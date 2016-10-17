from core.config.configReader import ConfigReader
from core.apis.datasource.common import Common

class TsharkThroughput:
    """TsharkThroughput API.  Most of these methods must be overwritten in your plugin.
    Datasource plugin must have a file named tsharkThroughput.py with a class name of TsharkThroughput
    """


    def getPlugin(self):
        """Internal method to get an instance of the active plugin"""
        return ConfigReader().getInstanceOfDatasourcePlugin("TsharkThroughput")


    def selectTsharkThroughputData(self, startDate, endDate):
        """Override: Select the timed data by start and end date. The input here will be strings, datetimes will be passed to the plugin.

        :param startDate: The a string value of the local datetime to begin search on
        :type startDate: str
        :param endDate: The a string value of the local datetime to end search on
        :type endDate: str
        :returns: JSON object
        """
        tsharkPlugin = self.getPlugin()
        jsonData = tsharkPlugin.selectTsharkThroughputData(Common().formatDateStringToUTC(startDate), Common().formatDateStringToUTC(endDate))
        return jsonData


    def selectTsharkThroughputDataById(self, dataId):
        """Override: Select the TsharkThroughput data by its ID

        :param dataId: The ID of the Data point
        :type dataId: str
        :returns: JSON object
        """
        tsharkPlugin = self.getPlugin()
        jsonData = tsharkPlugin.selectTsharkThroughputDataById(dataId)
        return jsonData


    def insertFixedTsharkThroughputData(self, dataId, x, y):
        """Override: Inserts a fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :param x: The string value of the updated datetime of the event, datetime UTC will be passed to the plugin.
        :type x: str
        :param y: The number of protocols being used
        :type y: int
        :returns: The modified count.
        """
        tsharkPlugin = self.getPlugin()
        result = tsharkPlugin.insertFixedTsharkThroughputData(dataId, Common().formatDateStringToUTC(x), y)
        return result


    def updateFixedTsharkThroughputData(self, dataId, x, y):
        """Override: Updates the fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :param x: The string value of the updated datetime of the event, datetime UTC will be passed to the plugin.
        :type x: str
        :param y: The number of protocols being used
        :type y: int
        :returns: The modified count.
        """
        tsharkPlugin = self.getPlugin()
        result = tsharkPlugin.updateFixedTsharkThroughputData(dataId, Common().formatDateStringToUTC(x), y)
        return result


    def deleteFixedTsharkThroughputData(self, dataId):
        """Override: Deletes the fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :returns: The modified count.
        """
        tsharkPlugin = self.getPlugin()
        result = tsharkPlugin.deleteFixedTsharkThroughputData(dataId)
        return result


    def addAnnotationTsharkThroughput(self, dataId, annotationText):
        """Override: Add an annotation to the TsharkThroughput object.

        :param dataId: The ID of the data to add the annotation to.
        :type dataId: str
        :param annotationText: The annotation text
        :type annotationText: str
        :returns: The modified count.
        """
        tsharkPlugin = self.getPlugin()
        return tsharkPlugin.addAnnotationTsharkThroughput(dataId, annotationText)


    # edit an annotation for the dataId
    def editAnnotationTsharkThroughput(self, dataId, oldAnnotationText, newAnnotationText):
        """Override: Edit an annotation on the TsharkThroughput object.

        :param dataId: The ID of the data to edit the annotation of.
        :type dataId: str
        :param oldAnnotationText: The old annotation text
        :type oldAnnotationText: str
        :param newAnnotationText: The new annotation text
        :type newAnnotationText: str
        :returns: The modified count.
        """
        tsharkPlugin = self.getPlugin()
        return tsharkPlugin.editAnnotationTsharkThroughput(dataId, oldAnnotationText, newAnnotationText)


    # delete an annotation for the dataId
    def deleteAnnotationTsharkThroughput(self, dataId, annotationText):
        """Override: Delete one annotation from the TsharkThroughput object.

        :param dataId: The ID of the data to remove the annotation from.
        :type dataId: str
        :param annotationText: The annotation text to remove.
        :type annotationText: str
        :returns: The modified count.
        """
        tsharkPlugin = self.getPlugin()
        return tsharkPlugin.deleteAnnotationTsharkThroughput(dataId, annotationText)


    # deletes all annotations for the dataId
    def deleteAllAnnotationsForTsharkThroughput(self, dataId):
        """Override: Delete all annotations from the TsharkThroughput object.

        :param dataId: The ID of the data to remove all annotations from.
        :type dataId: str
        :returns: The modified count.
        """
        tsharkPlugin = self.getPlugin()
        return tsharkPlugin.deleteAllAnnotationsForTsharkThroughput(dataId)


    # add an annotation to the timeline, not a datapoint
    def addAnnotationToTsharkThroughputTimeline(self, x, annotationText):
        """Override: Ands an annotation to the timeline (not a data point)

        :param x: The datetime string in local time to add the annotation to.  Will be converted to UTC before passing on to plugin
        :type x: str
        :param annotationText: The annotation text to add.
        :type annotationText: str
        :returns: The modified count.
         """

        tsharkPlugin = self.getPlugin()
        return tsharkPlugin.addAnnotationToTsharkThroughputTimeline(Common().formatDateStringToUTC(x), annotationText)
