import unittest
from pprint import pprint
from core.apis.datasource.tsharkProtocol import TsharkProtocol


class TsharkProtocolTest(unittest.TestCase):


    def test_selectTsharkProtocolData(self):
        jsonData = TsharkProtocol().selectTsharkProtocolData('2016-10-12 17:36:14', '2016-10-12 17:36:20')
        # pprint(jsonData)
        self.assertEqual(1, len(jsonData))

    def test_selectTsharkProtocolDataById(self):
        jsonData = TsharkProtocol().selectTsharkProtocolDataById(dataId)
        self.assertEqual(1, len(jsonData))

    def test_tsharkAnnotations(self):
        TsharkProtocol().addAnnotationTsharkProtocol(dataId, 'test')
        TsharkProtocol().addAnnotationTsharkProtocol(dataId, 'test test')
        TsharkProtocol().addAnnotationTsharkProtocol(dataId, 'test test test')
        TsharkProtocol().addAnnotationTsharkProtocol(dataId, 'test test test')
        addedAnns = TsharkProtocol().selectTsharkProtocolDataById(dataId)

        TsharkProtocol().editAnnotationTsharkProtocol(dataId, 'test test', 'updated annotation!!')
        changedAnn = TsharkProtocol().selectTsharkProtocolDataById(dataId)

        TsharkProtocol().deleteAnnotationTsharkProtocol(dataId, 'updated annotation!!')
        deletedChanged = TsharkProtocol().selectTsharkProtocolDataById(dataId)

        TsharkProtocol().deleteAllAnnotationsForTsharkProtocol(dataId)
        deletedAll = TsharkProtocol().selectTsharkProtocolDataById(dataId)

        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

    def test_insertFixedTsharkProtocolData(self):
        insertCount = TsharkProtocol().insertFixedTsharkProtocolData(dataId, '57f18727231bad12ecba99e4', '29 p/s', 'traffic', 'eth:ethertype:arp\neth:ethertype:ip:udp:dns\n', '2016-17-02 18:28:00')
        self.assertEqual(1, insertCount)

    def test_UpdateFixedTsharkProtocolData(self):
        modifiedCount = TsharkProtocol().updateFixedTsharkProtocolData(dataId, '57f18727231bad12ecba99e4', '1 p/s', 'traffic', 'eth:ethertype:arp\neth:ethertype:ip:udp:dns\n', '2016-10-02 18:28:00')
        self.assertEqual(1, modifiedCount)

    def test_deleteFixedTsharkProtocolData(self):
        deletedCount = TsharkProtocol().deleteFixedTsharkProtocolData(dataId)
        self.assertEqual(1, deletedCount)

    def test_addAnnotationToTsharkProtocolTimeline(self):
        objectId = TsharkProtocol().addAnnotationToTsharkProtocolTimeline('2016-08-01 10:00:00', "here's a timeline annotation")
        changedAnn = TsharkProtocol().selectTsharkProtocolDataById(objectId)
        self.assertIsNotNone(changedAnn)


if __name__ == '__main__':
    dataId = '58050233578ad8fa1837d737'
    unittest.main()

#python -m unittests.test_tsharkProtocol
