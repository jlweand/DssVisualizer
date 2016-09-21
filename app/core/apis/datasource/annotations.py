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
    def getAnnotations(self, dataObjectId):
        #build json
        findJson = {"dataObjectId":dataObjectId}

        # the javascript needs the annotationId back
        #findJson2 = {"_id":0, "dataObjectId":1, "annotationText":1}

        # get the datasource plugin.
        annotationPlugin = self.getInstanceOfPlugin()

        # call the select method.
        annotations = annotationPlugin.getAnnotation(findJson)
        return annotations

    # add an annotation for the dataObjectId
    def addAnnotation(self, dataObjectId, annotationText):
        #build json
        insertJson = {"annotationText":annotationText}

        # get the datasource plugin.
        annotationPlugin = self.getInstanceOfPlugin()

        # call the insert method.
        annotationId = annotationPlugin.addAnnotation("dataObjectId", insertJson)
        return annotationId

    # # edit an annotation for the annotationObjectId
    # def editAnnotation(self, dataObjectId, annotationObjectId):
    #     return 0;

    # # delete an annotation for the annotationObjectId
    # def deleteAnnotation(self, annotationObjectId):
    #     return 0;

    # # deletes all annotations for the dataObjectId
    # def deleteAllAnnotationsForData(self, dataObjectId):
    #     return 0;

#HardCoded String Variables
# dataObjectId = "19900412"
# annotationText = "This is a test for Practicum Class"

#instance of Plugin
# annObj = Annotations()
#print(annObj.getInstanceOfPlugin())

#Calling Class methods
# print (annObj.addAnnotation(dataObjectId, annotationText))
# print (annObj.getAnnotation(dataObjectId))
