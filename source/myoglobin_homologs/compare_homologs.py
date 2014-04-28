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
    unalignedprotfile = 'unaligned_proteins.fasta' # created alignment
    alignedprotfile = 'aligned_proteins.fasta' # created alignment
    aafreqsfile = 'aa_frequencies.txt' # created amino-acid frequences
    logoplot = 'myoglobin_site_preferences_logoplot.jpg' # created logo plot
    dsspfile = '1MBN_renumbered.dssp' # DSSP results

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
    open(alignedprotfile, 'w').write(''.join([">%s\n%s\n" % (host, prot[ : -1]) for (host, prot) in zip(species, alignedprots)])) # rewrite to eliminate line wrapping, stopc codons

    # determine amino-acid frequencies, make logo plot
    print "Writing amino-acid frequencies to %s" % aafreqsfile
    if os.path.isfile(aafreqsfile):
        os.remove(aafreqsfile)
    open('phyloExpCM_FreqsFromAlignment_infile.txt', 'w').write('\n'.join([\
            'alignmentfile %s' % alignedprotfile,
            'translateseqs False',
            'includestop False',
            'pseudocounts 0',
            'outputfile %s' % aafreqsfile]))
    os.system('phyloExpCM_FreqsFromAlignment.py phyloExpCM_FreqsFromAlignment_infile.txt')
    assert os.path.isfile(aafreqsfile), "Failed to create %s" % aafreqsfile
    print "Creating logo plot %s" % logoplot
    if os.path.isfile(logoplot):
        os.remove(logoplot)
    open('mapmuts_siteprofileplots_infile.txt', 'w').write('\n'.join([\
            'sitepreferences %s' % aafreqsfile,
            'outfileprefix myoglobin_',
            'siterange all',
            'dsspfile %s' % dsspfile,
            'dsspchain None',
            'add_rsa True',
            'add_ss True',
            'nperline 39',
            'includestop False']))
    os.system('mapmuts_siteprofileplots.py mapmuts_siteprofileplots_infile.txt')
    os.system('convert -density 300 %s.pdf %s' % (os.path.splitext(logoplot)[0], logoplot))
    assert os.path.isfile(logoplot), "Failed to create %s" % logoplot


    


main() # run the script
