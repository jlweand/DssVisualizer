.. highlight:: java

Java JSON Data Creator
======================

* Jennifer makes no claims of goodness on this code.  It was thrown together in a fit of frustration from using the Linux VM on her crappy laptop. Do not judge her based on this code.

* Can be found in /DssVisualizer/datacreater/

* Needs Java 8

* Main method can be found in CreateData.java

* It will generate a 'datapoint' every n units of time within a two week period starting two weeks from the current date/time.  The n units are determined by::

    twoWeeksAgo = twoWeeksAgo.plus(45, ChronoUnit.MINUTES);

* Only generates JSON files for Keypresses, Click, Timed, and Manual Snapshots.
