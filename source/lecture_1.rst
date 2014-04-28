===============================================
Lecture 1 
===============================================

* Genome Sciences 541, `Jesse Bloom`_

* These slides are at http://jbloom.github.io/GenomeSciences541/lecture_1.html

* Reading for this lecture is :download:`Zuckerkandl and Pauling (1965) <readings/Zuckerkandl_and_Pauling-1965.pdf>`.
  Read pages 97-114 and 147-152 carefully,
  skim pages 115-146,
  feel free to skip pages 153-end.

* The homework for this lecture is at ???.

Lecture 1: the evolution of protein-coding genes
==================================================
* :download:`Zuckerkandl and Pauling (1965) <readings/Zuckerkandl_and_Pauling-1965.pdf>`: one of the first molecular studies of protein evolution

* Structure imposes many constraints

* Very hard to quantitatively understand these constraints

* Sequence divergence :math:`\ne` Functional divergence

* A molecular clock?

Genes evolve at the level of DNA (or sometimes RNA)
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

But proteins derive their relevant properties from their three-dimensional structures.

Properties of proteins are not easily abstracted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: myoglobin_structure/png_images/myoglobin_static.png
   :width: 61%
   :align: center

   `PyMol analysis of sperm whale myoglobin`_

   *Perhaps the most remarkable features of the molecule are its complexity and its lack of symmetry. The arrangement seems to be almost totally lacking in the kind of regularities which one instinctively anticipates, and it is more complicated than has been predicated by any theory of protein structure.* -- `Kendrew et al (1958)`_

Context for reading Zuckerkandl and Pauling (1965)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/Zuckerkandl_and_Pauling-1965.png
   :width: 90%
   :align: center

   :download:`Zuckerkandl and Pauling (1965) <readings/Zuckerkandl_and_Pauling-1965.pdf>`


They knew the structure of sperm whale myoglobin
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. figure:: myoglobin_structure/png_images/myoglobin_static.png
   :width: 90%
   :align: center

   `PyMol analysis of sperm whale myoglobin`_

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

* human hemoglobin :math:`\alpha`, :math:`\beta`, :math:`\gamma`, and :math:`\delta` chains

* horse hemoglobin :math:`\alpha` and :math:`\beta` chains

* cattle hemoglobin :math:`\alpha` and :math:`\beta` chains

* cattle fetal hemoglobin chain

* pig hemoglobin :math:`\alpha` and :math:`\beta` chains

* gorilla :math:`\alpha` and :math:`\beta` chains

* carp hemoglobin :math:`\alpha` chain

* lamprey hemoglobin chain

Analysis of myoglobin homologs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We will perform an analysis similar to that of Zuckerkandl and Pauling, and look at some of the conclusions that they draw.

Myoglobin homologs
~~~~~~~~~~~~~~~~~~~

.. include:: myoglobin_homologs/aligned_proteins.fasta
   :literal: 

Sequences at `Analysis of myoglobin homologs`_

The evolution studied in molecular phylogenetics is due to both mutation and selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    atg gtg ctc agc gag gga gaa tgg cag ttg gtt ctg cTc gtc ...
    atg gtg ctc agc gag gga gaa tgA cag ttg gtt ctg cac gtc ...
    atg gtg ctc agc Cag gga gaa tgg cag ttg gtt ctg cac gtc ...

::

    atg gtg Atc agc gag gga gaa tgg cag ttg gtt ctg cac gtc ...
    atg gtg ctc agc Cag gga gaa tgg cTg ttg gtt ctg cac gtc ...
    atg gtg ctc agc Cag gga gaa tgg cag ttg gtA ctg cac gtc ...

::

    atg gtA ctc agc Cag gga gaa tgg cag ttg gtt ctg cac gtc ...
    atg gtg ctc agc Cag gga gaa tgg cTg ttg gtt ctg Aac gtc ...
    atg gtg ctc agc Cag gga gaa tgg cTg ttg gtA ctg cac gtc ...

::

    atg atg cAc agc Cag gga gaa tgg cTg ttg gtt ctg cac gtc ...
    atg gtg ctc agc Cag gga gaa tgg cTg ttg gtt ctg Aac gtc ...
    atg gtg ctc agc Cag gga gaa tgg cTg ttg gtA ctg cac gtc ...

More
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In these lectures (and in most molecular phylogenetics), we consider only point substitutions::
:download:`Zuckerkandl and Pauling (1965) <readings/Zuckerkandl_and_Pauling-1965.pdf>`  (pages 111-112) suggest:

    *Deletions or additions of one to several amino acid residues are expected to be eliminated by natural selection in a high proportion of cases. Those that are preserved should be mostly found at either end of a chain, at the end of helices, in short helices, or in nonhelical regions, notably in loops that may be shortened or lengthened without  affecting the steric relationships in the rest of the molecule, A deletion or additionin the middle of a long helix would result in so many simultaneous alterations in side-chain interactions that it is highly unlikely that the tertiary structure and the function of the molecule could survive such an event. The deletions or additions found in hemoglobin and myoglobin chains are compatible with these generalities.*



.. include:: weblinks.txt
