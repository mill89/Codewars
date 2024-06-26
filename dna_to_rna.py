def dna_to_rna(dna: str) -> str:
    return dna.replace('T', 'U')


if __name__ == '__main__':
    print(dna_to_rna("GCAT"))

    assert dna_to_rna("TTTT") == "UUUU"
    assert dna_to_rna("GCAT") == "GCAU"
    assert dna_to_rna("GACCGCCGCC") == "GACCGCCGCC"
