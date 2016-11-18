#  Copyright (C) 2016  Jamie Acosta, Jennifer Weand, Juan Soto, Mark Eby, Mark Smith, Andres Olivas
#
# This file is part of DssVisualizer.
#
# DssVisualizer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DssVisualizer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with DssVisualizer.  If not, see <http://www.gnu.org/licenses/>.

import unittest
from pprint import pprint
from core.apis.datasource.tsharkProtocol import TsharkProtocol


class TsharkProtocolTest(unittest.TestCase):
    def test_searching(self):
        # select by only date
        jsonData = TsharkProtocol().selectTsharkProtocolData('2016-10-18 18:27:42', '2016-10-18 18:27:42',[], [], [])
        self.assertEqual(5, len(jsonData))

        # select by one Tech name
        jsonData = TsharkProtocol().selectTsharkProtocolData('2016-10-18 18:27:42', '2016-10-18 18:27:42',["Alex"], [], [])
        self.assertEqual(2, len(jsonData))

        # select by two Tech names
        jsonData = TsharkProtocol().selectTsharkProtocolData('2016-10-18 18:27:42', '2016-10-18 18:27:42',["Alex", "Julie"], [], [])
        self.assertEqual(3, len(jsonData))

        # select by one event name
        jsonData = TsharkProtocol().selectTsharkProtocolData('2016-10-18 18:27:42', '2016-10-18 18:27:42', [], ["Super Summer Event"], [])
        self.assertEqual(2, len(jsonData))

        # select by two event names
        jsonData = TsharkProtocol().selectTsharkProtocolData('2016-10-18 18:27:42', '2016-10-18 18:27:42', [], ["Super Summer Event", "Another Event"], [])
        self.assertEqual(4, len(jsonData))

        # select by one tech name and one event name
        jsonData = TsharkProtocol().selectTsharkProtocolData('2016-10-18 18:27:42', '2016-10-18 18:27:42', ["Alex"], ["Super Summer Event"], [])
        self.assertEqual(1, len(jsonData))

        # select by two tech names and tow event names
        jsonData = TsharkProtocol().selectTsharkProtocolData('2016-10-18 18:27:42', '2016-10-18 18:27:42', ["Alex", "Tom"], ["Super Summer Event", "Another Event"], [])
        self.assertEqual(3, len(jsonData))

        # select by one event/tech combo
        jsonData = TsharkProtocol().selectTsharkProtocolData('2016-10-18 18:27:42', '2016-10-18 18:27:42', [], [], ["Another Event by Julie"])
        self.assertEqual(1, len(jsonData))

        # select by two event/tech combos
        jsonData = TsharkProtocol().selectTsharkProtocolData('2016-10-18 18:27:42', '2016-10-18 18:27:42', [], [], ["Another Event by Julie", "Unicorns and more! by Willow"])
        self.assertEqual(2, len(jsonData))

        # select by one event/tech combo for a full day
        jsonData = TsharkProtocol().selectTsharkProtocolData('2016-10-18 00:00:01', '2016-10-18 23:59:59', [], [], ["Another Event by Alex"])
        self.assertEqual(79, len(jsonData))
        dataId = jsonData[0]["id"]

        # select by Id
        jsonData = TsharkProtocol().selectTsharkProtocolDataById(dataId)
        self.assertEqual(1, len(jsonData))

    def test_fixedData(self):
        jsonData = TsharkProtocol().selectTsharkProtocolData('2016-10-18 18:27:42', '2016-10-18 18:27:42', [], [], ["Another Event by Alex"])
        dataId = jsonData[0]["id"]

        # insert Fixed MultiExcludeProtocol Data
        insertCount = TsharkProtocol().insertFixedTsharkProtocolData(dataId, '1111', '111 p/s', 'traffic',
                                                                     'new new new',
                                                                     '2016-09-11 17:37:14', True)
        self.assertEqual(1, insertCount)
        jsonData = TsharkProtocol().selectTsharkProtocolDataById(dataId)
        self.assertEqual(jsonData[0]["fixedData"]["traffic_all_id"], '1111')
        self.assertEqual(jsonData[0]["fixedData"]["content"], '111 p/s')
        self.assertEqual(jsonData[0]["fixedData"]["className"], 'traffic')
        self.assertEqual(jsonData[0]["fixedData"]["start"], '2016-09-11 17:37:14')
        self.assertEqual(jsonData[0]["fixedData"]["title"], 'new new new')
        self.assertTrue(jsonData[0]["fixedData"]["isDeleted"])

        # update Fixed MultiExcludeProtocol Data
        modifiedCount = TsharkProtocol().updateFixedTsharkProtocolData(dataId, '5555', '1 p/s', 'traffic123',
                                                                       'eth:ethertype:arp\neth:ethertype:ip:udp:dns\n',
                                                                       '2016-01-02 18:28:00', False)
        self.assertEqual(1, modifiedCount)
        jsonData = TsharkProtocol().selectTsharkProtocolDataById(dataId)
        self.assertEqual(jsonData[0]["fixedData"]["traffic_all_id"], '5555')
        self.assertEqual(jsonData[0]["fixedData"]["content"], '1 p/s')
        self.assertEqual(jsonData[0]["fixedData"]["className"], 'traffic123')
        self.assertEqual(jsonData[0]["fixedData"]["start"], '2016-01-02 18:28:00')
        self.assertEqual(jsonData[0]["fixedData"]["title"], 'eth:ethertype:arp\neth:ethertype:ip:udp:dns\n')
        self.assertFalse(jsonData[0]["fixedData"]["isDeleted"])

        # delete Fixed MultiExcludeProtocol Data
        deletedCount = TsharkProtocol().deleteFixedTsharkProtocolData(dataId)
        self.assertEqual(1, deletedCount)
        jsonData = TsharkProtocol().selectTsharkProtocolDataById(dataId)
        self.assertRaises(KeyError, lambda: jsonData[0]["fixedData"])


    def test_annotations(self):
        jsonData = TsharkProtocol().selectTsharkProtocolData('2016-10-18 18:27:42', '2016-10-18 18:27:42', [], [],
                                                             ["Another Event by Alex"])
        dataId = jsonData[0]["id"]

        # test Annotations
        TsharkProtocol().addAnnotationTsharkProtocol(dataId, 'test')
        TsharkProtocol().addAnnotationTsharkProtocol(dataId, 'test test')
        TsharkProtocol().addAnnotationTsharkProtocol(dataId, 'test test test')
        TsharkProtocol().addAnnotationTsharkProtocol(dataId, 'test test test')
        addedAnns = TsharkProtocol().selectTsharkProtocolDataById(dataId)
        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual('test', addedAnns[0]["annotations"][0]["annotation"])
        self.assertEqual('test test', addedAnns[0]["annotations"][1]["annotation"])
        self.assertEqual('test test test', addedAnns[0]["annotations"][2]["annotation"])

        TsharkProtocol().editAnnotationTsharkProtocol(dataId, 'test test', 'updated annotation!!')
        changedAnn = TsharkProtocol().selectTsharkProtocolDataById(dataId)
        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual('updated annotation!!', changedAnn[0]["annotations"][1]["annotation"])

        TsharkProtocol().deleteAnnotationTsharkProtocol(dataId, 'updated annotation!!')
        deletedChanged = TsharkProtocol().selectTsharkProtocolDataById(dataId)
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))

        TsharkProtocol().deleteAllAnnotationsForTsharkProtocol(dataId)
        deletedAll = TsharkProtocol().selectTsharkProtocolDataById(dataId)
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

        # add Annotation To MultiExcludeProtocol Timeline
        objectId = TsharkProtocol().addAnnotationToTsharkProtocolTimeline('2016-08-01 10:00:00',
                                                                          "here's a timeline annotation", "Alex", "Super Summer Event")
        addtimelineAnnotation = TsharkProtocol().selectTsharkProtocolDataById(objectId)
        pprint(addtimelineAnnotation)
        self.assertEqual(addtimelineAnnotation[0]["className"], 'annotation')
        self.assertEqual(addtimelineAnnotation[0]["start"], '2016-08-01 10:00:00')
        self.assertEqual(addtimelineAnnotation[0]["annotations"]["annotation"], "here's a timeline annotation")
        self.assertEqual(addtimelineAnnotation[0]["metadata"]["techName"], 'Alex')
        self.assertEqual(addtimelineAnnotation[0]["metadata"]["eventName"], 'Super Summer Event')


if __name__ == '__main__':
    unittest.main()

# python -m unittests.test_tsharkProtocol
