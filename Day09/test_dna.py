from dna_sequencing_doctest import clean_sequence

def test_clean_sequence():
    assert clean_sequence("ACGTAGT") == "ACGTAGT"
    assert clean_sequence("ACGTBXZ") == "ACGT"
    assert clean_sequence("XYZ") == ""
    assert clean_sequence("") == "hi"
