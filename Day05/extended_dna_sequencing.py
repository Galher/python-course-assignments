import sys
import re

dna_nucleotides = {'A', 'C', 'G', 'T'}

def clean_sequence(sequence):
    clean = ""
    for nucleotide in sequence:
        if nucleotide in dna_nucleotides:
            clean += nucleotide
        else:
            break
    return clean

if len(sys.argv) != 2:
    print("Usage: python dna_sequencing.py <DNA_SEQUENCE>")
    sys.exit(1)

input_sequence = sys.argv[1].upper()
chunks = re.split('[^ACGT]+', input_sequence)
cleaned_chunks =[]
for chunk in chunks:
    if chunk:
        clean_chunk = clean_sequence(chunk)
        if clean_chunk != "":
            cleaned_chunks.append(clean_chunk)

print("Cleaned DNA sequences:", cleaned_chunks)

cleaned_chunks.sort(key=len, reverse=True)

print("Cleaned DNA sequences sorted by length:", cleaned_chunks)