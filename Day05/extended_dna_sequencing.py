import re

dna_nucleotides = {'A', 'C', 'G', 'T'}
input_sequence = input("Please enter a DNA sequence: ").upper()

def clean_sequence(sequence):
    clean = ""
    for nucleotide in sequence:
        if nucleotide in dna_nucleotides:
            clean += nucleotide
        else:
            break
    return clean

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