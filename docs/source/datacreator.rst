.. highlight:: rst

Java Data Creator
=================

* I make no claims of goodness on this code.  It was thrown together in a fit of frustration from using the Linux VM on my crappy laptop. Do not judge me based on this code.

* Needs Java 8 for the dates

* Main method can be found in CreateData.java

* It will generate a 'datapoint' every n units of time within a two week period starting two weeks from the current date/time.  The n units are determined by::

    twoWeeksAgo = twoWeeksAgo.plus(45, ChronoUnit.MINUTES);
