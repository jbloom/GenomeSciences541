"""Simple script for mutating a nucleotide sequence.

kappa is transition / transversion rate."""


import random

def main():
    """Body of script."""
    random.seed(1)
    seq = raw_input("Enter sequence: ").upper()
    kappa = float(raw_input("Enter kappa: "))
    nsubs = int(raw_input("Enter number of substitutions: "))
    for isub in range(nsubs):
        isite = random.randint(1, len(seq))
        print "Site = %d" % random.randint(1, len(seq))
        wt = seq[isite - 1]
        if random.random() < kappa / (2.0 + kappa):
            # transversion
            mut = {'A':'G', 'G':'A', 'C':'T', 'T':'C'}[wt]
        else:
            # transition 
            mut = random.choice({'A':['C', 'T'], 'C':['A', 'G'], 'G':['C', 'T'], 'T':['A', 'G']}[wt])
        seq = "%s%s%s" % (seq[ : isite - 1], mut, seq[isite : ])
        print "\nSubstitution %d is %s%d%s.\nNew sequence is:\n%s" % (isub + 1, wt, isite, mut, seq)
        raw_input("\nPress ENTER for the next mutation.")


main() # run the script


