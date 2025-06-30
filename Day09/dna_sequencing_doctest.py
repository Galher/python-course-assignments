dna_nucleotides = {'A', 'C', 'G', 'T'}

def clean_sequence(sequence):
    """
    Cleans a DNA sequence by keeping only valid nucleotides (A, C, G, T) 
    from the start until the first invalid character.

    Args:
        sequence (str): The DNA sequence string to clean.

    Returns:
        str: The cleaned DNA sequence up to the first invalid nucleotide.

    Examples:
    >>> clean_sequence("ACGTAGT")
    'ACGTAGT'
    >>> clean_sequence("ACGTBXZ")
    'ACGT'
    >>> clean_sequence("XYZ")
    ''
    >>> clean_sequence("")
    ''
    """
    clean = ""
    for nucleotide in sequence:
        if nucleotide in dna_nucleotides:
            clean += nucleotide
        else:
            break
    return clean
