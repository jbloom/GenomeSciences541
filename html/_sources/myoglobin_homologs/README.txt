===========================================
Myoglobin homologs
===========================================

This is an analysis by `Jesse Bloom`_ of a set of myoglobin homologs.


Programs used
--------------
* `Python`_: tested with version 2.7.3

* `BioPython`_: tested with version 1.6.3

* `probcons`_: for alignments, tested with version 1.12

* `phyloExpCM`_: for calculating natural frequencies from alignments. Note that `phyloExpCM`_ also has some requirements for external programs as described in its documentation.

* `mapmuts`_: for calculating natural frequencies from alignments. Note that `mapmuts`_ also has some requirements for external programs as described in its documentation.

* `ImageMagick convert`_: for making JPGs from PDFs.

Input files
------------------------------------------

* ``./genes/`` is a subdirectory that contains the coding DNA sequences of a variety of myoglobin homologs.

* ``1MBN_renumbered.pdb`` is PDB file `1MBN`_ of sperm whale myoglobin renumbered to begin with 1 at the N-terminal methionine and proceed sequentially from there. The original `1MBN`_ begins with 1 at the second valine, hence the need for renumbering.

* ``1MBN_renumbered.pdb`` gives the results of analyzing ``1MBN_renumbered.pdb`` with the `DSSP webserver`_ to calculate secondary structure and solvent accessibility.

* ``compare_homologs.py`` is the master `Python`_ script that runs the analysis in this directory.

Running the analysis
---------------------
To run the analysis, simply type the following at the command line::

    python compare_homologs.py

If you have installed the `Programs used`_, this will generate all of the remaining output.


.. _`Jesse Bloom`: http://research.fhcrc.org/bloom/en.html
.. _`Python`: https://www.python.org/
.. _`BioPython`: http://biopython.org/wiki/Main_Page
.. _`probcons`: http://probcons.stanford.edu/
.. _`1MBN`: http://www.pdb.org/pdb/explore/explore.do?structureId=1MBN
.. _`DSSP webserver`: http://www.cmbi.ru.nl/hsspsoap/
.. _`mapmuts`: https://github.com/jbloom/mapmuts
.. _`phyloExpCM`: https://github.com/jbloom/phyloExpCM
.. _`ImageMagick convert`: http://www.imagemagick.org/script/convert.php
