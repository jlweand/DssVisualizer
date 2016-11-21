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
from core.apis.datasource.techAndEventNames import TechAndEventNames
from pprint import pprint

class DistinctEventTechNames(unittest.TestCase):

    def test_getDistinctNames(self):
        eventNames = TechAndEventNames().getDistinctEventNames()
        techNames = TechAndEventNames().getDistinctTechNamesForEvents(eventNames[1:2])
        techAndEventNames = TechAndEventNames().getDistinctTechAndEventNames()
        pprint(eventNames)
        pprint(techNames)
        pprint(techAndEventNames)

        self.assertEquals(3, len(eventNames))
        self.assertEquals('Another Event', eventNames[0])
        self.assertEquals('Super Summer Event', eventNames[1])
        self.assertEquals('Unicorns and more!', eventNames[2])

        self.assertEquals(2, len(techNames))
        self.assertEquals('Alex', techNames[0])
        self.assertEquals('Tom', techNames[1])

        self.assertEquals(5, len(techAndEventNames))
        self.assertEquals('Another Event by Alex', techAndEventNames[0])
        self.assertEquals('Another Event by Julie', techAndEventNames[1])
        self.assertEquals('Super Summer Event by Alex', techAndEventNames[2])
        self.assertEquals('Super Summer Event by Tom', techAndEventNames[3])
        self.assertEquals('Unicorns and more! by Willow', techAndEventNames[4])

if __name__ == '__main__':
    unittest.main()

# python -m unittests.test_distinctNames
