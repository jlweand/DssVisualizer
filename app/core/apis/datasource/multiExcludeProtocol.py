from core.config.configReader import ConfigReader
#from plugins.datasource.mongodb.common import Common
from core.apis.datasource.common import Common

class MultiExcludeProtocol:
    """MultiExcludeProtocol API.  Most of these methods must be overwritten in your plugin.
    Datasource plugin must have a file named multiExcludeProtocol.py with a class name of MultiExcludeProtocol
    """


    def getPlugin(self):
        """Internal method to get an instance of the active plugin"""
        return ConfigReader().getInstanceOfDatasourcePlugin("MultiExcludeProtocol")


    def selectMultiExcludeProtocolData(self, startDate, endDate):
        """Override: Select the data by start and end date.

        :param startDate: The datetime to return data
        :type startDate: datetime
        :param endDate: The datatime to return data
        :type endDate: datetime
        :returns: JSON object
        """
        multiExcludePlugin = self.getPlugin()
        jsonData = multiExcludePlugin.selectMultiExcludeProtocolData(Common().formatDateStringToUTC(startDate), Common().formatDateStringToUTC(endDate))
        return jsonData


    def selectMultiExcludeProtocolDataById(self, dataId):
        """Override: Select the MultiExcludeProtocol data by its ID

        :param dataId: The ID of the Data point
        :type dataId: str
        :returns: JSON object
        """
        multiExcludePlugin = self.getPlugin()
        jsonData = multiExcludePlugin.selectMultiExcludeProtocolDataById(dataId)
        return jsonData


    def insertFixedMultiExcludeProtocolData(self, dataId, oldDataId, content, className, title, start):
        """Override: Inserts a fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :param x: x is the Datetime
        :type x: datetime
        :param y: The number of protocols being used
        :type y: str
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        result = multiExcludePlugin.insertFixedMultiExcludeProtocolData(dataId, oldDataId, content, className, title, Common().formatDateStringToUTC(startDate))
        return result


    def updateFixedMultiExcludeProtocolData(self, dataId, oldDataId, content, className, title, start):
        """Override: Updates the fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :param x: x is the Datetime
        :type x: datetime
        :param y: The number of protocols being used
        :type y: str
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        result = multiExcludePlugin.updateFixedMultiExcludeProtocolData(dataId, oldDataId, content, className, title, Common().formatDateStringToUTC(startDate))
        return result


    def deleteFixedMultiExcludeProtocolData(self, dataId):
        """Override: Deletes the fixedData attribute.

        :param dataId: The key of the original data
        :type dataId: str
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        result = multiExcludePlugin.deleteFixedMultiExcludeProtocolData(dataId)
        return result

    def addAnnotationMultiExcludeProtocol(self, dataId, annotationText):
        """Override: Add an annotation to the MultiExcludeProtocol object.

        :param dataId: The ID of the data to add the annotation to.
        :type dataId: str
        :param annotationText: The annotation text
        :type annotationText: str
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        return multiExcludePlugin.addAnnotationMultiExcludeProtocol(dataId, annotationText)


    # edit an annotation for the dataId
    def editAnnotationMultiExcludeProtocol(self, dataId, oldAnnotationText, newAnnotationText):
        """Override: Edit an annotation on the MultiExcludeProtocol object.

        :param dataId: The ID of the data to edit the annotation of.
        :type dataId: str
        :param oldAnnotationText: The old annotation text
        :type oldAnnotationText: str
        :param newAnnotationText: The new annotation text
        :type newAnnotationText: str
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        return multiExcludePlugin.editAnnotationMultiExcludeProtocol(dataId, oldAnnotationText, newAnnotationText)


    # delete an annotation for the dataId
    def deleteAnnotationMultiExcludeProtocol(self, dataId, annotationText):
        """Override: Delete one annotation from the MultiExcludeProtocol object.

        :param dataId: The ID of the data to remove the annotation from.
        :type dataId: str
        :param annotationText: The annotation text to remove.
        :type annotationText: str
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        return multiExcludePlugin.deleteAnnotationMultiExcludeProtocol(dataId, annotationText)


    # deletes all annotations for the dataId
    def deleteAllAnnotationsForMultiExcludeProtocol(self, dataId):
        """Override: Delete all annotations from the MultiExcludeProtocol object.

        :param dataId: The ID of the data to remove all annotations from.
        :type dataId: str
        :returns: The modified count.
        """
        multiExcludePlugin = self.getPlugin()
        return multiExcludePlugin.deleteAllAnnotationsForMultiExcludeProtocol(dataId)


    # add an annotation to the timeline, not a datapoint
    def addAnnotationToMultiExcludeProtocolTimeline(self, startTime, annotationText):
        """Override: Ands an annotation to the timeline (not a data point)

        :param startTime: The datetime to add the annotation to
        :type startTime: datetime
        :param annotationText: The annotation text to add.
        :type annotationText: str
        :returns: The modified count.
         """

        multiExcludePlugin = self.getPlugin()
        return multiExcludePlugin.addAnnotationToMultiExcludeProtocolTimeline(Common().formatDateStringToUTC(startDate), annotationText)
