import unittest
from core.apis.datasource.annotations import Annotations
from pymongo import MongoClient
import ujson

class AnnotationsTest(unittest.TestCase):

    # see https://docs.python.org/3/library/unittest.html for unit test information
    # the bottom part of the page has all the things you can assert.

    def test_addAnnotation(self):
        annotationId = Annotations().addAnnotation("OjbectId", "text text text")
        self.assertIsNotNone(annotationId)

    def test_getAnnotations(self):
        annotations = Annotations().getAnnotations("dataObjectId")
        jsonObject = ujson.loads(annotations)
        self.assertEqual(len(jsonObject), 10)

    # def test_editAnnotation(self):
    #     self.assertEqual()
    #
    # def test_deleteAnnotation(self):
    #     self.assertEqual()
    #
    # def test_deleteAllAnnotationsForData(self):
    #     self.assertEqual()

if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_annotations
