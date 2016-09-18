import ujson

class Annotations:

    def getInstacneOfPlugin(self):
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
        # get the datasource plugin.
        annotationPlugin = self.getInstacneOfPlugin()

        # call the insert method.
        annotations = annotationPlugin.getAnnotations(dataObjectId)
        return annotations

    # add an annotation for the dataObjectId
    def addAnnotation(self, dataObjectId):
        return 0;

    # edit an annotation for the annotationObjectId
    def editAnnotation(self, dataObjectId, annotationObjectId):
        return 0;

    # delete an annotation for the annotationObjectId
    def deleteAnnotation(self, annotationObjectId):
        return 0;

    # deletes all annotations for the dataObjectId
    def deleteAllAnnotationsForData(self, dataObjectId):
        return 0;
