
Incomplete Items
================

1. Show image on hover
    For some reason adding the 'itemover' event does not work on the timelines.  We were never able to figure out why.
    I think if you add a 'onhover' event to the timeline you can catch it that way.

2. Image location on import
    When importing to the data source you can indicate if you want to copy the images to the file structure of the application.
    The current functionality will look at the image path in the JSON, find that image, and copy it to the images folder in the application.
    When exporting you also have the option to copy the images into the output directory.  No changes are made to the JSON on where the exported images are.
    The problem arises when you take that exported data, copy it to a different file structure than where the images lived on the first computer.
    If you try to import that data AND choose to copy the images, the Python will not be able to find the images since the path in the JSON is no longer valid.

    So, we wanted to add an option to specify the directory where the images actually are on import.  If the location is not specified, the Python will look
    for them in the path in the JSON.  If the path is specified, it will look for the image name in that directory and copy it.

    The issues to work out:

        * What if two images have the same name? I have no idea what the possibility of that happening is, but I assume it is.
        * Do you specify one location and hard code the folder names where they should be found within that location?
        * other things?

3. Distinct Event / Tech for ElasticSearch
    This is also talked about in the `Limitations/Issues/Weirdness <limitations.html>`_ page.
    When researching on how to get the distinct event/tech names I tried `aggregation <https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations-bucket-terms-aggregation.html>`_ and then ran into `fielddata is disabled on text fields by default <https://www.elastic.co/guide/en/elasticsearch/reference/current/fielddata.html>`_
    I was not comfortable enough with ElasticSearch to determine if turning on fielddata for the text field was really a good idea.
    Another idea is to add a unique tech/event number on import.  Aggregation works fine on non text fields.

4. More plug and playable
    For the data source I wrote up some ideas in the `Datasource API Documentation <datasourceapi.html#simplify-things>`_
    
    For the front end... I have no idea what would need to be done to make this more plug and playable.  Anyone else have any ideas?

5. Windows Install package
    We just didn't get to this.  Our expertise on such things was not up to snuff either.
