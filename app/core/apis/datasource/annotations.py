#import ujson
#strings received, create json and then pass it to the class

class Annotations:

    def getInstanceOfPlugin(self):
        # todo get this information from the config.json
        module = "plugins.datasource.mongodb.annotations"
        classname = "Annotations"

        #import the module by saying 'from myApp.models import Blog'
        module = __import__(module, {}, {}, classname)

        #now you can instantiate the class
        obj = getattr(module, classname )()
        return obj

    # return all annotations for the dataObjectId
    def getAnnotations(self, dataId):
        # get the datasource plugin.
        annotationPlugin = self.getInstanceOfPlugin()

        # call the select method.
        annotations = annotationPlugin.getAnnotation(dataId)
        return annotations

    # add an annotation for the dataObjectId
    def addAnnotation(self, dataObjectId, annotationText):
        # get the datasource plugin.
        annotationPlugin = self.getInstanceOfPlugin()

        # call the insert method.
        annotationId = annotationPlugin.addAnnotation(dataObjectId, annotationText)
        return annotationId

    # edit an annotation for the annotationObjectId
    def editAnnotation(self, annotationObjectId, annotationText):
        # get the datasource plugin.
        annotationPlugin = self.getInstanceOfPlugin()

        # call the update method.
        updatedAnnotationId = annotationPlugin.editAnnotation(annotationObjectId, annotationText)
        return updatedAnnotationId

    # delete an annotation for the annotationObjectId
    def deleteAnnotation(self, annotationObjectId):
        # get the datasource plugin.
        annotationPlugin = self.getInstanceOfPlugin()

        #call deleteAnnotation method
        delByAnnObjId = annotationPlugin.deleteAnnotation(annotationObjectId)
        return delByAnnObjId

    # deletes all annotations for the dataObjectId
    def deleteAllAnnotationsForData(self, dataObjectId):
        # get the datasource plugin.
        annotationPlugin = self.getInstanceOfPlugin()

        #call deleteAnnotation method
        delByDataIdCount = annotationPlugin.deleteAllAnnotationsForData(dataObjectId)
        return delByDataIdCount

#BELOW IS FOR TESGING
# #HardCoded String Variables
# dataObjectId = "TODAY"
# annotationText = "TEST from API"

# #instance of Plugin
# annObj = Annotations()
# print(annObj.getInstanceOfPlugin())

# #Calling Class methods
# print (annObj.addAnnotation(dataObjectId, annotationText))
# print (annObj.getAnnotation(dataObjectId))
