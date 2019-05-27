=====================================
2nd Homework from Jesse Bloom
=====================================

This is the second homework from Jesse Bloom for Genome Sciences 541. 

It is due on May 25, 2017. Submit it via the DropBox link.

For this homework, you should choose a gene of interest to yourself and perform a phylogenetic analysis using `RAxML`_ like we did for the first homework and in lecture 2.

You should then use the *FEL* method to search for sites under purifying and positive selection using `DataMonkey`_ like we did in lecture 4.

Please do the following steps, and submit your code along with a single file containing the results as a ``.zip`` or ``.tgz`` file:

    1) Choose a gene to analyze. This can be any protein-coding gene of interest to you. But it must be a gene with at least a few homologs within 50% sequence identity. Answer this question: **What gene did you choose?**

    2) Build a **codon** alignment of your gene and at least 5 other homologs. You can include many more sequences if you want, but as you add more the programs will get slower (although this shouldn't be a problem unless you have more than 100). 
    
       If you are working on a gene that you already study, you may already have an alignment. If you don't have a gene or alignment in mind, pick one and find homologs. There are lots of ways to get homologs:
    
        - One easy way is to go to `HomoloGene <http://www.ncbi.nlm.nih.gov/homologene>`_, which will automatically search for homologs. Once you do the search, you will get a list of homologs and **protein** alignments, but you will have to manually click through to get the **coding** alignments.

        - Another easy thing is to go to the `Influenza Virus Resource <http://www.ncbi.nlm.nih.gov/genomes/FLU/Database/nph-select.cgi?go=database>`_ and download some sequences from the same *Protein* making sure that you take the *Protein Coding Region*.

       Whatever you choose, build a **codon** alignment (e.g. nucleotide alignment from the protein alignment). Then answer the following: **How many sequences did you choose? What is the average pairwise identity?**.

    3) Use `RAxML`_ to infer a maximum likelihood phylogenetic tree using the *GTRCAT* model like we did in lecture 2 and homework 1. Then visualize this tree using `FigTree <http://tree.bio.ed.ac.uk/software/figtree/>`_ or one of the many other tree visualizing programs you can find via Google. The do the following: **Include an image of your tree, and comment on whether it looks as you expected.**

    4) Use `DataMonkey`_ to test for positive selection using the *FEL* method. Answer the following: **Where there any sites under positive selection? Where there any sites under purifying selection? Are these results what you expected? Include the full *FEL* report too.**

.. _`RAxML`: http://sco.h-its.org/exelixis/web/software/raxml/index.html
.. _`DataMonkey`: http://www.datamonkey.org/
