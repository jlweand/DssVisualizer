import unittest
from core.config.configRenderers import ConfigRenderers

class ConfigRenderersTest(unittest.TestCase):

    def test_addRenderer(self):
        output = ConfigRenderers().addRenderer("newName", "here's the location")
        self.assertEqual(output, "newName")

        # test adding duplicate renderer
        output = ConfigRenderers().addRenderer("newName", "here's the location")
        self.assertEqual(output, "Duplicate renderer name. Unable to add this renderer plugin.")

    def test_getListOfRenderers(self):
        output = ConfigRenderers().getListOfRenderers()
        self.assertEqual(len(output), 3)

    def test_removeRenderer(self):
        #test removing nonexistant renderer
        output = ConfigRenderers().removeRenderer("dummyName")
        self.assertEqual(output, "Failed to find renderer plugin named dummyName")

        #test removing default renderer
        output = ConfigRenderers().removeRenderer("vis.js")
        self.assertEqual(output, "Sorry, this plugin cannot be deleted. It is currently in use. Please choose another default plugin before deleting this one.")

        #test removing renderer
        output = ConfigRenderers().removeRenderer("newName")
        self.assertEqual(output, "newName")

    def test_setDefaultRenderer(self):
        output = ConfigRenderers().setDefaultRenderer("d3.js")
        self.assertEqual(output, "d3.js")

        # test setting nonexistant default renderer
        output = ConfigRenderers().setDefaultRenderer("dummyName")
        self.assertEqual(output, "No renderer plugin has been imported for dummyName")

        # set it back to vis.js
        output = ConfigRenderers().setDefaultRenderer("vis.js")
        self.assertEqual(output, "vis.js")

if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_configRenderers
