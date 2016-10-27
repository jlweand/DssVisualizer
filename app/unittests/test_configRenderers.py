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
from core.config.configRenderers import ConfigRenderers


class ConfigRenderersTest(unittest.TestCase):
    def test_addRenderer(self):
        output1 = ConfigRenderers().addRenderer("newName", "here's the location")

        # test adding duplicate renderer
        output2 = ConfigRenderers().addRenderer("newName", "here's the location")

        self.assertEqual(output1, "newName")
        self.assertEqual(output2, "Duplicate renderer name. Unable to add this renderer plugin.")

    def test_removeRenderer(self):
        # test removing nonexistant renderer
        output1 = ConfigRenderers().removeRenderer("dummyName")

        # test removing default renderer
        output2 = ConfigRenderers().removeRenderer("vis.js")

        # test removing renderer
        output3 = ConfigRenderers().removeRenderer("newName")

        self.assertEqual(output1, "Failed to find renderer plugin named dummyName")
        self.assertEqual(output2,
                         "Sorry, this plugin cannot be deleted. It is currently in use. Please choose another default plugin before deleting this one.")
        self.assertEqual(output3, "newName")

    def test_setDefaultRenderer(self):
        output1 = ConfigRenderers().setDefaultRenderer("pyKeyLogger", "d3.js", "something.txt")

        # test setting nonexistant default renderer
        output2 = ConfigRenderers().setDefaultRenderer("pyKeyLogger", "dummyName", "dummyName")

        # set it back to vis.js
        output3 = ConfigRenderers().setDefaultRenderer("pyKeyLogger", "vis.js", "scripts.txt")

        self.assertEqual(output1, "d3.js")
        self.assertEqual(output2, "No renderer plugin has been imported for dummyName")
        self.assertEqual(output3, "vis.js")


if __name__ == '__main__':
    unittest.main()

# python -m unittests.test_configRenderers
