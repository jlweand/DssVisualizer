.. highlight:: rst

ElasticSearch Installation
==========================

Installing Elastic Search (for Windows. Mac OS and Linux may vary)
------------------------------------------------------------------
1.	Download the version of Elastic Search you need `here <https://www.elastic.co/downloads/elasticsearch>`_.

2.	Change the install path to C:\elasticsearch. Accept all other defaults.

3.	Start Elastic Search up:  You must use a command window with Administrative rights. And this must be done before you try to use our app::

    C:\elasticsearch-5.0.0\bin>elasticsearch

You’ll get a lot of text scrolling.  It will show the number of indices.  You should see the test index online.

4. Test that ElasticSearch is running by opening its `url <http://localhost:9200>`_.

5. You can check the installation documentation `here <https://www.elastic.co/guide/en/elasticsearch/reference/5.0/install-elasticsearch.html>`_
