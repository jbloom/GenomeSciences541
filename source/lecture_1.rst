===============================================
Lecture 1 details
===============================================

* Genome Sciences 541, `Jesse Bloom`_

* These slides are at http://jbloom.github.io/GenomeSciences541/lecture_1.html

* Reading for this lecture is :download:`Zuckerkandl and Pauling (1965) <readings/Zuckerkandl_and_Pauling-1965.pdf>`.
  Read pages 97-114 and 147-152.

Lecture 1: the evolution of protein-coding genes
=================================================

Pauling and Zuckerkandl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* :download:`Zuckerkandl and Pauling (1965) <readings/Zuckerkandl_and_Pauling-1965.pdf>`: one of the first molecular studies of protein evolution

* Structure imposes many constraints

* Very hard to quantitatively understand these constraints

* *Sequence divergence* not equal to *Functional divergence*

* A molecular clock?

Genes evolve at the level of DNA (or RNA for some viruses)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We routinely abstract the complex molecule DNA to strings of letters with little loss of relevant information::

    atg gtg ctc agc gag gga gaa tgg cag ttg gtt ctg cac gtc ...


*It has not escaped our notice that the specific pairing we have postulated immediately suggests a possible copying mechanism for the genetic material.* -- `Watson and Crick (1953)`_

*The translation from nucleic acid to protein proceeds in a sequential fashion according to a systematic code with relatively simple rules.* -- `Nirenberg (1968)`_


But most selection is on the protein
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The properties of proteins are **not** easily abstracted. 

Proteins are linear polymers encoded by DNA::

    atg gtg ctc agc gag gga gaa tgg cag ttg gtt ctg cac gtc ...
    M   V   L   S   E   G   E   W   Q   L   V   L   H   V   ...

Proteins derive their relevant properties from their three-dimensional structures.

Properties of proteins are not easily abstracted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: myoglobin_structure/png_images/myoglobin_static.png
   :width: 61%
   :align: center

   `PyMol analysis of myoglobin`_

   *Perhaps the most remarkable features of the molecule are its complexity and its lack of symmetry. The arrangement seems to be almost totally lacking in the kind of regularities which one instinctively anticipates, and it is more complicated than has been predicated by any theory of protein structure.* -- `Kendrew et al (1958)`_

Context for reading Zuckerkandl and Pauling (1965)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/Zuckerkandl_and_Pauling-1965.png
   :width: 90%
   :align: center

   :download:`Zuckerkandl and Pauling (1965) <readings/Zuckerkandl_and_Pauling-1965.pdf>`


They knew the structure of sperm whale myoglobin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. figure:: myoglobin_structure/png_images/myoglobin_static.png
   :width: 90%
   :align: center

   `PyMol analysis of myoglobin`_

   Structure had been determined by `Kendrew et al (1958)`_

They knew that single mutations could potentially have large biological consequences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    MVHLTPEEKSAVT...
    MVHLTPvEKSAVT...


`"Sickle Cell Anemia, a Molecular Disease" (Pauling et al, 1949)`_

`"A Specific Chemical Difference between Globins of Normal and Sickle-cell Anemia Hemoglobins" (Ingram, 1956)`_


They knew the sequences of a variety of homologous globins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* sperm whale myoglobin

* human myoglobin

* human hemoglobin alpha, beta, gamma, and delta chains

* horse hemoglobin alpha and beta chains

* cattle hemoglobin alpha and beta chains

* cattle fetal hemoglobin chain

* pig hemoglobin alpha and beta chains

* gorilla alpha and beta chains

* carp hemoglobin alpha chain

* lamprey hemoglobin chain

Analysis of myoglobin homologs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We will perform an analysis similar to that of Zuckerkandl and Pauling, and look at some of the conclusions that they draw.

Myoglobin homologs
~~~~~~~~~~~~~~~~~~~

.. include:: myoglobin_homologs/aligned_proteins.fasta
   :literal: 

Sequences at `Analysis of myoglobin homologs`_

Site variability among myoglobin homologs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: myoglobin_homologs/myoglobin_site_preferences_logoplot.jpg
   :width: 91%
   :align: center

   Code /data to produce this figure at `Analysis of myoglobin homologs`_

Very little sequence is strictly conserved
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. figure:: images/invariant_sites.png
   :width: 90%
   :align: center

   :download:`Zuckerkandl and Pauling (1965) <readings/Zuckerkandl_and_Pauling-1965.pdf>`

Relatively few insertions and deletions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*Deletions or additions of one to several amino acid residues are expected to be eliminated by natural selection in a high proportion of cases. Those that are preserved should be mostly found at either end of a chain, at the end of helices, in short helices, or in nonhelical regions, notably in loops that may be shortened or lengthened without  affecting the steric relationships in the rest of the molecule. A deletion or addition in the middle of a long helix would result in so many simultaneous alterations in side-chain interactions that it is highly unlikely that the tertiary structure and the function of the molecule could survive such an event. The deletions or additions found in hemoglobin and myoglobin chains are compatible with these generalities.* 

:download:`Zuckerkandl and Pauling (1965) <readings/Zuckerkandl_and_Pauling-1965.pdf>`

Structure is highly conserved
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. figure:: images/structural_conservation.png
   :width: 90%
   :align: center

   :download:`Zuckerkandl and Pauling (1965) <readings/Zuckerkandl_and_Pauling-1965.pdf>`

This observation has stood the test of time. In fact, sequences with as little as 30-35% identity generally have
very similar structures. See `Chothia and Lesk (1984) <http://www.ncbi.nlm.nih.gov/pmc/articles/PMC1166865/?page=1>`_ and `Sander and Schneider (1991) <http://cbio.mskcc.org/publications/papers/sander/038.pdf>`_.

Structure is highly conserved
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. figure:: myoglobin_structure/png_images/sperm_whale_tuna_myoglobin_overlay_static.png
   :width: 80%
   :align: center

   `PyMol analysis of myoglobin`_

   Structural alignment of sperm whale (gray) and yellowfin tuna (orange) myoglobins. These proteins are only 57% identical.

Different proteins evolve at different rates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. figure:: images/cytochrome_C.png
   :width: 100%
   :align: center

   :download:`Zuckerkandl and Pauling (1965) <readings/Zuckerkandl_and_Pauling-1965.pdf>`

Zuckerkandl and Pauling's view of evolution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. figure:: images/conclusions_1.png
   :width: 100%
   :align: center

   :download:`Zuckerkandl and Pauling (1965) <readings/Zuckerkandl_and_Pauling-1965.pdf>`

One key point (subject of next week)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Many such substitutions may lead to relatively little fuinctional change, whereas at other times the replacement of one single amino acid residue by another may lead to a radical functional change... Of course, the two aspects are not unrelated, since the functional effect of a given single substitution will frequently depend on the presence or absence of a number of other substitutions.*

What do we call that phenomenon?

Zuckerkandl and Pauling propose a molecular clock 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. figure:: images/conclusions_2.png
   :width: 100%
   :align: center

   :download:`Zuckerkandl and Pauling (1965) <readings/Zuckerkandl_and_Pauling-1965.pdf>`

A striking example of the molecular clock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:download:`Figure 6 of dos Reis et al (2009) <readings/dos_Reis_et_al-2009.pdf>`

Important implications
~~~~~~~~~~~~~~~~~~~~~~~~
* The extent of sequence change can be used to reconstruct evolutionary relationships (*molecular phylogenetics*)

* However, the constant background sequence change can make it difficult to pinpoint biologically important changes:

    - *Positive selection* : for instance, take a look at `nextflu <http://nextflu.org>`_

    - *Disease-causing mutations* 

Hand-written notes
~~~~~~~~~~~~~~~~~~~

:download:`notes from the second half of class <readings/lecture_1_notes_new.pdf>`

.. include:: weblinks.txt
