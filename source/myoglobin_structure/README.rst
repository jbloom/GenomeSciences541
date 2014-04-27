===========================================
Structure and evolution of myoglobin
===========================================

This is an analysis by `Jesse Bloom`_ of the structure and evolution of myoglobin. It is based around the structure of sperm whale myoglobin, which was the first protein ever to have its crystal structure solved, in work by `Kendrew et al (1958)`_.


Programs used
--------------
* `Python`_: tested with version 2.7.3

* `PyMol`_

Input files
------------------------------------------

* ``1MBN.pdb`` is PDB file `1MBN` containing the crystal structure of sperm whale myoglobin.

* ``analyze_protein.py`` is a `Python`_ script to be run in `PyMol`_ to label the protein structure and generate images. Run by opening `PyMol`_ and then in `PyMol`_, typing::

    run analyze_protein.py


.. _`Jesse Bloom`: http://research.fhcrc.org/bloom/en.html
.. _`Watson and Crick (1953)`: http://www.nature.com/nature/dna50/watsoncrick.pdf
.. _`Nirenberg (1968)`: http://www.nobelprize.org/nobel_prizes/medicine/laureates/1968/nirenberg-lecture.pdf
.. _`Kendrew et al (1958)`: http://www.chem.uwec.edu/Chem452_Media/pages/readings/media/Kendrew_et_al_1958.pdf
.. _`1MBN`: http://www.pdb.org/pdb/explore/explore.do?structureId=1MBN
.. _`Python`: https://www.python.org/
.. _`PyMol`: http://www.pymol.org/
