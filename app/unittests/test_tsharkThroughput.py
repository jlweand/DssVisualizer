import unittest
from pprint import pprint
from core.apis.datasource.tsharkThroughput import TsharkThroughput


class TsharkThroughputTest(unittest.TestCase):


    def test_selectTsharkData(self):
        jsonData = TsharkThroughput().selectTsharkData('2016-10-13 00:00:00', '2016-10-13 23:00:00')
        self.assertEqual(22, len(jsonData))

    def test_selectTsharkDataById(self):
        jsonData = TsharkThroughput().selectTsharkDataById(dataId)
        pprint(jsonData)
        self.assertEqual(1, len(jsonData))

    def test_keyPressAnnotations(self):
        TsharkThroughput().addAnnotationTshark(dataId, 'test')
        TsharkThroughput().addAnnotationTshark(dataId, 'test test')
        TsharkThroughput().addAnnotationTshark(dataId, 'test test test')
        TsharkThroughput().addAnnotationTshark(dataId, 'test test test')
        addedAnns = TsharkThroughput().selectTsharkDataById(dataId)

        TsharkThroughput().editAnnotationTshark(dataId, 'test test', 'updated annotation!!')
        changedAnn = TsharkThroughput().selectTsharkDataById(dataId)

        TsharkThroughput().deleteAnnotationTshark(dataId, 'updated annotation!!')
        deletedChanged = TsharkThroughput().selectTsharkDataById(dataId)

        TsharkThroughput().deleteAllAnnotationsForTshark(dataId)
        deletedAll = TsharkThroughput().selectTsharkDataById(dataId)

        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])
    
    def test_insertFixedTsharkData(self):
        modifiedCount = TsharkThroughput().insertFixedTsharkData(dataId, '2016-10-02 18:28:00', 1111)
        self.assertEqual(1, modifiedCount)

    def test_updateFixedTsharkData(self):
        modifiedCount = TsharkThroughput().updateFixedTsharkData(dataId, '2017-01-02 18:28:00', 99999)
        self.assertEqual(1, modifiedCount)

    def test_deleteFixedTsharkData(self):
        modifiedCount = TsharkThroughput().deleteFixedTsharkData(dataId)
        jsonData2 = TsharkThroughput().selectTsharkDataById(dataId)
        pprint(jsonData2)
        self.assertEqual(1, modifiedCount)

    def test_addAnnotationToTsharkTimeline(self):
        objectId = TsharkThroughput().addAnnotationToTsharkTimeline('2016-08-01 10:00:00', "here's a timeline annotation")
        changedAnn = TsharkThroughput().selectTsharkDataById(objectId)
        pprint(changedAnn)
        self.assertIsNotNone(changedAnn)


if __name__ == '__main__':
    dataId = '58003459578ad835c848124c'
    unittest.main()

#python -m unittests.test_tsharkThroughput
