"""Python script for comparing myoglobin homologs.

Written by Jesse Bloom."""


import os
import glob
import Bio.SeqIO
import Bio.Seq


def main():
    "Main body of script."""
    
    # input / output files
    genesubdir = './genes/' # subdirectory with genes
    probcons = '~/probcons/probcons' # path to PROBCONS executable
    unalignedprotfile = 'unaligned_proteins.fasta'
    alignedprotfile = 'aligned_proteins.fasta'

    # read the genes and corresponding species
    genes = []
    species = []
    for genefile in glob.glob("%s/*.fasta" % genesubdir):
        genes += [gene.seq for gene in Bio.SeqIO.parse(genefile, 'fasta')]
        species.append(os.path.basename(genefile).split('_')[0])
    print "Read %d genes from %s." % (len(genes), genefile)
    assert len(genes) == len(species), "Number of species didn't match, probably because some of the files have more than one sequence."

    # translate into corresponding proteins
    prots = []
    for (host, gene) in zip(species, genes):
        prots.append(gene.translate())

    # align the proteins
    print "Writing translated proteins to %s and aligning with %s to create %s" % (unalignedprotfile, probcons, alignedprotfile)
    if os.path.isfile(alignedprotfile):
        os.remove(alignedprotfile)
    f = open(unalignedprotfile, 'w')
    for (host, prot) in zip(species, prots):
        f.write('>%s\n%s\n\n' % (host, prot))
    f.close()
    os.system('%s %s > %s' % (probcons, unalignedprotfile, alignedprotfile))
    assert os.path.isfile(alignedprotfile), 'failed to create file %s' % alignedprotfile
    alignedprots = [aprot.seq for aprot in Bio.SeqIO.parse(alignedprotfile, 'fasta')]
    open(alignedprotfile, 'w').write(''.join([">%s\n%s\n" % (host, prot) for (host, prot) in zip(species, alignedprots)])) # rewrite to eliminate line wrapping
    


main() # run the script
