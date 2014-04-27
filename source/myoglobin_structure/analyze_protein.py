"""``pymol`` script for labeling and analyzing PDB structure.

To run this script, open ``pymol``, go to the directory containing the
script, and run::

    run analyze_protein.py

This script written by Jesse Bloom."""



def main():
    """Main body of script."""
    cmd.load('1MBN.pdb', 'myoglobin')




main() # run the script
