codon_table = {
    'Phe' : ['TTT', 'TTC'],
    'Leu' : ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile' : ['ATT', 'ATC', 'ATA'],
    'Met' : ['ATG'],
    'Val' : ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser' : ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro' : ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr' : ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala' : ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr' : ['TAT', 'TAC'],
    'His' : ['CAT', 'CAC'],
    'Gln' : ['CAA', 'CAG'],
    'Asn' : ['AAT', 'AAC'],
    'Lys' : ['AAA', 'AAG'],
    'Asp' : ['GAT', 'GAC'],
    'Glu' : ['GAA', 'GAG'],
    'Cys' : ['TGT', 'TGC'],
    'Trp' : ['TGG'],
    'Arg' : ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly' : ['GGT', 'GGC', 'GGA', 'GGG'],
    'STOP' : ['TAA', 'TAG', 'TGA']
}

codon_to_amino_acid = {}

for amino_acid in codon_table:
    codons = codon_table[amino_acid]
    for codon in codons:
        codon_to_amino_acid[codon] = amino_acid

def count_amino_acids(filename):
    with open(filename, 'r') as f:
        sequence = f.read().strip().upper()

    counts = {}

    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        aa = codon_to_amino_acid.get(codon, 'Unknown')

        if aa in counts:
            counts[aa] += 1
        else:
            counts[aa] = 1

    for amino_acid, count in counts.items():
        print(f"{amino_acid}: {count}")

file_path = input("Enter the path to the DNA sequence file: ")
count_amino_acids(file_path)

