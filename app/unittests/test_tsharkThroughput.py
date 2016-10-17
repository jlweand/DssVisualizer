import unittest
from core.apis.datasource.tsharkThroughput import TsharkThroughput
from pprint import pprint

class TsharkThroughputTest(unittest.TestCase):

    def test_monolithicTestCase(self):
        # select by date
        jsonData = TsharkThroughput().selectTsharkThroughputData('2016-10-15 11:57:19', '2016-10-15 11:57:19')
        pprint(jsonData)
        dataId = jsonData[0]["id"]
        self.assertEqual(1, len(jsonData))

        # select by Id
        jsonData = TsharkThroughput().selectTsharkThroughputDataById(dataId)
        self.assertEqual(1, len(jsonData))

        # test Annotations
        TsharkThroughput().addAnnotationTsharkThroughput(dataId, 'test')
        TsharkThroughput().addAnnotationTsharkThroughput(dataId, 'test test')
        TsharkThroughput().addAnnotationTsharkThroughput(dataId, 'test test test')
        TsharkThroughput().addAnnotationTsharkThroughput(dataId, 'test test test')
        addedAnns = TsharkThroughput().selectTsharkThroughputDataById(dataId)

        TsharkThroughput().editAnnotationTsharkThroughput(dataId, 'test test', 'updated annotation!!')
        changedAnn = TsharkThroughput().selectTsharkThroughputDataById(dataId)

        TsharkThroughput().deleteAnnotationTsharkThroughput(dataId, 'updated annotation!!')
        deletedChanged = TsharkThroughput().selectTsharkThroughputDataById(dataId)

        TsharkThroughput().deleteAllAnnotationsForTsharkThroughput(dataId)
        deletedAll = TsharkThroughput().selectTsharkThroughputDataById(dataId)

        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

        # insert Fixed MultiExcludeThroughput Data
        modifiedCount = TsharkThroughput().insertFixedTsharkThroughputData(dataId, '2016-10-02 18:28:00', 1111)
        self.assertEqual(1, modifiedCount)

        # update Fixed MultiExcludeThroughput Data
        modifiedCount = TsharkThroughput().updateFixedTsharkThroughputData(dataId, '2017-01-02 18:28:00', 99999)
        self.assertEqual(1, modifiedCount)

        # delete Fixed MultiExcludeThroughput Data
        modifiedCount = TsharkThroughput().deleteFixedTsharkThroughputData(dataId)
        self.assertEqual(1, modifiedCount)

        # add Annotation To MultiExcludeThroughput Timeline
        objectId = TsharkThroughput().addAnnotationToTsharkThroughputTimeline('2016-08-01 10:00:00', "here's a timeline annotation")
        addtimelineAnnotation = TsharkThroughput().selectTsharkThroughputDataById(objectId)
        pprint(addtimelineAnnotation)
        self.assertIsNotNone(addtimelineAnnotation)


if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_tsharkThroughput
