from core.apis.datasource.annotations import Annotations

class RAnnotations:

    # return all annotations for the dataObjectId
    def getAnnotations(self, dataObjectId):
        # get the datasource plugin.
        annotationPlugin = self.getInstacneOfPlugin()

        # call the insert method.
        annotations = annotationPlugin.getAnnotations(dataObjectId)
        return annotations

    # add an annotation for the dataObjectId
    def addAnnotation(self, dataObjectId, text):
        return Annotations().addAnnotation(dataObjectId, text);
