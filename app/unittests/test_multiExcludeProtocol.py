import unittest
from core.apis.datasource.multiExcludeProtocol import MultiExcludeProtocol


class MultiExcludeProtocolTest(unittest.TestCase):

    def test_monolithicTestCase(self):
        # select by date
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolData('2016-10-18 18:27:20', '2016-10-18 18:27:25')
        dataId = jsonData[0]["id"]
        self.assertEqual(1, len(jsonData))

        # select by Id
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(dataId)
        self.assertEqual(1, len(jsonData))

        # test Annotations
        MultiExcludeProtocol().addAnnotationMultiExcludeProtocol(dataId, 'test')
        MultiExcludeProtocol().addAnnotationMultiExcludeProtocol(dataId, 'test test')
        MultiExcludeProtocol().addAnnotationMultiExcludeProtocol(dataId, 'test test test')
        MultiExcludeProtocol().addAnnotationMultiExcludeProtocol(dataId, 'test test test')
        addedAnns = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(dataId)

        MultiExcludeProtocol().editAnnotationMultiExcludeProtocol(dataId, 'test test', 'updated annotation!!')
        changedAnn = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(dataId)

        MultiExcludeProtocol().deleteAnnotationMultiExcludeProtocol(dataId, 'updated annotation!!')
        deletedChanged = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(dataId)

        MultiExcludeProtocol().deleteAllAnnotationsForMultiExcludeProtocol(dataId)
        deletedAll = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(dataId)

        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

        # insert Fixed MultiExcludeProtocol Data
        modifiedCount = MultiExcludeProtocol().insertFixedMultiExcludeProtocolData(dataId, '57f18727231bad12ecba99e4', '1 p/s', 'traffic', 'eth:ethertype:arp\neth:ethertype:ip:udp:dns\n', '2016-17-02 18:28:00')
        self.assertEqual(1, modifiedCount)

        # update Fixed MultiExcludeProtocol Data
        modifiedCount = MultiExcludeProtocol().updateFixedMultiExcludeProtocolData(dataId, '57f18727231bad12ecba99e4', '2 p/s', 'traffic', 'eth:ethertype:arp\neth:ethertype:ip:udp:dns\n', '2016-10-02 18:28:00')
        self.assertEqual(1, modifiedCount)

        # delete Fixed MultiExcludeProtocol Data
        modifiedCount = MultiExcludeProtocol().deleteFixedMultiExcludeProtocolData(dataId)
        self.assertEqual(1, modifiedCount)

        # add Annotation To MultiExcludeProtocol Timeline
        objectId = MultiExcludeProtocol().addAnnotationToMultiExcludeProtocolTimeline('2016-08-01 10:00:00', "here's a timeline annotation")
        changedAnn = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(objectId)
        self.assertIsNotNone(changedAnn)


if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_multiExcludeProtocol
