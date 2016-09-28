import unittest
from core.apis.datasource.annotations import Annotations
from pymongo import MongoClient
#import ujson
import json

class AnnotationsTest(unittest.TestCase):

    #see https://docs.python.org/3/library/unittest.html for unit test information
    #the bottom part of the page has all the things you can assert.

    def test_addAnnotation(self):
        #annotationId = Annotations().addAnnotation("ObjectId", "text text text")
        annotationId = Annotations().addAnnotation("57eb1d50231bad1f1c990d88", "text text text")
        self.assertIsNotNone(annotationId)

    def test_getAnnotations(self):
        #annotations = Annotations().getAnnotations("dataObjectId")
        annotations = Annotations().getAnnotations("19871011")
        #jsonObject = ujson.loads(annotations)
        jsonObject = json.loads(annotations)
        self.assertEqual(len(jsonObject), 2)

    def test_editAnnotation(self):
        #annotationId = Annotations().editAnnotation("annotationObjectId", "annotationText")
        annotationId = Annotations().editAnnotation("57eb1d50231bad1f1c990d8c", "Updated annotation text")
        self.assertIsNotNone(annotationId)
    
    def test_deleteAnnotation(self):
        #delByAnnObjId = Annotations().deleteAnnotation("annotationObjectId")
        delByAnnObjId = Annotations().deleteAnnotation("57eb2622231bad117ced4ff8")
        self.assertEqual(delByAnnObjId, 1)#<---Since we are deleting by annotation object id, it needs to be one and only one
    
    def test_deleteAllAnnotationsForData(self):
        #delByDataIdCount = Annotations().deleteAllAnnotationsForData("ObjectId")
        delByDataIdCount = Annotations().deleteAllAnnotationsForData(" ")
        self.assertEqual(delByDataIdCount, 1)#<---It depends on the number of documents that match the dataObjectId

if __name__ == '__main__':
    unittest.main()

#run: python -m unittests.test_annotations
#from app/
