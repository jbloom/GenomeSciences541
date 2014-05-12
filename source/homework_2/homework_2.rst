============================
Homework 2
============================
Homework 2 for Genome Sciences 541, assigned by `Jesse Bloom`_.

This homework is due on May 13, 2014.

What you need 
---------------------
* You first need to have completed `homework 1`_.

* You need a program that can be used to compute matrix exponentials. One such program is ``scipy``, see for example http://docs.scipy.org/doc/scipy-0.13.0/reference/generated/scipy.linalg.expm.html

Question 1
-----------
Compute the maximum likelihood Jukes-Cantor distance from the starting sequence as a function of the number of simulation steps for your simulations in `homework 1`_. 
Do this for the full sequences and the first, second, and third codon positions separately.
Recall that the estimate of the Jukes-Cantor distance is :math:`t = \frac{3}{4\mu} \ln\left(\frac{3}{4 p - 1}\right)` where :math:`p` is the pairwise sequence identity. We will use units of time such that :math:`\mu = 1`.
If the Jukes-Cantor estimate is accurate, then the estimated distance should scale linearly with the number of simulation steps. Does this happen? Why or why not?

Question 2 (background)
------------------------
The Kimura 2-paramer model adds a single parameter :math:`\kappa` to the Jukes Cantor model. The transition matrix :math:`\mathbf{P}` for this model is as follows, where nucleotides are indexed in alphabetical order (A, C, G, T) and matrix entry :math:`P_{ij}` is the rate going from :math:`i` to :math:`j`. Note that :math:`\mu` has been defined such that most of the matrix elements are one.

.. math::

   \mathbf{P} = \left[\begin{array}{cccc}
                -\left(2 + \kappa\right) & 1 & \kappa & 1 \\ 
                1 & -\left(2 + \kappa\right) & 1 & \kappa \\ 
                \kappa & 1 & -\left(2 + \kappa\right) & 1 \\ 
                1 & \kappa & 1 & -\left(2 + \kappa\right) \\ 
                \end{array} \right]

Question 2 (more background) 
------------------------------- 
With the definition on the previous slide, let :math:`\mathbf{p_0}` be the initial probability distribution. The probability distribution after time :math:`t` is then :math:`\mathbf{p}\left(t\right) = \mathbf{p_0} \exp\left(t \mathbf{P}\right)` where we are using units of time so that :math:`\mu = 1`.

So to get the probability that a site changes from A to C in time :math:`t`, set :math:`\mathbf{p_0} = \left(1, 0, 0, 0\right)` and then compute element 2 of :math:`\mathbf{p}\left(t\right)`. The probability the site changes from A to C is likewise element 3 of :math:`\mathbf{p}\left(t\right)`, etc.

Question 2
----------
Using a value of :math:`\kappa = 4` (the one from your simulation), compute the maximum likelihood distance from your initial sequence to the sequence after 100 evolutionary steps. You no longer have an analytical formula for :math:`t` (one is possible but we haven't solved for it), so you can just test values of :math:`t` taking very small steps to find the maximum value. How does the maximum likelihood with the Kimura 2-parameter model compare to the maximum likelihood for the same pair of sequences using the Jukes-Cantor model? Note that you do **not** need to compare the estimated value of :math:`t` -- rather, the comparison is between the maximum likelihood value itself for the two models (i.e. which fits better).

.. _`Jesse Bloom`: http://research.fhcrc.org/bloom/en.html
.. _`homework 1`: https://github.com/jbloom/GenomeSciences541/tree/gh-pages/source/homework_1
.. _`1MBN`: http://www.pdb.org/pdb/explore/explore.do?structureId=1MBN
.. _`FoldX`: http://foldx.crg.es/
