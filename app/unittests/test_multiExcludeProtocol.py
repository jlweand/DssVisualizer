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
from core.apis.datasource.multiExcludeProtocol import MultiExcludeProtocol
from pprint import pprint


class MultiExcludeProtocolTest(unittest.TestCase):

    def test_searching(self):
        # select by only date
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolData('2016-10-15 11:59:27', '2016-10-15 11:59:27', [], [], [])
        self.assertEqual(5, len(jsonData))

        # select by one Tech name
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolData('2016-10-15 11:59:27', '2016-10-15 11:59:27', ["Alex"], [], [])
        self.assertEqual(2, len(jsonData))

        # select by two Tech names
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolData('2016-10-15 11:59:27', '2016-10-15 11:59:27', ["Alex", "Julie"], [], [])
        self.assertEqual(3, len(jsonData))

        # select by one event name
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolData('2016-10-15 11:59:27', '2016-10-15 11:59:27', [], ["Super Summer Event"], [])
        self.assertEqual(2, len(jsonData))

        # select by two event names
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolData('2016-10-15 11:59:27', '2016-10-15 11:59:27', [], ["Super Summer Event", "Another Event"], [])
        self.assertEqual(4, len(jsonData))

        # select by one tech name and one event name
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolData('2016-10-15 11:59:27', '2016-10-15 11:59:27', ["Alex"], ["Super Summer Event"], [])
        self.assertEqual(1, len(jsonData))

        # select by two tech names and tow event names
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolData('2016-10-15 11:59:27', '2016-10-15 11:59:27', ["Alex", "Tom"], ["Super Summer Event", "Another Event"], [])
        self.assertEqual(3, len(jsonData))

        # select by one event/tech combo
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolData('2016-10-15 11:59:27', '2016-10-15 11:59:27', [], [], ["Another Event by Julie"])
        self.assertEqual(1, len(jsonData))

        # select by two event/tech combos
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolData('2016-10-15 11:59:27', '2016-10-15 11:59:27', [], [], ["Another Event by Julie", "Unicorns and more! by Willow"])
        self.assertEqual(2, len(jsonData))

        # select by one event/tech combo for a full day
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolData('2016-10-18 00:00:01', '2016-10-18 23:59:59', [], [], ["Another Event by Alex"])
        self.assertEqual(77, len(jsonData))
        dataId = jsonData[0]["id"]

        # select by Id
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(dataId)
        self.assertEqual(1, len(jsonData))

    def test_fixedData(self):
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolData('2016-10-15 11:59:27', '2016-10-15 11:59:27', [], [], ["Another Event by Alex"])
        dataId = jsonData[0]["id"]

        # insert Fixed MultiExcludeProtocol Data
        modifiedCount = MultiExcludeProtocol().insertFixedMultiExcludeProtocolData(dataId, '55555', '111 p/s', 'traffic',
                                                                                   'new new new',
                                                                                   '2016-12-02 18:28:00', True)
        self.assertEqual(1, modifiedCount)
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(dataId)
        self.assertEqual(jsonData[0]["fixedData"]["traffic_all_id"], '55555')
        self.assertEqual(jsonData[0]["fixedData"]["content"], '111 p/s')
        self.assertEqual(jsonData[0]["fixedData"]["className"], 'traffic')
        self.assertEqual(jsonData[0]["fixedData"]["start"], '2016-12-02 18:28:00')
        self.assertEqual(jsonData[0]["fixedData"]["title"], 'new new new')
        self.assertTrue(jsonData[0]["fixedData"]["isDeleted"])

        # update Fixed MultiExcludeProtocol Data
        modifiedCount = MultiExcludeProtocol().updateFixedMultiExcludeProtocolData(dataId, '7777', '222 p/s', 'traffic123',
                                                                                   'eth:ethertype:arp\neth:ethertype:ip:udp:dns\n',
                                                                                   '2016-01-02 18:28:00', False)
        self.assertEqual(1, modifiedCount)
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(dataId)
        self.assertEqual(jsonData[0]["fixedData"]["traffic_all_id"], '7777')
        self.assertEqual(jsonData[0]["fixedData"]["content"], '222 p/s')
        self.assertEqual(jsonData[0]["fixedData"]["className"], 'traffic123')
        self.assertEqual(jsonData[0]["fixedData"]["start"], '2016-01-02 18:28:00')
        self.assertEqual(jsonData[0]["fixedData"]["title"], 'eth:ethertype:arp\neth:ethertype:ip:udp:dns\n')
        self.assertFalse(jsonData[0]["fixedData"]["isDeleted"])

        # delete Fixed MultiExcludeProtocol Data
        modifiedCount = MultiExcludeProtocol().deleteFixedMultiExcludeProtocolData(dataId)
        self.assertEqual(1, modifiedCount)
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(dataId)
        self.assertRaises(KeyError, lambda: jsonData[0]["fixedData"])


    def test_annotations(self):
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolData('2016-10-15 11:59:27', '2016-10-15 11:59:27', [], [], ["Another Event by Alex"])
        dataId = jsonData[0]["id"]

        # test Annotations
        MultiExcludeProtocol().addAnnotationMultiExcludeProtocol(dataId, 'test')
        MultiExcludeProtocol().addAnnotationMultiExcludeProtocol(dataId, 'test test')
        MultiExcludeProtocol().addAnnotationMultiExcludeProtocol(dataId, 'test test test')
        MultiExcludeProtocol().addAnnotationMultiExcludeProtocol(dataId, 'test test test')
        addedAnns = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(dataId)
        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual('test', addedAnns[0]["annotations"][0]["annotation"])
        self.assertEqual('test test', addedAnns[0]["annotations"][1]["annotation"])
        self.assertEqual('test test test', addedAnns[0]["annotations"][2]["annotation"])

        MultiExcludeProtocol().editAnnotationMultiExcludeProtocol(dataId, 'test test', 'updated annotation!!')
        changedAnn = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(dataId)
        self.assertEqual(3, len(addedAnns[0]["annotations"]))
        self.assertEqual('updated annotation!!', changedAnn[0]["annotations"][1]["annotation"])

        MultiExcludeProtocol().deleteAnnotationMultiExcludeProtocol(dataId, 'updated annotation!!')
        deletedChanged = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(dataId)
        self.assertEqual(2, len(deletedChanged[0]["annotations"]))

        MultiExcludeProtocol().deleteAllAnnotationsForMultiExcludeProtocol(dataId)
        deletedAll = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(dataId)
        self.assertRaises(KeyError, lambda: deletedAll[0]["annotations"])

        # add Annotation To MultiExcludeProtocol Timeline
        objectId = MultiExcludeProtocol().addAnnotationToMultiExcludeProtocolTimeline('2016-08-01 10:00:00',
                                                                                      "here's a timeline annotation", "Alex", "Super Summer Event")
        addtimelineAnnotation = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(objectId)
        pprint(addtimelineAnnotation)
        self.assertEqual(addtimelineAnnotation[0]["className"], 'annotation')
        self.assertEqual(addtimelineAnnotation[0]["start"], '2016-08-01 10:00:00')
        self.assertEqual(addtimelineAnnotation[0]["content"], "here's a timeline annotation")
        self.assertEqual(addtimelineAnnotation[0]["metadata"]["techName"], 'Alex')
        self.assertEqual(addtimelineAnnotation[0]["metadata"]["eventName"], 'Super Summer Event')


if __name__ == '__main__':
    unittest.main()

# python -m unittests.test_multiExcludeProtocol
