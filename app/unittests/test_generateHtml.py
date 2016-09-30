import unittest
from core.apis.renderer.generateHtml import GenerateHtml
from pprint import pprint

class GenerateHtmlTest(unittest.TestCase):

    def test_selectKeyPressData(self):
        stuff = GenerateHtml().generatHtml()
        pprint(stuff)
        # self.assertIsNotNone(jsonData)

if __name__ == '__main__':
    unittest.main()

#python -m unittests.test_generateHtml
