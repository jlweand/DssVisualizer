import unittest
from pprint import pprint
from core.apis.datasource.multiIncludeProtocol import MultiIncludeProtocol


class MultiIncludeProtocolTest(unittest.TestCase):


    def test_monolithicTestCase(self):
        # select by date
        jsonData = MultiIncludeProtocol().selectMultiIncludeProtocolData('2016-10-15 11:57:18', '2016-10-15 11:57:18', "", "")
        pprint(jsonData)
        dataId = jsonData[0]["id"]
        self.assertEqual(1, len(jsonData))

        # select by Id
        jsonData = MultiIncludeProtocol().selectMultiIncludeProtocolDataById(dataId)
        self.assertEqual(1, len(jsonData))

        #select by Tech name
        jsonData = MultiIncludeProtocol().selectMultiIncludeProtocolData('2016-10-15 11:59:27', '2016-10-15 11:59:27', "Alex", "")
        self.assertEqual(1, len(jsonData))

        #select by event name
        jsonData = MultiIncludeProtocol().selectMultiIncludeProtocolData('2016-10-15 11:59:27', '2016-10-15 11:59:27', "", "Super Summer Event")
        self.assertEqual(1, len(jsonData))

        #select by tech name AND event name
        jsonData = MultiIncludeProtocol().selectMultiIncludeProtocolData('2016-10-15 11:59:27', '2016-10-15 11:59:27', "Alex", "Super Summer Event")
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
        modifiedCount = MultiIncludeProtocol().insertFixedMultiIncludeProtocolData(dataId, '1111', '29 p/s', 'traffic', 'eth:ethertype:arp\neth:ethertype:ip:udp:dns\n', '2016-12-02 18:28:00')
        self.assertEqual(1, modifiedCount)

        # update Fixed MultiExcludeProtocol Data
        modifiedCount = MultiIncludeProtocol().updateFixedMultiIncludeProtocolData(dataId, '7777', '2 p/s', 'traffic', 'eth:ethertype:arp\neth:ethertype:ip:udp:dns\n', '2016-10-02 18:28:00')
        self.assertEqual(1, modifiedCount)

        # delete Fixed MultiExcludeProtocol Data
        modifiedCount = MultiIncludeProtocol().deleteFixedMultiIncludeProtocolData(dataId)
        self.assertEqual(1, modifiedCount)

        # add Annotation To MultiExcludeProtocol Timeline
        objectId = MultiIncludeProtocol().addAnnotationToMultiIncludeProtocolTimeline('2016-08-01 10:00:00', "here's a timeline annotation")
        addtimelineAnnotation = MultiIncludeProtocol().selectMultiIncludeProtocolDataById(objectId)
        pprint(addtimelineAnnotation)
        self.assertIsNotNone(addtimelineAnnotation)


if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_multiIncludeProtocol
