
Unit Tests
==========

There are a number of test cases that were used to ensure that the data sources were
working as expected.  At the beginning of the semester we came up with a list of
functionality that we thought the UI would need.  It ended up that the data sources
have more functionality than is needed.  We have left it in there in case there is a
reason you may need it in the future.

Each data type has its own test case, so 10 of the test cases have the exact same tests.
There is a method that tests all the different ways to search. A method to test adding and
editing the fixedData. And a method that tests the annotations, including the timeline annotation.

1. test_manualScreenShot.py
2. test_multiExcludePrototcol.py
3. test_multiExcludeThroughput.py
4. test_multiIncludePrototcol.py
5. test_multiIncludeThroughput.py
6. test_pyClick.py
7. test_pyKeyPress.py
8. test_pyTimed.py
9. test_tsharkProtocol.py
10. test_tsharkThroughput.py

In order for these test cases to pass, the correct data must be imported into the database. There are
two ways to do this; run the correct 'setup' test case, or run the correct test suite.  These test cases
use the JSON found in /DssVisualizer/app/json/unittestDatasets/

**WARNING: Running either the setup test case or test suite will DELETE EVERYTHING in your data source.**

There are two 'setup' test cases.  One is for MongoDB and the other is for ElasticSearch.

1. test_setupMongoDatasource.py
2. test_setupElasticSearchDatasource.py

There are two test suites that will run the correct setup test case as well as the 10 different datatype test cases above.

1. test_AMongoDataSetTestSuite.py
2. test_AnElasticSearchDataSetTestSuite.py

**WARNING: Running either the setup test case or test suite will DELETE EVERYTHING in your data source.**

The test_AMongoDataSetTestSuite.py also runs a test case that verifies that the event/tech names are being selected correctly.
Remember that the ElasticSearch does not have this functionality.  This test case is named test_distinctEventTechNames.py

Here is a list of the rest of the miscellaneous test cases:

1. test_configDatasources.py - This tests the adding, removing, setting of the data source plugins from the config.json file.
2. test_configRenderers.py - This tests the adding, removing, setting of the renderer plugins from the config.json file.
3. test_dataexport.py - tests the data export functionality.
4. test_dataimport.py - tests the data import functionality.
5. test_generateHtml.py - tests the generating the index.html from index.html.template and the needed install plugin scripts.
