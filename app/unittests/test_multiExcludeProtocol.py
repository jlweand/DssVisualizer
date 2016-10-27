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
    def test_monolithicTestCase(self):
        # select by date
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolData('2016-10-15 11:59:27', '2016-10-15 11:59:27',
                                                                         "", "")
        pprint(jsonData)
        dataId = jsonData[0]["id"]
        self.assertEqual(1, len(jsonData))

        # select by Id
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(dataId)
        self.assertEqual(1, len(jsonData))

        # select by Tech name
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolData('2016-10-15 11:59:27', '2016-10-15 11:59:27',
                                                                         "Alex", "")
        self.assertEqual(1, len(jsonData))

        # select by event name
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolData('2016-10-15 11:59:27', '2016-10-15 11:59:27',
                                                                         "", "Super Summer Event")
        self.assertEqual(1, len(jsonData))

        # select by tech name AND event name
        jsonData = MultiExcludeProtocol().selectMultiExcludeProtocolData('2016-10-15 11:59:27', '2016-10-15 11:59:27',
                                                                         "Alex", "Super Summer Event")
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
        modifiedCount = MultiExcludeProtocol().insertFixedMultiExcludeProtocolData(dataId, '55555', '1 p/s', 'traffic',
                                                                                   'eth:ethertype:arp\neth:ethertype:ip:udp:dns\n',
                                                                                   '2016-12-02 18:28:00')
        self.assertEqual(1, modifiedCount)

        # update Fixed MultiExcludeProtocol Data
        modifiedCount = MultiExcludeProtocol().updateFixedMultiExcludeProtocolData(dataId, '7777', '2 p/s', 'traffic',
                                                                                   'eth:ethertype:arp\neth:ethertype:ip:udp:dns\n',
                                                                                   '2016-10-02 18:28:00')
        self.assertEqual(1, modifiedCount)

        # delete Fixed MultiExcludeProtocol Data
        modifiedCount = MultiExcludeProtocol().deleteFixedMultiExcludeProtocolData(dataId)
        self.assertEqual(1, modifiedCount)

        # add Annotation To MultiExcludeProtocol Timeline
        objectId = MultiExcludeProtocol().addAnnotationToMultiExcludeProtocolTimeline('2016-08-01 10:00:00',
                                                                                      "here's a timeline annotation")
        addtimelineAnnotation = MultiExcludeProtocol().selectMultiExcludeProtocolDataById(objectId)
        # pprint(addtimelineAnnotation)
        self.assertIsNotNone(addtimelineAnnotation)


if __name__ == '__main__':
    unittest.main()

# python -m unittests.test_multiExcludeProtocol
