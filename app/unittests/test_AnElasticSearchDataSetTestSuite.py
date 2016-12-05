import unittest
from unittests.test_setupElasticSearchDatasource import SetupElasticSearchDatasource
from unittests.test_manualScreenShot import ManualScreenShotTest
from unittests.test_multiExcludeProtocol import MultiExcludeProtocolTest
from unittests.test_multiExcludeThroughput import MultiExcludeThroughputTest
from unittests.test_multiIncludeProtocol import MultiIncludeProtocolTest
from unittests.test_multiIncludeThroughput import MultiIncludeThroughputTest
from unittests.test_pyClick import PyClickTest
from unittests.test_pyKeyPress import PyKeyPressTest
from unittests.test_pyTimed import PyTimedTest
from unittests.test_tsharkProtocol import TsharkProtocolTest
from unittests.test_tsharkThroughput import TsharkThroughputTest

if __name__ == '__main__':
    test_classes_to_run = [SetupElasticSearchDatasource,
                           ManualScreenShotTest,
                           MultiExcludeProtocolTest, MultiExcludeThroughputTest,
                           MultiIncludeProtocolTest, MultiIncludeThroughputTest,
                           PyClickTest, PyKeyPressTest, PyTimedTest,
                           TsharkProtocolTest, TsharkThroughputTest]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)
