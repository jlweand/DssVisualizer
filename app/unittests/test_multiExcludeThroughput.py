import unittest
from pprint import pprint
from core.apis.datasource.multiExcludeThroughput import MultiExcludeThroughput


class MultiExcludeThroughputTest(unittest.TestCase):


    def test_selectMultiExcludeThroughputData(self):
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputData('2016-10-13 00:00:00', '2016-10-13 23:00:00')
        self.assertEqual(23, len(jsonData))

    def test_selectMultiExcludeThroughputDataById(self):
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputDataById(dataId)
        self.assertEqual(1, len(jsonData))

    def test_multiExcludeAnnotations(self):
        MultiExcludeThroughput().addAnnotationMultiExcludeThroughput(dataId, 'test')
        MultiExcludeThroughput().addAnnotationMultiExcludeThroughput(dataId, 'test test')
        MultiExcludeThroughput().addAnnotationMultiExcludeThroughput(dataId, 'test test test')
        MultiExcludeThroughput().addAnnotationMultiExcludeThroughput(dataId, 'test test test')
        addedAnns = MultiExcludeThroughput().selectMultiExcludeThroughputDataById(dataId)

        MultiExcludeThroughput().editAnnotationMultiExcludeThroughput(dataId, 'test test', 'updated annotation!!')
        changedAnn = MultiExcludeThroughput().selectMultiExcludeThroughputDataById(dataId)

        MultiExcludeThroughput().deleteAnnotationMultiExcludeThroughput(dataId, 'updated annotation!!')
        deletedChanged = MultiExcludeThroughput().selectMultiExcludeThroughputDataById(dataId)

        MultiExcludeThroughput().deleteAllAnnotationsForMultiExcludeThroughput(dataId)
        deletedAll = MultiExcludeThroughput().selectMultiExcludeThroughputDataById(dataId)

        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

    def test_insertFixedMultiExcludeData(self):
        modifiedCount = MultiExcludeThroughput().insertFixedMultiExcludeThroughputData(dataId, '2016-10-02 18:28:00', 1111)
        self.assertEqual(1, modifiedCount)

    def test_updateFixedMultiExcludeThroughputData(self):
        modifiedCount = MultiExcludeThroughput().updateFixedMultiExcludeThroughputData(dataId, '2017-01-02 18:28:00', 99999)
        self.assertEqual(1, modifiedCount)

    def test_deleteFixedMultiExcludeThroughputData(self):
        modifiedCount = MultiExcludeThroughput().deleteFixedMultiExcludeThroughputData(dataId)
        self.assertEqual(1, modifiedCount)

    def test_addAnnotationToMultiExcludeThroughputTimeline(self):
        objectId = MultiExcludeThroughput().addAnnotationToMultiExcludeThroughputTimeline('2016-08-01 10:00:00', "here's a timeline annotation")
        changedAnn = MultiExcludeThroughput().selectMultiExcludeThroughputDataById(objectId)
        self.assertIsNotNone(changedAnn)


if __name__ == '__main__':
    dataId = '58004f4f578ad838e44fb2b2'
    unittest.main()

#python -m unittests.test_multiExcludeThroughput
