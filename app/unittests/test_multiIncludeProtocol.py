import unittest
from pprint import pprint
from core.apis.datasource.multiIncludeProtocol import MultiIncludeProtocol


class MultiIncludeProtocolTest(unittest.TestCase):


    def test_monolithicTestCase(self):
        # select by date
        jsonData = MultiIncludeProtocol().selectMultiIncludeProtocolData('2016-10-15 11:57:18', '2016-10-15 11:57:20')
        dataId = jsonData[0]["id"]
        self.assertEqual(1, len(jsonData))

        # select by Id
        jsonData = MultiIncludeProtocol().selectMultiIncludeProtocolDataById(dataId)
        self.assertEqual(1, len(jsonData))

        # test Annotations
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

        # insert Fixed MultiExcludeProtocol Data
        modifiedCount = MultiIncludeProtocol().insertFixedMultiIncludeProtocolData(dataId, '57f18727231bad12ecba99e4', '29 p/s', 'traffic', 'eth:ethertype:arp\neth:ethertype:ip:udp:dns\n', '2016-17-02 18:28:00')
        self.assertEqual(1, modifiedCount)

        # update Fixed MultiExcludeProtocol Data
        modifiedCount = MultiIncludeProtocol().updateFixedMultiIncludeProtocolData(dataId, '57f18727231bad12ecba99e4', '2 p/s', 'traffic', 'eth:ethertype:arp\neth:ethertype:ip:udp:dns\n', '2016-10-02 18:28:00')
        self.assertEqual(1, modifiedCount)

        # delete Fixed MultiExcludeProtocol Data
        modifiedCount = MultiIncludeProtocol().deleteFixedMultiIncludeProtocolData(dataId)
        self.assertEqual(1, modifiedCount)

        # add Annotation To MultiExcludeProtocol Timeline
        objectId = MultiIncludeProtocol().addAnnotationToMultiIncludeProtocolTimeline('2016-08-01 10:00:00', "here's a timeline annotation")
        changedAnn = MultiIncludeProtocol().selectMultiIncludeProtocolDataById(objectId)
        self.assertIsNotNone(changedAnn)


if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_multiIncludeProtocol
