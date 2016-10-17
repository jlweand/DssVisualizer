import unittest
from pprint import pprint
from core.apis.datasource.multiIncludeProtocol import MultiIncludeProtocol


class MultiIncludeProtocolTest(unittest.TestCase):


    def test_selectMultiIncludeProtocolData(self):
        jsonData = MultiIncludeProtocol().selectMultiIncludeProtocolData('2016-10-12 17:37:10', '2016-10-12 17:37:13')
        # pprint(jsonData)
        self.assertEqual(1, len(jsonData))

    def test_selectMultiIncludeProtocolDataById(self):
        jsonData = MultiIncludeProtocol().selectMultiIncludeProtocolDataById(dataId)
        self.assertEqual(1, len(jsonData))

    def test_multiIncludeProtocolAnnotations(self):
        MultiIncludeProtocol().addAnnotationMultiIncludeProtocol(dataId, 'test')
        MultiIncludeProtocol().addAnnotationMultiIncludeProtocol(dataId, 'test test')
        MultiIncludeProtocol().addAnnotationMultiIncludeProtocol(dataId, 'test test test')
        MultiIncludeProtocol().addAnnotationMultiIncludeProtocol(dataId, 'test test test')
        addedAnns = MultiIncludeProtocol().selectMultiIncludeProtocolDataById(dataId)

        MultiIncludeProtocol().editAnnotationMultiIncludeProtocol(dataId, 'test test', 'updated annotation!!')
        changedAnn = MultiIncludeProtocol().selectMultiIncludeProtocolDataById(dataId)

        MultiIncludeProtocol().deleteAnnotationMultiIncludeProtocol(dataId, 'updated annotation!!')
        deletedChanged = MultiIncludeProtocol().selectMultiIncludeProtocolDataById(dataId)

        MultiIncludeProtocol().deleteAllAnnotationsForMultiIncludeProtocol(dataId)
        deletedAll = MultiIncludeProtocol().selectMultiIncludeProtocolDataById(dataId)

        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

    def test_insertFixedMultiIncludeProtocolData(self):
        modifiedCount = MultiIncludeProtocol().insertFixedMultiIncludeProtocolData(dataId, '57f18727231bad12ecba99e4', '29 p/s', 'traffic', 'eth:ethertype:arp\neth:ethertype:ip:udp:dns\n', '2016-17-02 18:28:00')
        self.assertEqual(1, modifiedCount)

    def test_updateFixedMultiIncludeProtocolData(self):
        modifiedCount = MultiIncludeProtocol().updateFixedMultiIncludeProtocolData(dataId, '57f18727231bad12ecba99e4', '2 p/s', 'traffic', 'eth:ethertype:arp\neth:ethertype:ip:udp:dns\n', '2016-10-02 18:28:00')
        self.assertEqual(1, modifiedCount)

    def test_deleteFixedMultiIncludeProtocolData(self):
        modifiedCount = MultiIncludeProtocol().deleteFixedMultiIncludeProtocolData(dataId)
        self.assertEqual(1, modifiedCount)

    def test_addAnnotationToMultiIncludeProtocolTimeline(self):
        objectId = MultiIncludeProtocol().addAnnotationToMultiIncludeProtocolTimeline('2016-08-01 10:00:00', "here's a timeline annotation")
        changedAnn = MultiIncludeProtocol().selectMultiIncludeProtocolDataById(objectId)
        self.assertIsNotNone(changedAnn)


if __name__ == '__main__':
    dataId = '58050233578ad8fa1837d703'
    unittest.main()

#python -m unittests.test_multiIncludeProtocol
