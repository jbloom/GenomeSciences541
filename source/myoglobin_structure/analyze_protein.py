"""``pymol`` script for labeling and analyzing PDB structure.

To run this script, open ``pymol``, go to the directory containing the
script, and run::

    run analyze_protein.py

This script written by Jesse Bloom."""


import os


def main():
    """Main body of script."""
    # subdictory for images
    image_dir = './png_images/'
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # load molecule 
    cmd.delete('everything')
    cmd.bg_color('white')
    cmd.load('1MBN.pdb', 'myoglobin')

    # set up static view        
    cmd.hide('everything')
    cmd.show('cartoon', 'myoglobin')
    cmd.color('gray', 'myoglobin')
    cmd.select('iron', 'elem FE')
    cmd.select('heme', 'resn HEM and not iron')
    cmd.show('sticks', 'heme')
    cmd.color('green', 'heme')
    cmd.show('spheres', 'iron')
    cmd.color('red', 'iron')
    cmd.select('his93', 'resi 93')
    cmd.show('sticks', 'his93')
    cmd.select('oxygen', 'resn OH')
    cmd.show('spheres', 'oxygen')
    cmd.color('blue', 'oxygen')
    cmd.set_view(\
            '-0.384154022,    0.878374994,    0.284453362,' +\
            '-0.627070785,   -0.474350274,    0.617919803,' +\
            '0.677684247,    0.059000824,    0.733017325,' +\
            '0.000000000,    0.000000000, -120.189903259,' +\
            '13.839839935,   20.989685059,    7.839759827,' +\
            '101.168441772,  141.655395508,    0.000000000')
    cmd.ray(1.5 * 1024, 1.5 * 768)
    cmd.png('%s/myoglobin_static.png' % image_dir)



main() # run the script
