import unittest
from core.apis.datasource.tsharkThroughput import TsharkThroughput


class TsharkThroughputTest(unittest.TestCase):


    def test_selectTsharkThroughputData(self):
        jsonData = TsharkThroughput().selectTsharkThroughputData('2016-10-13 00:00:00', '2016-10-13 23:00:00')
        self.assertEqual(22, len(jsonData))

    def test_selectTsharkThroughputDataById(self):
        jsonData = TsharkThroughput().selectTsharkThroughputDataById(dataId)
        self.assertEqual(1, len(jsonData))

    def test_tsharkAnnotations(self):
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
    
    def test_fixedTsharkThroughputData(self):
        insertCount = TsharkThroughput().insertFixedTsharkThroughputData(dataId, '2016-10-02 18:28:00', 1111)
        modifiedCount = TsharkThroughput().updateFixedTsharkThroughputData(dataId, '2017-01-02 18:28:00', 99999)
        deletedCount = TsharkThroughput().deleteFixedTsharkThroughputData(dataId)

        self.assertEqual(1, insertCount)
        self.assertEqual(1, modifiedCount)
        self.assertEqual(1, deletedCount)

    def test_addAnnotationToTsharkThroughputTimeline(self):
        objectId = TsharkThroughput().addAnnotationToTsharkThroughputTimeline('2016-08-01 10:00:00', "here's a timeline annotation")
        changedAnn = TsharkThroughput().selectTsharkThroughputDataById(objectId)
        self.assertIsNotNone(changedAnn)


if __name__ == '__main__':
    dataId = '58003459578ad835c848124c'
    unittest.main()

#python -m unittests.test_tsharkThroughput
