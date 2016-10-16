import unittest
from pprint import pprint
from core.apis.datasource.multiExcludeProtocol import MultiExcludeProtocol


class MultiExcludeProtocolTest(unittest.TestCase):


    def test_selectMultiExcludeProtocolData(self):
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolData('2016-10-13 00:00:00', '2016-10-13 23:00:00')
        self.assertEqual(23, len(jsonData))

    def test_selectMultiExcludeProtocolDataById(self):
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(dataId)
        self.assertEqual(1, len(jsonData))

    # def test_multiExcludeProtocolAnnotations(self):
    #     MultiExcludeProtocol().addAnnotationMultiExcludeProtocol(dataId, 'test')
    #     MultiExcludeProtocol().addAnnotationMultiExcludeProtocol(dataId, 'test test')
    #     MultiExcludeProtocol().addAnnotationMultiExcludeProtocol(dataId, 'test test test')
    #     MultiExcludeProtocol().addAnnotationMultiExcludeProtocol(dataId, 'test test test')
    #     addedAnns = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(dataId)

    #     MultiExcludeProtocol().editAnnotationMultiExcludeProtocol(dataId, 'test test', 'updated annotation!!')
    #     changedAnn = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(dataId)

    #     MultiExcludeProtocol().deleteAnnotationMultiExcludeProtocol(dataId, 'updated annotation!!')
    #     deletedChanged = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(dataId)

    #     MultiExcludeProtocol().deleteProtocolAnnotationsForMultiExcludeProtocol(dataId)
    #     deletedAll = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(dataId)

    #     self.assertEqual(3, len(addedAnns[0]["annotations"]))
    #     self.assertEqual(2, len(deletedChanged[0]["annotations"]))
    #     self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

    def test_insertFixedMultiExcludeProtocolData(self):
        modifiedCount = MultiExcludeProtocol().insertFixedMultiExcludeProtocolData(dataId, '2016-10-02 18:28:00', 1111)
        self.assertEqual(1, modifiedCount)

    def test_updateFixedMultiExcludeProtocolData(self):
        modifiedCount = MultiExcludeProtocol().updateFixedMultiExcludeProtocolData(dataId, '2017-01-02 18:28:00', 99999)
        self.assertEqual(1, modifiedCount)

    def test_deleteFixedMultiExcludeProtocolData(self):
        modifiedCount = MultiExcludeProtocol().deleteFixedMultiExcludeProtocolData(dataId)
        self.assertEqual(1, modifiedCount)

    # def test_addAnnotationToMultiExcludeProtocolTimeline(self):
    #     objectId = MultiExcludeProtocol().addAnnotationToMultiExcludeProtocolTimeline('2016-08-01 10:00:00', "here's a timeline annotation")
    #     changedAnn = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(objectId)
    #     self.assertIsNotNone(changedAnn)


if __name__ == '__main__':
    dataId = '58003bd2231bad19dcc398c2'
    unittest.main()

#python -m unittests.test_multiExcludeProtocol
