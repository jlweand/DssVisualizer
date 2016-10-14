import unittest
from pprint import pprint
from core.apis.datasource.multiIncludeThroughput import MultiIncludeThroughput


class MultiIncludeThroughputTest(unittest.TestCase):
    def test_selectMultiIncludeThroughputData(self):
        jsonData = MultiIncludeThroughput().selectMultiIncludeThroughputData('2016-10-13 00:00:00', '2016-10-13 23:00:00')
        self.assertEqual(23, len(jsonData))

    def test_selectMultiIncludeThroughputDataById(self):
        jsonData = MultiIncludeThroughput().selectMultiIncludeThroughputDataById(dataId)
        self.assertEqual(1, len(jsonData))

    def test_multiIncludeAnnotations(self):
        MultiIncludeThroughput().addAnnotationMultiIncludeThroughput(dataId, 'test')
        MultiIncludeThroughput().addAnnotationMultiIncludeThroughput(dataId, 'test test')
        MultiIncludeThroughput().addAnnotationMultiIncludeThroughput(dataId, 'test test test')
        MultiIncludeThroughput().addAnnotationMultiIncludeThroughput(dataId, 'test test test')
        addedAnns = MultiIncludeThroughput().selectMultiIncludeThroughputDataById(dataId)

        MultiIncludeThroughput().editAnnotationMultiIncludeThroughput(dataId, 'test test', 'updated annotation!!')
        changedAnn = MultiIncludeThroughput().selectMultiIncludeThroughputDataById(dataId)

        MultiIncludeThroughput().deleteAnnotationMultiIncludeThroughput(dataId, 'updated annotation!!')
        deletedChanged = MultiIncludeThroughput().selectMultiIncludeThroughputDataById(dataId)

        MultiIncludeThroughput().deleteAllAnnotationsForMultiIncludeThroughput(dataId)
        deletedAll = MultiIncludeThroughput().selectMultiIncludeThroughputDataById(dataId)

        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

    def test_insertFixedMultiIncludeData(self):
        modifiedCount = MultiIncludeThroughput().insertFixedMultiIncludeThroughputData(dataId, '2016-10-02 18:28:00', 1111)
        self.assertEqual(1, modifiedCount)

    def test_updateFixedMultiIncludeThroughputData(self):
        modifiedCount = MultiIncludeThroughput().updateFixedMultiIncludeThroughputData(dataId, '2017-01-02 18:28:00', 99999)
        self.assertEqual(1, modifiedCount)

    def test_deleteFixedMultiIncludeThroughputData(self):
        modifiedCount = MultiIncludeThroughput().deleteFixedMultiIncludeThroughputData(dataId)
        self.assertEqual(1, modifiedCount)

    def test_addAnnotationToMultiIncludeThroughputTimeline(self):
        objectId = MultiIncludeThroughput().addAnnotationToMultiIncludeThroughputTimeline('2016-08-01 10:00:00', "here's a timeline annotation")
        changedAnn = MultiIncludeThroughput().selectMultiIncludeThroughputDataById(objectId)
        self.assertIsNotNone(changedAnn)


if __name__ == '__main__':
    dataId = '58004f4f578ad838e44fb300'
    unittest.main()

# python -m unittests.test_multiIncludeThroughput
