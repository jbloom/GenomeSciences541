=============================================
Jesse Bloom's Genome Sciences 541 materials
=============================================

``README`` for the `GenomeSciences541 GitHub`_ repository.

This repository was created by `Jesse Bloom`_.

This repository contains materials for `Jesse Bloom`_'s lectures in the University of Washington's Genome Sciences 541 class

Making the slides
---------------------

These slides are written in `reStructuredText`_ and compiled with `hieroglyph`_ (a `Python`_ package).

To compile the slides, you need to first install `hieroglyph`_ on your computer::

    easy_install hieroglyphy

and then make the slides with::

    make slides

The slides are in the home directory, while the source is in the ``./source/`` subdirectory.

When this repository is pushed to the ``gh_pages`` branch of the `GenomeSciences541 GitHub`_ repository, the slides will become available on ``GitHub Pages``. 

For example, a file named ``./source/lecture_1.rst`` will compile to ``lecture_1.html`` with the ``make slides`` command, and after the pushing to the `GenomeSciences 541 GitHub`_ repository, the slides will be available for viewing at http://jbloom.github.io/GenomeSciences541/lecture_1.html.

Advance through the slides with the arrow keys or space bar.

.. _`hieroglyph`: http://docs.hieroglyph.io/en/latest/index.html
.. _`reStructuredText`: http://docutils.sourceforge.net/rst.html
.. _`Python`: https://www.python.org/
.. _`GenomeSciences541 Github`: https://github.com/jbloom/GenomeSciences541
.. _`Jesse Bloom`: http://research.fhcrc.org/bloom/en.html
