import unittest
from core.apis.datasource.multiExcludeThroughput import MultiExcludeThroughput
from pprint import pprint

class MultiExcludeThroughputTest(unittest.TestCase):

    def test_monolithicTestCase(self):
        # select by date
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputData('2016-10-15 11:57:19', '2016-10-15 11:57:19', "", "")
        pprint(jsonData)
        dataId = jsonData[0]["id"] #list index out of range ERROR
        self.assertEqual(1, len(jsonData))

        # select by Id
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputDataById(dataId)
        self.assertEqual(1, len(jsonData))

        #select by Tech name
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputData('2016-10-15 11:59:27', '2016-10-15 11:59:27', "Alex", "")
        self.assertEqual(1, len(jsonData))
        #select by event name
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputData('2016-10-15 11:59:27', '2016-10-15 11:59:27', "", "Super Summer Event")
        self.assertEqual(1, len(jsonData))

        #select by tech name AND event name
        jsonData = MultiExcludeThroughput().selectMultiExcludeThroughputData('2016-10-15 11:59:27', '2016-10-15 11:59:27', "Alex", "Super Summer Event")
        self.assertEqual(1, len(jsonData))

        # test Annotations
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

        # insert Fixed MultiExcludeThroughput Data
        modifiedCount = MultiExcludeThroughput().insertFixedMultiExcludeThroughputData(dataId, '2016-10-02 18:28:00', 1111)
        self.assertEqual(1, modifiedCount)

        # update Fixed MultiExcludeThroughput Data
        modifiedCount = MultiExcludeThroughput().updateFixedMultiExcludeThroughputData(dataId, '2017-01-02 18:28:00', 99999)
        self.assertEqual(1, modifiedCount)

        # delete Fixed MultiExcludeThroughput Data
        modifiedCount = MultiExcludeThroughput().deleteFixedMultiExcludeThroughputData(dataId)
        self.assertEqual(1, modifiedCount)

        # add Annotation To MultiExcludeThroughput Timeline
        objectId = MultiExcludeThroughput().addAnnotationToMultiExcludeThroughputTimeline('2016-08-01 10:00:00', "here's a timeline annotation")
        addtimelineAnnotation = MultiExcludeThroughput().selectMultiExcludeThroughputDataById(objectId)
        pprint(addtimelineAnnotation)
        self.assertIsNotNone(addtimelineAnnotation)


if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_multiExcludeThroughput
