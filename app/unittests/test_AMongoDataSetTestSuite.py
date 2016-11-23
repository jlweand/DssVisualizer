import unittest
from unittests.test_setupMongoDatasource import SetupMongoDatasource
from unittests.test_manualScreenShot import ManualScreenShotTest
from unittests.test_multiExcludeProtocol import MultiExcludeProtocolTest
from unittests.test_multiExcludeThroughput import MultiExcludeThroughputTest
from unittests.test_multiIncludeProtocol import MultiIncludeProtocolTest
from unittests.test_multiIncludeThroughput import MultiIncludeThroughputTest
from unittests.test_pyClick import PyClick
from unittests.test_pyKeyPress import PyKeyPress
from unittests.test_pyTimed import PyTimed
from unittests.test_tsharkProtocol import TsharkProtocolTest
from unittests.test_tsharkThroughput import TsharkThroughputTest
from unittests.test_distinctEventTechNames import DistinctEventTechNames

if __name__ == '__main__':
    test_classes_to_run = [ManualScreenShotTest,
                           MultiExcludeProtocolTest, MultiExcludeThroughputTest,
                           MultiIncludeProtocolTest, MultiIncludeThroughputTest,
                           PyClick, PyKeyPress, PyTimed,
                           TsharkProtocolTest, TsharkThroughputTest,
                           DistinctEventTechNames]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)
