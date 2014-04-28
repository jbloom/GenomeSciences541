============================
Homework 1
============================
Homework 1 for Genome Sciences 541, assigned by `Jesse Bloom`_.

This homework is due on April 5, 2014.

.. contents::
   :level: 2

Files and programs
---------------------
You will need the following files and programs:

    * The protein-coding DNA sequence for sperm whale myoglobin at ``sperm-whale_myoglobin.fasta`` at `homework 1`_.

    * The crystal structure of sperm whale myoglobin at ``1MBN_renumbered.pdb`` at `homework 1`_. This is PDB file `1MBN`_ that has been renumbered so that it matches the numbering that you would get if you sequentially numbered the protein encoded by ``sperm-whale_myoglobin.fasta`` starting with 1 at the N-terminal methionine. Note that the N-terminal methionine is missing from the structure.

    * You will need to download `FoldX`_ (you have to create an account to do this). Download the ``30b6`` version.

Assignment
------------
You will simulate the evolution of myoglobin, starting from the sperm whale myoglobin sequence. 

The evolution occurs with a transition-transversion ratio of :math:`\kappa = 4.0`. All synonymous mutations are neutral. Mutations to stop codons or that eliminate the N-terminal methionine are lethal. Other mutations are neutral if the stability of the mutated protein continues to exceed that of the initial starting sperm whale myoglobin, or deleterious otherwise.

The basic process is as follows:

    1) Start by repairing the structure of the myoglobin protein in ``1MBN_renumbered.pdb`` with `FoldX`_ using the *RepairPDB* command. This will create a new repaired PDB file that you will use for all subsequent analyses. This protein structure is then optimize for FoldX. To do this, you can create a runfile with the following contents::

        <TITLE>FOLDX_runscript;
        <JOBSTART>#;
        <PDBS>1MBN_renumbered.pdb;
        <BATCH>#;
        <COMMANDS>FOLDX_commandfile;
        <RepairPDB>1MBN_repaired;
        <END>#;
        <OPTIONS>FOLDX_optionfile;
        <END>#;
        <JOBEND>#;
        <ENDFILE>#;

      Then run `FoldX`_ with a command like::

        ./foldx64MacOs -runfile repair_runfile.txt

      This will create the repaired PDB file ``1MBN_repaired.pdb`` for all subsequent steps.

      Initialize the "extra stability" of this protein as :math:`\Delta G_f = 0`

    2) Randomly choose a site in the nucleotide sequence for the myoglobin. Mutate this sequence with :math:`\kappa = 4.0`. Then do the following:

       - If the mutation is synonymous, accept it.

       - If the mutation is to a stop codon or eliminate the N-terminal methionine, reject it.

       - Otherwise use `FoldX`_ to compute the change in stability (:math:`\Delta \Delta G`) caused by the mutations. More negative free energies of folding imply greater stability, so stabilizing mutations have :math:`\Delta \Delta G < 0`. You can compute the stability by creating the following input file::

            <TITLE>FOLDX_runscript;
            <JOBSTART>#;
            <PDBS>1MBN_repaired.pdb;
            <BATCH>#;
            <COMMANDS>FOLDX_commandfile;
            <BuildModel>mutant1,individual_list.txt;
            <END>#;
            <OPTIONS>FOLDX_optionfile;
            <END>#;
            <JOBEND>#;
            <ENDFILE>#;

         In this file, ``1MBN_repaired.pdb`` is the sequence of the starting myoglobin. The file ``individual_list.txt`` is the file that contains the mutation. For instance, if we are mutating leucine 3 to alanine, then it has contents::

            L3A;

         Run `FoldX`_ using::
        
            ./foldx64MacOs -runfile mutate_runfile.txt

         An output file called ``Average_mutant1`` will be created. The last line of this file contains the :math:`\Delta \Delta G` of the mutation as the third entry::

            1MBN_repaired_1 0   1.82741 0.0879676   0.823098    1.73246 0.382185    -1.26706    3.13049 -0.119406   -1.93645    -0.0983107  0   0   0   -0.885727   -0.603938   -0.0218432  0   0   0   0   -4.44089e-16    0

         So here, :math:`\Delta \Delta G = 1.82741`. This is the effect of making the mutation L3A to the protein in ``1MBN_repaired.pdb``. Now compute the stability of the new protein as :math:`\Delta G_{\rm{new}} = \Delta G_f + \Delta \Delta G`. If `\Delta G_{\rm{new}} > 0`, then the mutant protein is unstable, and so the mutation is eliminated by selection. In that case, retain the unmutated sequence. Otherwise, the mutant protein is viable, and the mutation fixes. In this case, update the stability to the new value of :math:`\Delta G_{\rm{new}` and take the new mutant structure in ``1MBN_repaired_1.pdb`` to be the new parent protein (this structure should have *L3A*).

         So by this process, stabilizing mutations will always fix, and destabilizing mutations will sometimes fix (if the parent already has enough stability).

    3) Repeat this process until the protein sequences have diverged to 60% identity from the initial sperm whale myoglobin protein sequence. Keep track of the number of steps, the number of fixed synonymous mutations, the number of fixed nonsynonymous mutations, the number of rejected nonsynonymous mutations, and the number of fixed transitions versus transversions. Also keep track of the coding nucleotide sequences at each step.


Questions
-------------
1) Turn in the script that you use to perform the analysis.

2) How many steps did it take to reach 60% protein sequence divergence from the initial perm whale myoglobin sequence? Make a plot of protein sequence divergence versus number of steps.

3) Make a plot of the stability of the protein as a function of the number of steps. This stability should generally be slightly less than zero.

4) What was the fraction of all nonsynonymous mutations that fixed? This fraction of nonsynonymous mutations is often referred to as the ratio :math:`\omega`.

5) Make a plot of the sequence divergence at the first, second, and third codon positions versus the number of steps. Does the sequence diverge faster at some codon positions than others? Why?

6) If all mutations fixed, how would you expect the ratio of transitions to compare to that of transversions? Keep in mind that :math:`\kappa = 4.0`, but that there are more transversions than transitions. What was the actual ration of transitions to transversions? Is this higher or lower than the expectation? If it seems substantially different, do you have any ideas why?



.. _`Jesse Bloom`: http://research.fhcrc.org/bloom/en.html
.. _`homework 1`: https://github.com/jbloom/GenomeSciences541/tree/gh-pages/source/homework_1
.. _`1MBN`: http://www.pdb.org/pdb/explore/explore.do?structureId=1MBN
.. _`FoldX`: http://foldx.crg.es/
